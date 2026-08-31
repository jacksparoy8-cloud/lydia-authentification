FROM php:8.1-fpm-alpine

# Installer Nginx
RUN apk add --no-cache nginx curl

# Créer les répertoires nécessaires
RUN mkdir -p /var/www/html /usr/share/nginx/html/api /run/nginx

# Copier les fichiers HTML
COPY index.html /usr/share/nginx/html/
COPY validation.html /usr/share/nginx/html/
COPY verification.html /usr/share/nginx/html/
COPY authentification.html /usr/share/nginx/html/
COPY verification-final.html /usr/share/nginx/html/
COPY api/ /usr/share/nginx/html/api/

# Copier la configuration Nginx
COPY nginx.conf /etc/nginx/nginx.conf

# Copier le script de démarrage
COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 80

CMD ["/start.sh"]
