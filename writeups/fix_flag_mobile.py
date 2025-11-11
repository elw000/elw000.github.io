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
    
    # Fix flag section for mobile
    # Change from flex items-center to flex-col or wrap
    old_pattern = r'(<div class="bg-gradient-to-r from-green-900/50 to-emerald-900/50 border border-green-500/30 rounded-lg p-6">)\s*(<div class="flex items-center gap-3">)\s*(<i class="ph-bold ph-check-circle text-3xl text-green-400"></i>)\s*(<code class="text-xl font-mono text-green-400">.*?</code>)'
    
    new_replacement = r'\1\n                <div class="flex flex-col sm:flex-row items-start sm:items-center gap-3">\n                    \3\n                    \4'
    
    content = re.sub(old_pattern, new_replacement, content, flags=re.DOTALL)
    
    # Also make code responsive
    content = re.sub(
        r'<code class="text-xl font-mono text-green-400">',
        '<code class="text-sm sm:text-xl font-mono text-green-400 break-all">',
        content
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Fixed {filename}")

print("All flags fixed for mobile\!")
