import re

# Lire le fichier
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Modifications CSS
content = content.replace('width: 320px;', 'width: 420px;')
content = content.replace('height: 640px;', 'height: 840px;')
content = content.replace('border-radius: 60px;', 'border-radius: 80px;')
content = content.replace('padding: 14px;', 'padding: 18px;')
content = content.replace('border: 8px solid #0a0a0a;', 'border: 12px solid #0a0a0a;')
content = content.replace('border-radius: 52px;', 'border-radius: 68px;')

# Remplacer le texte du compte à rebours
content = content.replace(
    '<div class="progress-text">5 secondes</div>',
    '<div class="progress-text" id="countdownTimer">5</div><div class="countdown-label">secondes</div>'
)

# Ajouter les styles pour l'animation du compte à rebours
countdown_style = '''
    .countdown-label {
      font-size: 11px;
      color: var(--gray-dark);
      font-weight: 500;
      margin-top: 2px;
    }

    #countdownTimer {
      font-size: 32px;
      font-weight: 900;
      animation: countdownPulse 1s ease-in-out infinite;
    }

    @keyframes countdownPulse {
      0% {
        transform: scale(1);
        color: var(--primary-blue);
      }
      50% {
        transform: scale(1.15);
        color: #0052CC;
      }
      100% {
        transform: scale(1);
        color: var(--primary-blue);
      }
    }

    .countdown-end-animation {
      animation: countdownExplosion 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55) !important;
    }

    @keyframes countdownExplosion {
      0% {
        transform: scale(1);
        opacity: 1;
      }
      50% {
        transform: scale(1.3) rotate(5deg);
        opacity: 0.9;
      }
      100% {
        transform: scale(0.8) rotate(-5deg);
        opacity: 0.7;
      }
    }
'''

content = content.replace('    @keyframes progress {', countdown_style + '    @keyframes progress {')

# Ajouter le script du compte à rebours
countdown_script = '''
      // COUNTDOWN TIMER
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
      }
'''

content = content.replace('      elements.forEach(el => observer.observe(el));', countdown_script + '      elements.forEach(el => observer.observe(el));')

# Écrire le fichier
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
