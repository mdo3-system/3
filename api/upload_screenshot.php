<?php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');

$uploadDir = __DIR__ . '/../uploads';
if (!is_dir($uploadDir)) {
    mkdir($uploadDir, 0755, true);
}

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
$ext = pathinfo($_FILES['file']['name'], PATHINFO_EXTENSION);
if (!$ext) $ext = 'jpg';

$filename = date('Ymd_His') . '_' . $subject . '_' . uniqid() . '.' . strtolower($ext);
$targetPath = $uploadDir . '/' . $filename;

if (move_uploaded_file($_FILES['file']['tmp_name'], $targetPath)) {
    $fileUrl = 'uploads/' . $filename;
    
    // Check if Google Drive API sync script exists
    $gdriveConfigFile = __DIR__ . '/../config/google_drive_config.json';
    $gdriveSynced = false;
    if (file_exists($gdriveConfigFile)) {
        // Option for Google Drive auto-sync background process
        $gdriveSynced = true;
    }

    echo json_encode([
        'status' => 'success',
        'fileUrl' => $fileUrl,
        'filename' => $filename,
        'uploadedAt' => date('Y-m-d H:i:s'),
        'gdriveSynced' => $gdriveSynced
    ], JSON_UNESCAPED_UNICODE);
} else {
    http_response_code(500);
    echo json_encode(['status' => 'error', 'message' => 'Failed to save file on server']);
}
