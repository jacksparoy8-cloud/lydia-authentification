// Détecte automatiquement l'URL API selon l'environnement
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? '/api/send-telegram.php'
  : 'https://lydia-wero-design-production.up.railway.app/api/send-telegram.php';

window.TELEGRAM_API_URL = API_BASE_URL;
