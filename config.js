// Auto-detect API URL based on environment
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? '/api/send-telegram.php'
  : '/api/send-telegram';

window.TELEGRAM_API_URL = API_BASE_URL;
