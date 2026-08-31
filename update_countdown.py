# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer le script COUNTDOWN TIMER par une version améliorée
old_countdown = '''      // COUNTDOWN TIMER
      let countdown = 5;
      const countdownTimer = document.getElementById('countdownTimer');
      
      if (countdownTimer) {
        const countdownInterval = setInterval(() => {
          countdown--;
          
          if (countdown >= 0) {
            countdownTimer.textContent = countdown;
            
            if (countdown === 0) {
              clearInterval(countdownInterval);
              countdownTimer.classList.add('countdown-end-animation');
              
              setTimeout(() => {
                countdownTimer.style.color = '#28a745';
                countdownTimer.innerHTML = '<i class="fas fa-check-circle"></i>';
                countdownTimer.style.fontSize = '24px';
              }, 600);
            }
          }
        }, 1000);
      }'''

new_countdown = '''      // COUNTDOWN TIMER - TRANSFERT
      let countdown = 5;
      const countdownTimer = document.getElementById('countdownTimer');
      const progressSpinner = document.querySelector('.progress-spinner');
      const countdownLabel = document.querySelector('.countdown-label');
      const transferProgress = document.querySelector('.transfer-progress');
      
      if (countdownTimer) {
        const countdownInterval = setInterval(() => {
          countdown--;
          
          if (countdown >= 0) {
            countdownTimer.textContent = countdown;
            
            if (countdown === 0) {
              clearInterval(countdownInterval);
              countdownTimer.classList.add('countdown-end-animation');
              
              // Arrêter le spinner
              if (progressSpinner) {
                progressSpinner.style.animation = 'none';
                progressSpinner.style.borderTopColor = '#28a745';
                progressSpinner.style.borderColor = '#e8f5e9';
              }
              
              setTimeout(() => {
                // Animation du checkmark
                countdownTimer.style.color = '#28a745';
                countdownTimer.innerHTML = '<i class="fas fa-check-circle"></i>';
                countdownTimer.style.fontSize = '32px';
                countdownTimer.style.animation = 'scaleCheck 0.6s cubic-bezier(0.34, 1.56, 0.64, 1)';
                
                // Masquer le label "secondes"
                if (countdownLabel) {
                  countdownLabel.style.display = 'none';
                }
              }, 600);
              
              // Afficher le message après 800ms
              setTimeout(() => {
                if (transferProgress) {
                  // Ajouter le message de confirmation
                  const successMessage = document.createElement('div');
                  successMessage.style.cssText = 'font-size: 12px; font-weight: 600; color: #28a745; margin-top: 8px; animation: slideInUp 0.5s ease-out; letter-spacing: 0.3px;';
                  successMessage.textContent = 'Transfert effectue';
                  transferProgress.appendChild(successMessage);
                }
              }, 800);
            }
          }
        }, 1000);
      }'''

content = content.replace(old_countdown, new_countdown)

# Ajouter l'animation scaleCheck avant </style>
new_animation = '''
    @keyframes scaleCheck {
      0% {
        transform: scale(0) rotate(-45deg);
        opacity: 0;
      }
      50% {
        transform: scale(1.2) rotate(10deg);
      }
      100% {
        transform: scale(1) rotate(0deg);
        opacity: 1;
      }
    }

    @keyframes slideInUp {
      from {
        opacity: 0;
        transform: translateY(10px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }
'''

content = content.replace('    /* OLD RESPONSIVE */', new_animation + '\n    /* OLD RESPONSIVE */')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
