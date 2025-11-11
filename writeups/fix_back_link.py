#\!/usr/bin/env python3
import os

writeups = [
    'exploit-100-2.html',
    'exploit-100-4.html', 
    'exploit-200-2.html',
    'exploit-300-1.html',
    'reverse-100-1.html',
    'reverse-100-2.html',
    'reverse-100-3.html',
    'reverse-100-4.html',
    'reverse-200-2.html',
    'reverse-200-3.html',
    'reverse-300-1.html',
    'reverse-300-2.html'
]

for filename in writeups:
    filepath = f'/home/elw00/ctf-site/writeups/{filename}'
    
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Fix the back link
    content = content.replace('href="../ctf-new.html"', 'href="../index.html"')
    content = content.replace('href="../ctf.html"', 'href="../index.html"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filename}")

print("All back links fixed\!")
