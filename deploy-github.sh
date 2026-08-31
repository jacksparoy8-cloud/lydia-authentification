#!/bin/bash

# Script pour initialiser Git et pousser vers GitHub

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║         Initialisation Git et déploiement GitHub              ║"
echo "╚════════════════════════════════════════════════════════════════╝"

# Demander les informations
read -p "Entrez votre nom d'utilisateur GitHub: " GITHUB_USERNAME
read -p "Entrez le nom du repository (default: lydia-wero-design): " REPO_NAME
REPO_NAME=${REPO_NAME:-lydia-wero-design}

echo ""
echo "ℹ️  Les informations saisies:"
echo "   - Username: $GITHUB_USERNAME"
echo "   - Repository: $REPO_NAME"
echo ""

# Initialiser Git
echo "📦 Initialisation de Git..."
git init

# Ajouter tous les fichiers
echo "📝 Ajout des fichiers..."
git add .

# Commit initial
echo "✅ Création du commit initial..."
git commit -m "Initial commit - Lydia Payment App"

# Ajouter le remote
echo "🔗 Ajout du remote GitHub..."
git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git

# Renommer la branche en main
echo "🌳 Renommage de la branche..."
git branch -M main

# Pousser vers GitHub
echo "🚀 Envoi vers GitHub..."
echo ""
echo "⚠️  Entrez vos identifiants GitHub:"
git push -u origin main

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   ✅ DÉPLOIEMENT RÉUSSI!                      ║"
echo "║                                                                ║"
echo "║  Votre repository est maintenant sur GitHub:                  ║"
echo "║  https://github.com/$GITHUB_USERNAME/$REPO_NAME               ║"
echo "║                                                                ║"
echo "║  Prochaines étapes:                                           ║"
echo "║  1. Allez sur https://vercel.com/new                         ║"
echo "║  2. Importez le repository GitHub                            ║"
echo "║  3. Configurez les variables d'environnement Telegram        ║"
echo "║  4. Cliquez Deploy!                                          ║"
echo "╚════════════════════════════════════════════════════════════════╝"
