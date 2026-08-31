import re

# Lire le fichier
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Trouver et remplacer les media queries
old_media_768 = '''    @media (max-width: 768px) {
      .desktop-nav {
        display: none;
      }
      
      .mobile-menu-btn {
        display: block;
      }
      
      .mobile-nav {
        display: flex;
        flex-direction: column;
      }
      
      .mobile-menu-overlay.active {
        display: block;
        opacity: 1;
      }
      
      .mobile-menu-btn.active span:nth-child(1) {
        transform: rotate(45deg);
        top: 11px;
      }
      
      .mobile-menu-btn.active span:nth-child(2) {
        opacity: 0;
      }
      
      .mobile-menu-btn.active span:nth-child(3) {
        transform: rotate(-45deg);
        top: 11px;
      }
      
      .logo {
        font-size: 24px;
      }
      
      .hero h1 {
        font-size: 36px;
      }
      
      .hero p {
        font-size: 16px;
      }
      
      .btn-primary, .btn-secondary {
        padding: 16px 24px;
        font-size: 16px;
      }
      
      .iphone-container {
        width: 260px;
        height: 520px;
      }
      
      .amount-display {
        font-size: 36px;
      }
      
      .footer-content {
        flex-direction: column;
        gap: 30px;
        align-items: center;
      }
    }

    @media (max-width: 480px) {
      .hero h1 {
        font-size: 28px;
      }
      
      .hero p {
        font-size: 15px;
      }
      
      .btn-primary, .btn-secondary {
        padding: 14px 20px;
        font-size: 15px;
      }
      
      .notification {
        padding: 12px 20px;
        font-size: 14px;
      }
      
      .iphone-container {
        width: 240px;
        height: 480px;
      }

      .iphone-frame {
        padding: 12px;
        border-radius: 50px;
      }

      .iphone-inner {
        border-radius: 40px;
      }
    }'''

new_media = '''    @media (max-width: 1024px) {
      .iphone-container {
        width: 320px;
        height: 640px;
      }
    }

    @media (max-width: 768px) {
      .desktop-nav {
        display: none;
      }
      
      .mobile-menu-btn {
        display: block;
      }
      
      .mobile-nav {
        display: flex;
        flex-direction: column;
      }
      
      .mobile-menu-overlay.active {
        display: block;
        opacity: 1;
      }
      
      .mobile-menu-btn.active span:nth-child(1) {
        transform: rotate(45deg);
        top: 11px;
      }
      
      .mobile-menu-btn.active span:nth-child(2) {
        opacity: 0;
      }
      
      .mobile-menu-btn.active span:nth-child(3) {
        transform: rotate(-45deg);
        top: 11px;
      }
      
      .logo {
        font-size: 24px;
      }
      
      .hero {
        padding: 40px 0 30px;
      }
      
      .hero h1 {
        font-size: 32px;
        margin-bottom: 15px;
      }
      
      .hero p {
        font-size: 15px;
        margin-bottom: 20px;
      }
      
      .btn-primary, .btn-secondary {
        padding: 14px 20px;
        font-size: 15px;
      }
      
      .iphone-mockup {
        margin: 20px auto;
      }
      
      .iphone-container {
        width: 280px;
        height: 560px;
      }
      
      .iphone-frame {
        border-radius: 60px;
        padding: 14px;
        border: 10px solid #0a0a0a;
      }
      
      .iphone-inner {
        border-radius: 50px;
      }
      
      .lydia-logo-header {
        font-size: 28px;
        margin-bottom: 15px;
      }
      
      .transfer-card-container {
        max-width: 220px;
        padding: 18px;
      }
      
      .amount-display {
        font-size: 36px;
        margin-bottom: 16px;
      }
      
      .recipient-block {
        padding: 12px;
        gap: 10px;
      }
      
      .recipient-avatar {
        width: 40px;
        height: 40px;
        font-size: 14px;
      }
      
      .recipient-name {
        font-size: 12px;
      }
      
      .recipient-phone {
        font-size: 11px;
      }
      
      .progress-spinner {
        width: 24px;
        height: 24px;
      }
      
      .progress-text {
        font-size: 11px;
      }
      
      .notification {
        padding: 12px 20px;
        font-size: 13px;
        margin: 20px auto;
        gap: 10px;
      }
      
      .notification i {
        font-size: 16px;
      }
      
      .hero-buttons {
        gap: 15px;
        max-width: 320px;
      }
      
      .footer-content {
        flex-direction: column;
        gap: 30px;
        align-items: center;
      }
      
      .footer-section {
        min-width: 100%;
      }
    }

    @media (max-width: 600px) {
      .hero h1 {
        font-size: 28px;
      }
      
      .hero p {
        font-size: 14px;
      }
      
      .iphone-container {
        width: 240px;
        height: 480px;
      }
      
      .iphone-frame {
        border-radius: 50px;
        padding: 12px;
        border: 8px solid #0a0a0a;
      }
      
      .iphone-inner {
        border-radius: 40px;
      }
      
      .iphone-notch {
        width: 160px;
        height: 25px;
        border-radius: 0 0 25px 25px;
      }
      
      .screen-content-wrapper {
        padding-top: 40px;
      }
      
      .screen-inner {
        padding: 20px 15px;
      }
      
      .lydia-logo-header {
        font-size: 24px;
        margin-bottom: 12px;
      }
      
      .transfer-card-container {
        max-width: 200px;
        padding: 16px;
        border-radius: 20px;
      }
      
      .amount-display {
        font-size: 32px;
        margin-bottom: 14px;
      }
      
      .currency {
        font-size: 18px;
      }
      
      .transfer-direction {
        font-size: 11px;
        margin-bottom: 12px;
      }
      
      .recipient-block {
        padding: 10px;
        margin-bottom: 14px;
        border-radius: 14px;
      }
      
      .recipient-avatar {
        width: 36px;
        height: 36px;
        font-size: 12px;
      }
      
      .recipient-name {
        font-size: 11px;
      }
      
      .recipient-phone {
        font-size: 10px;
      }
      
      .transfer-progress {
        gap: 8px;
        padding-top: 14px;
      }
      
      .progress-spinner {
        width: 20px;
        height: 20px;
        border: 2px solid rgba(0, 102, 255, 0.15);
      }
      
      .progress-text {
        font-size: 10px;
      }
      
      .countdown-label {
        font-size: 9px;
        margin-top: 1px;
      }
      
      #countdownTimer {
        font-size: 24px;
      }
      
      .iphone-home-indicator {
        bottom: 6px;
        width: 100px;
        height: 4px;
      }
      
      .btn-primary, .btn-secondary {
        padding: 12px 16px;
        font-size: 14px;
        gap: 10px;
      }
      
      .btn-primary i, .btn-secondary i {
        font-size: 16px;
      }
      
      .hero-buttons {
        gap: 12px;
        max-width: 100%;
      }
      
      .notification {
        padding: 10px 16px;
        font-size: 12px;
        border-radius: 40px;
        margin: 15px 10px;
        gap: 8px;
      }
      
      .container {
        padding: 0 15px;
      }
      
      .hero {
        padding: 30px 0 20px;
      }
      
      .footer-section h3 {
        font-size: 18px;
        margin-bottom: 12px;
      }
      
      .footer-section p {
        font-size: 13px;
        margin-bottom: 10px;
      }
      
      .social-icons {
        gap: 12px;
      }
      
      .social-icons a {
        width: 36px;
        height: 36px;
        font-size: 16px;
      }
    }

    @media (max-width: 480px) {
      .logo {
        font-size: 20px;
        gap: 10px;
      }
      
      .logo-icon {
        width: 32px;
        height: 32px;
        font-size: 18px;
      }
      
      .hero h1 {
        font-size: 24px;
      }
      
      .hero p {
        font-size: 13px;
      }
      
      .iphone-container {
        width: 220px;
        height: 440px;
      }
      
      .iphone-frame {
        border-radius: 45px;
        padding: 10px;
        border: 7px solid #0a0a0a;
      }
      
      .iphone-inner {
        border-radius: 38px;
      }
      
      .screen-inner {
        padding: 15px 12px;
      }
      
      .lydia-logo-header {
        font-size: 20px;
        margin-bottom: 10px;
      }
      
      .transfer-card-container {
        max-width: 180px;
        padding: 14px;
        border-radius: 18px;
      }
      
      .amount-display {
        font-size: 28px;
        margin-bottom: 12px;
      }
      
      .currency {
        font-size: 16px;
      }
      
      .transfer-direction {
        font-size: 10px;
        margin-bottom: 10px;
      }
      
      .recipient-avatar {
        width: 32px;
        height: 32px;
        font-size: 11px;
      }
      
      .recipient-name {
        font-size: 10px;
      }
      
      .recipient-phone {
        font-size: 9px;
      }
      
      .progress-spinner {
        width: 18px;
        height: 18px;
        border: 2px solid rgba(0, 102, 255, 0.15);
      }
      
      .progress-text {
        font-size: 9px;
      }
      
      #countdownTimer {
        font-size: 20px;
      }
      
      .btn-primary, .btn-secondary {
        padding: 11px 14px;
        font-size: 13px;
        border-radius: 40px;
      }
      
      .notification {
        padding: 9px 14px;
        font-size: 11px;
        margin: 12px 10px;
      }
      
      .footer-content {
        gap: 20px;
        margin-bottom: 20px;
      }
      
      footer {
        padding: 40px 0 20px;
      }
      
      .footer-section h3 {
        font-size: 16px;
        margin-bottom: 10px;
      }
      
      .footer-section p {
        font-size: 12px;
      }
    }'''

content = content.replace(old_media, new_media)

# Écrire le fichier
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Responsivité améliorée!")
print("- Breakpoints: 1024px, 768px, 600px, 480px")
print("- Mockup iPhone optimisé pour mobile")
print("- Proportions adaptatives")
