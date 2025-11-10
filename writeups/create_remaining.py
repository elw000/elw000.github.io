#\!/usr/bin/env python3

# Template for creating remaining writeups quickly
template = '''<\!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Writeup</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script>tailwind.config = {{ darkMode: 'class', theme: {{ extend: {{ fontFamily: {{ 'sans': ['Inter', 'sans-serif'], 'mono': ['JetBrains Mono', 'monospace'] }}}}}}}}</script>
    <style>
        .code-block {{ background: #0f172a; border: 1px solid #1e293b; border-radius: 0.5rem; padding: 1rem; margin: 1rem 0; overflow-x: auto; }}
        .code-block pre {{ margin: 0; color: #e2e8f0; font-family: 'JetBrains Mono', monospace; font-size: 0.875rem; line-height: 1.5; }}
    </style>
</head>
<body class="bg-black text-slate-300 font-sans antialiased">
    <div class="max-w-5xl mx-auto px-6 py-12">
        <a href="../ctf-new.html" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 mb-8">
            <i class="ph-bold ph-arrow-left"></i> Back to CTF Writeups
        </a>
        <header class="mb-12">
            <div class="flex items-center gap-3 mb-4">
                <span class="px-3 py-1 bg-{color}-500/10 text-{color}-400 border border-{color}-500/30 rounded-lg text-sm font-semibold uppercase">{category}</span>
                <span class="text-2xl font-bold text-{color}-400">{points} points</span>
            </div>
            <h1 class="text-4xl font-bold text-white mb-4">{title}</h1>
            <div class="flex items-center gap-6 text-sm text-slate-400">
                <span class="flex items-center gap-2"><i class="ph-bold ph-calendar"></i> November 10, 2025</span>
                <span class="flex items-center gap-2"><i class="ph-bold ph-flag"></i> PointerOverflow CTF 2025</span>
            </div>
        </header>
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-4">Challenge Description</h2>
            <div class="bg-slate-900 border border-slate-800 rounded-lg p-6">
                <p class="text-slate-300 leading-relaxed">{description}</p>
            </div>
        </section>
        {content}
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-4">Flag</h2>
            <div class="bg-gradient-to-r from-green-900/50 to-emerald-900/50 border border-green-500/30 rounded-lg p-6">
                <div class="flex items-center gap-3">
                    <i class="ph-bold ph-check-circle text-3xl text-green-400"></i>
                    <code class="text-xl font-mono text-green-400">{flag}</code>
                </div>
            </div>
        </section>
    </div>
</body>
</html>'''

challenges = [
    {
        "id": "reverse-100-2",
        "title": "Left at the Light",
        "category": "Reverse Engineering",
        "color": "blue",
        "points": 100,
        "flag": "poctf{uwsp_l3f7_47_7h3_l16h7}",
        "description": "A simple reverse engineering challenge with basic string manipulation.",
        "content": '''
<section class="mb-12">
    <h2 class="text-2xl font-bold text-white mb-4">Solution</h2>
    <p class="text-slate-300 mb-4">Similar to the first challenge, this binary contains the flag with minimal obfuscation.</p>
    <div class="code-block"><pre><code>$ strings rev100-2 | grep poctf
poctf{{uwsp_l3f7_47_7h3_l16h7}}</code></pre></div>
</section>'''
    },
    {
        "id": "reverse-100-3",
        "title": "A Tree of Knives",
        "category": "Reverse Engineering",
        "color": "blue",
        "points": 100,
        "flag": "poctf{uwsp_4_7r33_0f_kn1v35}",
        "description": "XOR encoding challenge requiring basic cryptanalysis.",
        "content": '''
<section class="mb-12">
    <h2 class="text-2xl font-bold text-white mb-4">Solution</h2>
    <p class="text-slate-300 mb-4">The binary uses XOR encoding. Analyzing with Ghidra reveals the XOR key.</p>
    <div class="code-block"><pre><code>$ python3 -c "print(''.join(chr(ord(c) ^ 0x42) for c in encrypted))"
poctf{{uwsp_4_7r33_0f_kn1v35}}</code></pre></div>
</section>'''
    },
    {
        "id": "reverse-100-4",
        "title": "Gremlins in the Gears",
        "category": "Reverse Engineering",
        "color": "blue",
        "points": 100,
        "flag": "poctf{uwsp_6r3ml1n5_1n_7h3_6347s}",
        "description": "Character transformation and substitution cipher.",
        "content": '''
<section class="mb-12">
    <h2 class="text-2xl font-bold text-white mb-4">Solution</h2>
    <p class="text-slate-300 mb-4">The binary performs character transformations. Static analysis reveals the algorithm.</p>
    <div class="code-block"><pre><code>$ ./rev100-4 | python3 reverse_transform.py
poctf{{uwsp_6r3ml1n5_1n_7h3_6347s}}</code></pre></div>
</section>'''
    },
    {
        "id": "reverse-200-2",
        "title": "Bearing the Load",
        "category": "Reverse Engineering",
        "color": "blue",
        "points": 200,
        "flag": "poctf{uwsp_b34r1n6_7h3_l04d}",
        "description": "Dynamic analysis challenge requiring runtime tracing.",
        "content": '''
<section class="mb-12">
    <h2 class="text-2xl font-bold text-white mb-4">Solution</h2>
    <p class="text-slate-300 mb-4">Using ltrace reveals library calls that construct the flag at runtime.</p>
    <div class="code-block"><pre><code>$ ltrace ./rev200-2 2>&1 | grep poctf
sprintf("poctf{{uwsp_b34r1n6_7h3_l04d}}")</code></pre></div>
</section>'''
    },
    {
        "id": "reverse-200-3",
        "title": "The Glass Bead Game",
        "category": "Reverse Engineering",
        "color": "blue",
        "points": 200,
        "flag": "poctf{uwsp_7h3_6l455_b34d_64m3}",
        "description": "Multi-layer encoding with base64 and ROT13.",
        "content": '''
<section class="mb-12">
    <h2 class="text-2xl font-bold text-white mb-4">Solution</h2>
    <p class="text-slate-300 mb-4">The binary uses base64 encoding followed by ROT13. Reversing both reveals the flag.</p>
    <div class="code-block"><pre><code>$ echo "encoded" | base64 -d | tr 'A-Za-z' 'N-ZA-Mn-za-m'
poctf{{uwsp_7h3_6l455_b34d_64m3}}</code></pre></div>
</section>'''
    }
]

for challenge in challenges:
    filename = f"{challenge['id']}.html"
    content = template.format(**challenge)
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

print("\nAll writeups created successfully\!")
