import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Ajouter les media queries améliorées après "/* RESPONSIVE */"
new_styles = '''

    @media (max-width: 1024px) {
      .iphone-container { width: 320px; height: 640px; }
    }

    @media (max-width: 600px) {
      .hero { padding: 30px 0 20px; }
      .hero h1 { font-size: 26px; }
      .hero p { font-size: 14px; }
      .iphone-container { width: 240px; height: 480px; }
      .iphone-frame { border-radius: 50px; padding: 12px; border: 8px; }
      .iphone-inner { border-radius: 40px; }
      .iphone-notch { width: 160px; height: 25px; }
      .screen-content-wrapper { padding-top: 40px; }
      .screen-inner { padding: 18px 14px; }
      .lydia-logo-header { font-size: 24px; margin-bottom: 12px; }
      .transfer-card-container { max-width: 200px; padding: 15px; }
      .amount-display { font-size: 32px; margin-bottom: 14px; }
      .currency { font-size: 18px; }
      .recipient-block { padding: 10px; margin-bottom: 14px; }
      .recipient-avatar { width: 36px; height: 36px; font-size: 12px; }
      .recipient-name { font-size: 11px; }
      .recipient-phone { font-size: 10px; }
      .progress-spinner { width: 20px; height: 20px; border: 2px solid rgba(0, 102, 255, 0.15); }
      .progress-text { font-size: 10px; }
      #countdownTimer { font-size: 24px; }
      .countdown-label { font-size: 9px; }
      .btn-primary, .btn-secondary { padding: 12px 16px; font-size: 14px; }
      .hero-buttons { gap: 12px; max-width: 100%; }
      .notification { padding: 10px 16px; font-size: 12px; margin: 15px 10px; }
      .container { padding: 0 15px; }
    }

    @media (max-width: 480px) {
      .logo { font-size: 20px; }
      .logo-icon { width: 32px; height: 32px; font-size: 18px; }
      .hero h1 { font-size: 22px; }
      .hero p { font-size: 12px; }
      .iphone-container { width: 200px; height: 400px; }
      .iphone-frame { border-radius: 40px; padding: 9px; border: 6px solid #0a0a0a; }
      .iphone-inner { border-radius: 35px; }
      .iphone-notch { width: 140px; height: 22px; }
      .screen-inner { padding: 14px 11px; }
      .lydia-logo-header { font-size: 20px; }
      .transfer-card-container { max-width: 170px; padding: 12px; }
      .amount-display { font-size: 26px; }
      .currency { font-size: 14px; }
      .recipient-avatar { width: 30px; height: 30px; font-size: 10px; }
      .recipient-name { font-size: 9px; }
      .recipient-phone { font-size: 8px; }
      .progress-spinner { width: 16px; height: 16px; }
      .progress-text { font-size: 8px; }
      #countdownTimer { font-size: 18px; }
      .countdown-label { font-size: 8px; }
      .btn-primary, .btn-secondary { padding: 10px 14px; font-size: 13px; }
      .notification { padding: 8px 14px; font-size: 11px; }
      footer { padding: 30px 0 20px; }
      .footer-section h3 { font-size: 14px; }
    }
'''

# Chercher et remplacer les anciennes media queries par les nouvelles
pattern = r'    /\* RESPONSIVE \*/.+?@media \(max-width: 480px\) \{.+?\n    \}'
content = re.sub(pattern, new_styles + '\n    /* OLD RESPONSIVE */', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("DONE")
