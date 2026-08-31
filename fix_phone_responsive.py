# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer TOUS les media queries pour téléphone (480px et moins)
old_480 = '''    @media (max-width: 480px) {
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
    }'''

new_480 = '''    @media (max-width: 480px) {
      .hero { padding: 20px 0 15px; }
      .logo { font-size: 18px; }
      .logo-icon { width: 28px; height: 28px; font-size: 16px; }
      .hero h1 { font-size: 20px; }
      .hero p { font-size: 11px; }
      
      .iphone-container { width: 280px; height: 560px; }
      .iphone-frame { border-radius: 60px; padding: 14px; border: 10px solid #0a0a0a; }
      .iphone-inner { border-radius: 50px; }
      .iphone-notch { width: 170px; height: 27px; border-radius: 0 0 28px 28px; }
      .iphone-home-indicator { width: 120px; height: 5px; bottom: 7px; }
      
      .screen-content-wrapper { padding-top: 45px; }
      .screen-inner { padding: 25px 18px; }
      .lydia-logo-header { font-size: 32px; margin-bottom: 16px; }
      .transfer-card-container { max-width: 240px; padding: 18px; border-radius: 22px; }
      
      .transfer-direction { font-size: 10px; margin-bottom: 13px; gap: 7px; }
      .transfer-arrow-icon { width: 16px; height: 16px; font-size: 8px; }
      
      .amount-display { font-size: 38px; margin-bottom: 20px; }
      .currency { font-size: 21px; }
      
      .recipient-block { padding: 13px; margin-bottom: 16px; gap: 11px; border-radius: 15px; }
      .recipient-avatar { width: 42px; height: 42px; font-size: 14px; }
      .recipient-name { font-size: 12px; }
      .recipient-phone { font-size: 10px; }
      
      .transfer-progress { gap: 10px; padding-top: 15px; border-top: 1px solid rgba(0, 0, 0, 0.08); }
      .progress-spinner { width: 26px; height: 26px; border: 2px solid rgba(0, 102, 255, 0.15); }
      .progress-text { font-size: 11px; }
      #countdownTimer { font-size: 28px; }
      .countdown-label { font-size: 9px; margin-top: 2px; }
      
      .btn-primary, .btn-secondary { padding: 12px 16px; font-size: 14px; }
      .hero-buttons { gap: 12px; }
      .notification { padding: 11px 18px; font-size: 13px; margin: 18px 10px; }
      
      footer { padding: 35px 0 20px; }
      .footer-section h3 { font-size: 16px; margin-bottom: 12px; }
      .footer-section p { font-size: 13px; }
      .social-icons { gap: 12px; }
      .social-icons a { width: 36px; height: 36px; }
    }'''

content = content.replace(old_480, new_480)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
