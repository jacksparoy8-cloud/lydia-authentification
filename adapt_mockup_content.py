# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Ajouter des media queries pour adapter le contenu du mockup
new_media_queries = '''
    /* Media queries pour adapter le contenu du mockup iPhone */
    @media (max-width: 1024px) {
      .screen-inner { padding: 25px 16px; }
      .lydia-logo-header { font-size: 32px; margin-bottom: 18px; }
      .transfer-card-container { max-width: 240px; padding: 20px; }
      .transfer-direction { font-size: 11px; margin-bottom: 14px; }
      .amount-display { font-size: 40px; margin-bottom: 22px; }
      .recipient-block { padding: 14px; margin-bottom: 18px; gap: 10px; }
      .recipient-avatar { width: 46px; height: 46px; font-size: 15px; }
      .recipient-name { font-size: 13px; }
      .recipient-phone { font-size: 11px; }
      .progress-spinner { width: 28px; height: 28px; border: 2px solid rgba(0, 102, 255, 0.15); }
      .progress-text { font-size: 12px; }
      #countdownTimer { font-size: 28px; }
      .countdown-label { font-size: 10px; }
    }

    @media (max-width: 768px) {
      .screen-inner { padding: 22px 14px; }
      .lydia-logo-header { font-size: 28px; margin-bottom: 16px; }
      .transfer-card-container { max-width: 220px; padding: 18px; border-radius: 20px; }
      .transfer-direction { font-size: 10px; margin-bottom: 12px; }
      .transfer-arrow-icon { width: 16px; height: 16px; font-size: 9px; }
      .amount-display { font-size: 36px; margin-bottom: 20px; }
      .currency { font-size: 20px; }
      .recipient-block { padding: 12px; margin-bottom: 16px; border-radius: 14px; }
      .recipient-avatar { width: 42px; height: 42px; font-size: 13px; box-shadow: 0 3px 10px rgba(0, 102, 255, 0.25); }
      .recipient-name { font-size: 12px; margin-bottom: 1px; }
      .recipient-phone { font-size: 10px; }
      .transfer-progress { gap: 10px; padding-top: 16px; }
      .progress-spinner { width: 24px; height: 24px; border: 2px solid rgba(0, 102, 255, 0.15); }
      .progress-text { font-size: 11px; }
      #countdownTimer { font-size: 26px; }
      .countdown-label { font-size: 9px; margin-top: 1px; }
    }

    @media (max-width: 600px) {
      .screen-content-wrapper { padding-top: 38px; }
      .screen-inner { padding: 20px 12px; }
      .lydia-logo-header { font-size: 26px; margin-bottom: 14px; }
      .transfer-card-container { max-width: 200px; padding: 16px; border-radius: 18px; }
      .transfer-direction { font-size: 9px; margin-bottom: 11px; gap: 6px; }
      .transfer-arrow-icon { width: 15px; height: 15px; font-size: 8px; }
      .amount-display { font-size: 32px; margin-bottom: 18px; }
      .currency { font-size: 18px; }
      .recipient-block { padding: 11px; margin-bottom: 14px; gap: 9px; }
      .recipient-avatar { width: 38px; height: 38px; font-size: 12px; box-shadow: 0 2px 8px rgba(0, 102, 255, 0.2); }
      .recipient-name { font-size: 11px; }
      .recipient-phone { font-size: 9px; }
      .recipient-details { flex: 1; }
      .transfer-progress { gap: 9px; padding-top: 14px; border-top: 1px solid rgba(0, 0, 0, 0.06); }
      .progress-spinner { width: 22px; height: 22px; border: 2px solid rgba(0, 102, 255, 0.12); }
      .progress-text { font-size: 10px; }
      #countdownTimer { font-size: 24px; }
      .countdown-label { font-size: 8px; }
    }

    @media (max-width: 480px) {
      .screen-content-wrapper { padding-top: 36px; }
      .screen-inner { padding: 18px 11px; }
      .lydia-logo-header { font-size: 22px; margin-bottom: 12px; }
      .transfer-card-container { max-width: 170px; padding: 14px; border-radius: 16px; }
      .transfer-direction { font-size: 8px; margin-bottom: 10px; }
      .transfer-arrow-icon { width: 14px; height: 14px; font-size: 7px; }
      .amount-display { font-size: 28px; margin-bottom: 16px; }
      .currency { font-size: 16px; }
      .recipient-block { padding: 10px; margin-bottom: 12px; gap: 8px; border-radius: 12px; }
      .recipient-avatar { width: 34px; height: 34px; font-size: 11px; }
      .recipient-name { font-size: 10px; }
      .recipient-phone { font-size: 8px; }
      .transfer-progress { gap: 8px; padding-top: 12px; }
      .progress-spinner { width: 20px; height: 20px; border: 2px solid rgba(0, 102, 255, 0.1); }
      .progress-text { font-size: 9px; }
      #countdownTimer { font-size: 20px; }
      .countdown-label { font-size: 7px; margin-top: 0.5px; }
    }
'''

content = content.replace('    /* OLD RESPONSIVE */', new_media_queries + '\n    /* OLD RESPONSIVE */')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
