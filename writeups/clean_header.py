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
    
    # Remove points display (e.g., "300 points")
    content = re.sub(
        r'<span class="text-2xl font-bold text-[^"]*-400">\d+ points</span>',
        '',
        content
    )
    
    # Remove the entire date/time section
    content = re.sub(
        r'<div class="flex items-center gap-6 text-sm text-slate-400">.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )
    
    # Clean up extra spacing in header
    content = re.sub(
        r'(<h1 class="text-4xl font-bold text-white mb-4">.*?</h1>)\s*</div>',
        r'\1\n            </div>',
        content,
        flags=re.DOTALL
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Cleaned {filename}")

print("All headers cleaned\!")
