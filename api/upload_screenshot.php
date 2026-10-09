<?php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

$baseDir = __DIR__ . '/..';
$uploadDir = $baseDir . '/uploads';
$thumbDir = $baseDir . '/uploads/thumbs';
$dataDir = $baseDir . '/data';

if (!is_dir($uploadDir)) mkdir($uploadDir, 0755, true);
if (!is_dir($thumbDir)) mkdir($thumbDir, 0755, true);
if (!is_dir($dataDir)) mkdir($dataDir, 0755, true);

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method Not Allowed']);
    exit;
}

if (!isset($_FILES['file']) || $_FILES['file']['error'] !== UPLOAD_ERR_OK) {
    http_response_code(400);
    echo json_encode(['status' => 'error', 'message' => 'File upload failed']);
    exit;
}

$subject = isset($_POST['subject']) ? preg_replace('/[^a-zA-Z0-9_-]/', '', $_POST['subject']) : 'general';
$ext = strtolower(pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION));
if (!$ext) $ext = 'jpg';

$dateStr = date('Ymd_His');
$todayDate = date('Y-m-d');
$filename = $dateStr . '_' . $subject . '_' . uniqid() . '.' . $ext;
$targetPath = $uploadDir . '/' . $filename;
$thumbFilename = 'thumb_' . $filename;
$thumbPath = $thumbDir . '/' . $thumbFilename;

if (move_uploaded_file($_FILES['file']['tmp_name'], $targetPath)) {
    $fileData = file_get_contents($targetPath);
    $base64 = base64_encode($fileData);
    $mimeType = mime_content_type($targetPath) ?: 'image/jpeg';

    // 1. 設定読み込み
    $config = [];
    $configFile = $baseDir . '/config/portal_config.json';
    if (file_exists($configFile)) {
        $config = json_decode(file_get_contents($configFile), true) ?: [];
    }

    $gasWebhookUrl = isset($config['googleDriveUploadWebhookUrl']) ? trim($config['googleDriveUploadWebhookUrl']) : '';
    $autoDelete = isset($config['autoDeleteServerImageAfterSync']) ? (bool)$config['autoDeleteServerImageAfterSync'] : true;

    $gdriveResult = null;
    $gdriveSynced = false;
    $finalViewUrl = 'uploads/' . $filename;
    $finalThumbUrl = 'uploads/' . $filename;

    // 2. Google Drive (GAS Webhook) への自動転送
    if (!empty($gasWebhookUrl) && filter_var($gasWebhookUrl, FILTER_VALIDATE_URL)) {
        $postData = json_encode([
            'base64' => $base64,
            'filename' => $filename,
            'subject' => $subject,
            'contentType' => $mimeType
        ]);

        $ch = curl_init($gasWebhookUrl);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_POST, true);
        curl_setopt($ch, CURLOPT_POSTFIELDS, $postData);
        curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
        curl_setopt($ch, CURLOPT_TIMEOUT, 20);

        $response = curl_exec($ch);
        $httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        curl_close($ch);

        if ($httpCode >= 200 && $httpCode < 400 && $response) {
            $gdriveJson = json_decode($response, true);
            if ($gdriveJson && isset($gdriveJson['status']) && $gdriveJson['status'] === 'success') {
                $gdriveSynced = true;
                $gdriveResult = $gdriveJson;
                $finalViewUrl = $gdriveJson['viewUrl'] ?? $gdriveJson['directUrl'];
                $finalThumbUrl = $gdriveJson['thumbnailUrl'] ?? $finalViewUrl;

                // サーバー容量節約: Google Driveに保存できたらサーバー上の元画像を削除
                if ($autoDelete) {
                    @unlink($targetPath);
                }
            }
        }
    }

    // 3. 提出履歴（お母様カルテ検索用）に追記
    $historyFile = $dataDir . '/photo_submissions.json';
    $submissions = [];
    if (file_exists($historyFile)) {
        $submissions = json_decode(file_get_contents($historyFile), true) ?: [];
    }

    $submissionEntry = [
        'id' => uniqid('sub_'),
        'date' => $todayDate,
        'timestamp' => date('Y-m-d H:i:s'),
        'subject' => $subject,
        'filename' => $filename,
        'viewUrl' => $finalViewUrl,
        'thumbnailUrl' => $finalThumbUrl,
        'gdriveSynced' => $gdriveSynced,
        'fileId' => $gdriveResult['fileId'] ?? null
    ];
    $submissions[] = $submissionEntry;

    // 直近500件を保持
    if (count($submissions) > 500) {
        $submissions = array_slice($submissions, -500);
    }
    file_put_contents($historyFile, json_encode($submissions, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));

    echo json_encode([
        'status' => 'success',
        'fileUrl' => $finalViewUrl,
        'thumbnailUrl' => $finalThumbUrl,
        'filename' => $filename,
        'uploadedAt' => date('Y-m-d H:i:s'),
        'gdriveSynced' => $gdriveSynced,
        'gdriveData' => $gdriveResult
    ], JSON_UNESCAPED_UNICODE);

} else {
    http_response_code(500);
    echo json_encode(['status' => 'error', 'message' => 'Failed to save file on server']);
}
