#\!/usr/bin/env python3
import re
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
        print(f"Skipping {filename} - not found")
        continue
    
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        print(f"Error reading {filename}")
        continue
    
    # Remove Key Learnings section
    content = re.sub(
        r'<section[^>]*>\s*<h2[^>]*>Key Learnings</h2>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove Tools Used section
    content = re.sub(
        r'<section[^>]*>\s*<h2[^>]*>Tools Used</h2>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove emojis
    emoji_pattern = r'[\U0001F300-\U0001F9FF]'
    content = re.sub(emoji_pattern, '', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned {filename}")

print("All writeups cleaned\!")
