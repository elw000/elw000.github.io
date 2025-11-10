# PointerOverflow CTF 2025 - Writeups Summary

## Overview
Complete writeups for 12 solved challenges from PointerOverflow CTF 2025.

**Total Points:** 1400  
**Categories:** Reverse Engineering (8), Binary Exploitation (4)

---

## Reverse Engineering (800 points)

### 100-point challenges
1. **Seven Easy Pieces** - Basic strings analysis
   - Flag: `poctf{uwsp_s3v3n_345y_p13c35}`
   - File: `writeups/reverse-100-1.html`

2. **Left at the Light** - String manipulation
   - Flag: `poctf{uwsp_l3f7_47_7h3_l16h7}`
   - File: `writeups/reverse-100-2.html`

3. **A Tree of Knives** - XOR encoding
   - Flag: `poctf{uwsp_4_7r33_0f_kn1v35}`
   - File: `writeups/reverse-100-3.html`

4. **Gremlins in the Gears** - Character transformation
   - Flag: `poctf{uwsp_6r3ml1n5_1n_7h3_6347s}`
   - File: `writeups/reverse-100-4.html`

### 200-point challenges
5. **Bearing the Load** - Dynamic analysis with ltrace
   - Flag: `poctf{uwsp_b34r1n6_7h3_l04d}`
   - File: `writeups/reverse-200-2.html`

6. **The Glass Bead Game** - Base64 + ROT13
   - Flag: `poctf{uwsp_7h3_6l455_b34d_64m3}`
   - File: `writeups/reverse-200-3.html`

### 300-point challenges
7. **Through a Glass Darkly** - WebAssembly reverse engineering
   - Flag: `poctf{uwsp_7hr0u6h_4_6l455_d4rkly}`
   - File: `writeups/reverse-300-1.html`
   - **Detailed writeup with full WASM analysis**

8. **Make the Pieces Sing** - MIDI file analysis
   - Flag: `poctf{uwsp_m4k3_7h3_p13c35_51n6}`
   - File: `writeups/reverse-300-2.html`
   - **Detailed writeup with MIDI format explanation**

---

## Binary Exploitation (600 points)

### 100-point challenges
9. **Mason, Meridian** - Heartbleed-style information disclosure
   - Flag: `poctf{uwsp_m450n_m3r1d14n}`
   - File: `writeups/exploit-100-2.html`
   - **Detailed writeup with CVE-2014-0160 explanation**

10. **The Floor is Lava** - Stack buffer overflow
    - Flag: `poctf{uwsp_17_w45n7_3v3n_w0r7h_17}`
    - File: `writeups/exploit-100-4.html`

### 200-point challenges
11. **Count the Cost** - Integer overflow to buffer overflow
    - Flag: `poctf{uwsp_c0un7_7h3_c057}`
    - File: `writeups/exploit-200-2.html`
    - **Detailed writeup with type confusion analysis**

### 300-point challenges
12. **Choir Invisible** - Kernel UAF exploitation
    - Flag: `poctf{uwsp_ch01r_1nv151bl3}`
    - File: `writeups/exploit-300-1.html`

---

## Writeup Quality

### Detailed Writeups (5)
These include step-by-step analysis, code walkthroughs, and exploitation details:
- reverse-100-1.html (Seven Easy Pieces)
- reverse-300-1.html (Through a Glass Darkly - WASM)
- reverse-300-2.html (Make the Pieces Sing - MIDI)
- exploit-100-2.html (Mason, Meridian - Heartbleed)
- exploit-200-2.html (Count the Cost - Integer Overflow)

### Standard Writeups (7)
These include solution approach and flag:
- reverse-100-2, 100-3, 100-4
- reverse-200-2, 200-3
- exploit-100-4
- exploit-300-1

---

## Files Structure

```
ctf-site/
├── ctf-new.html              # Main CTF page with sidebar
├── index.html                # CV page with CTF link
└── writeups/
    ├── index.html            # Writeups index page
    ├── index.json            # Metadata for all writeups
    ├── README.md             # Summary document
    ├── reverse-100-1.html    # Detailed
    ├── reverse-100-2.html
    ├── reverse-100-3.html
    ├── reverse-100-4.html
    ├── reverse-200-2.html
    ├── reverse-200-3.html
    ├── reverse-300-1.html    # Detailed (WASM)
    ├── reverse-300-2.html    # Detailed (MIDI)
    ├── exploit-100-2.html    # Detailed (Heartbleed)
    ├── exploit-100-4.html
    ├── exploit-200-2.html    # Detailed (Integer Overflow)
    └── exploit-300-1.html
```

---

## Features

- Dark theme matching the main site
- Responsive design with Tailwind CSS
- Code syntax highlighting
- Step-by-step solutions
- Back navigation to main CTF page
- Consistent styling across all writeups

---

## Ready for Deployment

All files are ready to be pushed to GitHub Pages:
```bash
cd /home/elw00/ctf-site
git add .
git commit -m "Add complete CTF writeups for 12 challenges"
git push origin main
```

The site will be live at: https://elw000.github.io/ctf-new.html
