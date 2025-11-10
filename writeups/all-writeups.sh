#\!/bin/bash

# Function to create writeup HTML
create_writeup() {
    local id=$1
    local title=$2
    local category=$3
    local points=$4
    local flag=$5
    local desc=$6
    local solution=$7
    
    cat > "${id}.html" << EOF
<\!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title} - Writeup</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/@phosphor-icons/web"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script>tailwind.config = { darkMode: 'class', theme: { extend: { fontFamily: { 'sans': ['Inter', 'sans-serif'], 'mono': ['JetBrains Mono', 'monospace'] }}}}</script>
</head>
<body class="bg-black text-slate-300 font-sans antialiased">
    <div class="max-w-4xl mx-auto px-6 py-12">
        <a href="../ctf-new.html" class="inline-flex items-center gap-2 text-blue-400 hover:text-blue-300 mb-8">
            <i class="ph-bold ph-arrow-left"></i> Back to CTF Writeups
        </a>
        <header class="mb-12">
            <div class="flex items-center gap-3 mb-4">
                <span class="px-3 py-1 bg-${category}-500/10 text-${category}-400 border border-${category}-500/30 rounded-lg text-sm font-semibold uppercase">${category}</span>
                <span class="text-2xl font-bold text-${category}-400">${points} points</span>
            </div>
            <h1 class="text-4xl font-bold text-white mb-4">${title}</h1>
            <div class="flex items-center gap-6 text-sm text-slate-400">
                <span class="flex items-center gap-2"><i class="ph-bold ph-calendar"></i> November 10, 2025</span>
                <span class="flex items-center gap-2"><i class="ph-bold ph-flag"></i> PointerOverflow CTF 2025</span>
            </div>
        </header>
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-4">Challenge Description</h2>
            <div class="bg-slate-900 border border-slate-800 rounded-lg p-6">
                <p class="text-slate-300 leading-relaxed">${desc}</p>
            </div>
        </section>
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-4">Solution</h2>
            <div class="prose prose-invert max-w-none">
                ${solution}
            </div>
        </section>
        <section class="mb-12">
            <h2 class="text-2xl font-bold text-white mb-4">Flag</h2>
            <div class="bg-gradient-to-r from-green-900/50 to-emerald-900/50 border border-green-500/30 rounded-lg p-6">
                <div class="flex items-center gap-3">
                    <i class="ph-bold ph-check-circle text-3xl text-green-400"></i>
                    <code class="text-xl font-mono text-green-400">${flag}</code>
                </div>
            </div>
        </section>
    </div>
</body>
</html>
EOF
}

# Create all writeups
create_writeup "reverse-100-2" "Left at the Light" "blue" "100" "poctf{uwsp_l3f7_47_7h3_l16h7}" \
    "A reverse engineering challenge involving basic binary analysis." \
    "<p class='text-slate-300 mb-4'>Similar to the first challenge, this binary contains the flag as a plaintext string. Using <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>strings</code> command reveals the flag immediately.</p>"

create_writeup "reverse-100-3" "A Tree of Knives" "blue" "100" "poctf{uwsp_4_7r33_0f_kn1v35}" \
    "Basic reverse engineering with simple obfuscation." \
    "<p class='text-slate-300 mb-4'>The binary uses basic XOR encoding. Running it through a decompiler like Ghidra shows the XOR key and the encoded flag. Simple Python script to XOR decode reveals the flag.</p>"

create_writeup "reverse-100-4" "Gremlins in the Gears" "blue" "100" "poctf{uwsp_6r3ml1n5_1n_7h3_6347s}" \
    "Reverse engineering challenge with character manipulation." \
    "<p class='text-slate-300 mb-4'>The binary performs character transformations on the flag. Static analysis with Ghidra reveals the transformation algorithm. Reversing the operations gives us the original flag.</p>"

create_writeup "reverse-200-2" "Bearing the Load" "blue" "200" "poctf{uwsp_b34r1n6_7h3_l04d}" \
    "Intermediate reverse engineering with dynamic analysis." \
    "<p class='text-slate-300 mb-4'>This challenge requires dynamic analysis. Using <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>ltrace</code> or <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>strace</code> reveals library calls that construct the flag at runtime.</p>"

create_writeup "reverse-200-3" "The Glass Bead Game" "blue" "200" "poctf{uwsp_7h3_6l455_b34d_64m3}" \
    "Advanced string manipulation and encoding." \
    "<p class='text-slate-300 mb-4'>The binary uses base64 encoding combined with ROT13. Identifying the encoding scheme through static analysis and reversing it reveals the flag.</p>"

create_writeup "reverse-300-1" "Through a Glass Darkly" "blue" "300" "poctf{uwsp_7hr0u6h_4_6l455_d4rkly}" \
    "WebAssembly reverse engineering with custom encryption." \
    "<p class='text-slate-300 mb-4'>This challenge involves WebAssembly (WASM). Converting to WAT format with <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>wasm2wat</code> reveals the verification logic. The flag is encrypted with a custom XOR-based cipher. Analyzing the WASM bytecode and reversing the encryption algorithm yields the flag.</p>"

create_writeup "reverse-300-2" "Make the Pieces Sing" "blue" "300" "poctf{uwsp_m4k3_7h3_p13c35_51n6}" \
    "MIDI file analysis and reverse engineering." \
    "<p class='text-slate-300 mb-4'>The challenge provides a MIDI fingerprint validator. Analyzing the validation logic reveals that specific note sequences encode the flag. Creating a MIDI file with the correct note patterns generates the flag.</p>"

create_writeup "exploit-100-2" "Mason, Meridian" "red" "100" "poctf{uwsp_m450n_m3r1d14n}" \
    "Heartbleed-style information disclosure vulnerability." \
    "<p class='text-slate-300 mb-4'>This challenge simulates the Heartbleed vulnerability. The program reads a length parameter and echoes that many bytes from a stack buffer. By requesting more bytes than the input buffer size (e.g., 224 bytes instead of 64), we can leak stack memory containing the flag which is stored at offset 96.</p><div class='bg-slate-900 border border-slate-800 rounded-lg p-4 my-4'><pre class='text-sm text-slate-300 font-mono'>payload = '224:A'\nio.sendline(payload)\nleaked = io.recv(224)\nflag = leaked[96:]  # Flag starts at offset 96</pre></div>"

create_writeup "exploit-200-2" "Count the Cost" "red" "200" "poctf{uwsp_c0un7_7h3_c057}" \
    "Integer overflow leading to buffer overflow." \
    "<p class='text-slate-300 mb-4'>The vulnerability is an integer overflow in the <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>set_note</code> function. A <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>uint16_t</code> is cast to <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>int8_t</code> for size checking, but the original value is used for <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>memcpy</code>. By sending len=552 (which becomes 40 when cast to int8_t), we bypass the check but copy 552 bytes, overwriting the <code class='bg-slate-800 px-2 py-1 rounded text-blue-400'>st.admin</code> field with the MAGIC value to get the flag.</p>"

echo "All writeups created\!"
