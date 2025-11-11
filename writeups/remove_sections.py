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
        continue
    
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Remove Key Learnings section - more flexible pattern
    content = re.sub(
        r'<\!-- Key Learnings -->.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'<section[^>]*>\s*<h2[^>]*>\s*Key Learnings\s*</h2>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Remove Tools Used section
    content = re.sub(
        r'<\!-- Tools -->.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    content = re.sub(
        r'<section[^>]*>\s*<h2[^>]*>.*?Tools Used\s*</h2>.*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned {filename}")

print("All sections removed\!")
