<?php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

$baseDir = __DIR__ . '/..';
$dataDir = $baseDir . '/data';

$progressFile = $dataDir . '/son_progress.json';
$photosFile = $dataDir . '/photo_submissions.json';
$configFile = $baseDir . '/config/portal_config.json';

$progress = file_exists($progressFile) ? (json_decode(file_get_contents($progressFile), true) ?: []) : [];
$photos = file_exists($photosFile) ? (json_decode(file_get_contents($photosFile), true) ?: []) : [];
$config = file_exists($configFile) ? (json_decode(file_get_contents($configFile), true) ?: []) : [];

$queryDate = isset($_GET['date']) ? trim($_GET['date']) : '';

// 写真リストの抽出
$filteredPhotos = [];
if (!empty($queryDate)) {
    foreach ($photos as $p) {
        if (isset($p['date']) && $p['date'] === $queryDate) {
            $filteredPhotos[] = $p;
        }
    }
} else {
    $filteredPhotos = array_reverse(array_slice($photos, -50));
}

// 利用可能な日付一覧（カレンダー検索用）
$availableDates = [];
if (isset($progress['history']) && is_array($progress['history'])) {
    foreach ($progress['history'] as $h) {
        if (isset($h['date']) && !in_array($h['date'], $availableDates)) {
            $availableDates[] = $h['date'];
        }
    }
}
foreach ($photos as $p) {
    if (isset($p['date']) && !in_array($p['date'], $availableDates)) {
        $availableDates[] = $p['date'];
    }
}
rsort($availableDates);

echo json_encode([
    'status' => 'success',
    'queryDate' => $queryDate ?: date('Y-m-d'),
    'photos' => $filteredPhotos,
    'allPhotosCount' => count($photos),
    'progress' => $progress,
    'availableDates' => array_values(array_unique($availableDates)),
    'parentDriveFolderUrl' => $config['parentGoogleDriveFolderUrl'] ?? 'https://drive.google.com',
    'gdriveWebhookConfigured' => !empty($config['googleDriveUploadWebhookUrl'])
], JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT);
