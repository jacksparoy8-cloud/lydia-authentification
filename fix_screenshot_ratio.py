# -*- coding: utf-8 -*-
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer le CSS du mockup iPhone pour que le contenu soit en ratio 9:18 (capture d'écran)
old_iphone = '''    .iphone-inner {
      position: relative;
      width: 100%;
      height: 100%;
      background: #f5f5f5;
      border-radius: 68px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.1);
    }'''

new_iphone = '''    .iphone-inner {
      position: relative;
      width: 100%;
      height: 100%;
      background: #f5f5f5;
      border-radius: 68px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: inset 0 0 15px rgba(0, 0, 0, 0.1);
      aspect-ratio: 9 / 18;
    }'''

content = content.replace(old_iphone, new_iphone)

# Aussi s'assurer que le container maintient ce ratio
old_container = '''    .iphone-container {
      position: relative;
      width: 420px;
      height: 840px;
      perspective: 1200px;
      filter: drop-shadow(0 40px 80px rgba(0, 0, 0, 0.25));
    }'''

new_container = '''    .iphone-container {
      position: relative;
      width: 420px;
      height: 840px;
      perspective: 1200px;
      filter: drop-shadow(0 40px 80px rgba(0, 0, 0, 0.25));
      aspect-ratio: 9 / 18;
    }'''

content = content.replace(old_container, new_container)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("OK")
