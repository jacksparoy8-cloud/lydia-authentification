# Script PowerShell pour initialiser Git et pousser vers GitHub

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  Initialisation Git et deploiement GitHub" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Demander les informations
$GITHUB_USERNAME = Read-Host "Entrez votre nom d'utilisateur GitHub"
$REPO_NAME = Read-Host "Entrez le nom du repository (default: lydia-wero-design)"
if ([string]::IsNullOrWhiteSpace($REPO_NAME)) {
    $REPO_NAME = "lydia-wero-design"
}

Write-Host ""
Write-Host "Informations saisies:" -ForegroundColor Yellow
Write-Host "- Username: $GITHUB_USERNAME"
Write-Host "- Repository: $REPO_NAME"
Write-Host ""

# Initialiser Git
Write-Host "Initialisation de Git..." -ForegroundColor Green
git init

# Ajouter tous les fichiers
Write-Host "Ajout des fichiers..." -ForegroundColor Green
git add .

# Commit initial
Write-Host "Creation du commit initial..." -ForegroundColor Green
git commit -m "Initial commit - Lydia Payment App"

# Ajouter le remote
Write-Host "Ajout du remote GitHub..." -ForegroundColor Green
git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git

# Renommer la branche en main
Write-Host "Renommage de la branche..." -ForegroundColor Green
git branch -M main

# Pousser vers GitHub
Write-Host "Envoi vers GitHub..." -ForegroundColor Green
Write-Host ""
Write-Host "Entrez vos identifiants GitHub:" -ForegroundColor Yellow
git push -u origin main

Write-Host ""
Write-Host "================================================" -ForegroundColor Green
Write-Host "  DEPLOIEMENT REUSSI!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Votre repository est sur GitHub:" -ForegroundColor Green
Write-Host "https://github.com/$GITHUB_USERNAME/$REPO_NAME" -ForegroundColor Green
Write-Host ""
Write-Host "Prochaines etapes:" -ForegroundColor Green
Write-Host "1. Allez sur https://vercel.com/new" -ForegroundColor Green
Write-Host "2. Importez le repository GitHub" -ForegroundColor Green
Write-Host "3. Configurez les variables Telegram" -ForegroundColor Green
Write-Host "4. Cliquez Deploy!" -ForegroundColor Green
