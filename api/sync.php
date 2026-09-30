<?php
header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET, POST, OPTIONS');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'OPTIONS') {
    exit;
}

$dataDir = __DIR__ . '/../data';
if (!is_dir($dataDir)) {
    mkdir($dataDir, 0755, true);
}

$dataFile = $dataDir . '/son_progress.json';

if ($_SERVER['REQUEST_METHOD'] === 'GET') {
    if (file_exists($dataFile)) {
        echo file_get_contents($dataFile);
    } else {
        echo json_encode([
            'status' => 'success',
            'data' => [
                'taskState' => new stdClass(),
                'history' => [],
                'slackingDays' => 0,
                'playCounts' => new stdClass(),
                'updatedAt' => null
            ]
        ], JSON_UNESCAPED_UNICODE);
    }
    exit;
}

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $raw = file_get_contents('php://input');
    $json = json_decode($raw, true);

    if (!$json) {
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid JSON']);
        exit;
    }

    $json['updatedAt'] = date('Y-m-d H:i:s');
    file_put_contents($dataFile, json_encode($json, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT));

    echo json_encode(['status' => 'success', 'updatedAt' => $json['updatedAt']]);
    exit;
}
