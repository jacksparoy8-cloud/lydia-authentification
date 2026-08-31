# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Ajouter un style pour désactiver les liens automatiques sur les numéros de téléphone
css_fix = '''
    /* Désactiver les liens automatiques sur les numéros de téléphone */
    a[href^="tel:"] {
      color: inherit;
      text-decoration: none;
      pointer-events: none;
      cursor: default;
    }
    
    .recipient-phone {
      font-size: 10px;
      color: var(--gray-dark);
      font-weight: 400;
      pointer-events: none;
      -webkit-touch-callout: none;
      user-select: none;
    }
'''

content = content.replace('    /* OLD RESPONSIVE */', css_fix + '\n    /* OLD RESPONSIVE */')

# Aussi ajouter un attribut à la meta viewport pour éviter la détection automatique
content = content.replace(
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
    '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n  <meta name="format-detection" content="telephone=no">'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
