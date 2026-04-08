<div align="center">

```
██╗   ██╗ ██████╗ ██╗ ██████╗███████╗███████╗ ██████╗ ██████╗  ██████╗ ███████╗
██║   ██║██╔═══██╗██║██╔════╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝ ██╔════╝
██║   ██║██║   ██║██║██║     █████╗  █████╗  ██║   ██║██████╔╝██║  ███╗█████╗  
╚██╗ ██╔╝██║   ██║██║██║     ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║   ██║██╔══╝  
 ╚████╔╝ ╚██████╔╝██║╚██████╗███████╗██║     ╚██████╔╝██║  ██║╚██████╔╝███████╗
  ╚═══╝   ╚═════╝ ╚═╝ ╚═════╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
```

<h3>🎙️ Text-to-Speech Studio — Speak Any Language, Your Way</h3>

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/gTTS-2.5.1-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vercel-Ready-000000?style=for-the-badge&logo=vercel&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge"/>
</p>

<p>
  <img src="https://img.shields.io/badge/Languages_Supported-29+-4f6ef7?style=flat-square"/>
  <img src="https://img.shields.io/badge/Voice_Styles-12-8b5cf6?style=flat-square"/>
  <img src="https://img.shields.io/badge/PDF_Support-✅-22c55e?style=flat-square"/>
  <img src="https://img.shields.io/badge/MP3_Export-✅-22c55e?style=flat-square"/>
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Web-f97316?style=flat-square"/>
</p>

<br/>

> **VoiceForge** is a full-stack, browser-based Text-to-Speech studio with a polished UI.  
> Convert typed text, `.txt` files, or PDFs into natural-sounding speech in 29+ languages — and download it as an MP3.

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🖼️ UI Overview](#️-ui-overview)
- [🏗️ Project Structure](#️-project-structure)
- [⚙️ How It Works](#️-how-it-works)
- [🌐 Language Support](#-language-support)
- [🎭 Voice Styles](#-voice-styles)
- [🚀 Quick Start (Local)](#-quick-start-local)
- [☁️ Deploy to Vercel](#️-deploy-to-vercel)
- [🛠️ Tech Stack](#️-tech-stack)
- [📡 API Reference](#-api-reference)
- [🗂️ File Reference](#️-file-reference)
- [🔮 Roadmap](#-roadmap)
- [📄 License](#-license)

---

## ✨ Features

| Feature | Description |
|---|---|
| 🗣️ **Browser TTS** | Uses the native **Web Speech API** — zero server calls for live playback |
| 💾 **MP3 Download** | Server-side **Google TTS (gTTS)** renders a real MP3 file to download |
| 📄 **PDF Import** | Upload any PDF; text is extracted page-by-page via **PDF.js** |
| 📝 **TXT Import** | Drag-and-drop or upload `.txt` files directly |
| 🌐 **29+ Languages** | Indian, European, Asian & Middle-Eastern languages all supported |
| 🎭 **12 Voice Styles** | Natural, Calm, Robot, Whisper, Dramatic, News Anchor & more |
| 👤 **Gender Filter** | Filter available system voices by Male / Female |
| ⚡ **Fine-Tune Controls** | Live sliders for **Speed**, **Pitch**, and **Volume** |
| 📊 **Progress Tracker** | Real-time sentence-by-sentence reading progress bar |
| ✍️ **Word Highlighter** | Currently-spoken sentence is highlighted live |
| 🔔 **Toast Notifications** | Colour-coded toasts for success, warning, error & info states |
| 🌊 **Animated Waveform** | An 8-bar animated waveform shows live speaking state in the header |
| 📱 **Responsive Design** | Fully mobile-friendly with CSS Grid breakpoints |
| ☁️ **Vercel Ready** | Deploy serverless to Vercel with zero config — `vercel.json` included |

---

## 🖼️ UI Overview

```
┌──────────────────────────────────────────────────────────┐
│  🎙️ VoiceForge   Text to Speech Studio   ≋≋≋ ● Speaking │
├──────────────────────────────────────────────────────────┤
│  📝 CARD 1 — Enter Your Text                             │
│  [ Upload PDF ] [ Upload .txt ] [✨ Sample] [✕ Clear]    │
│  ┌────────────────────────────────────────────────────┐  │
│  │  Your text here...                                  │  │
│  └────────────────────────────────────────────────────┘  │
│  1,234 characters · 210 words              ~2 min read   │
├──────────────────────────────────────────────────────────┤
│  🌐 CARD 2 — Language & Voice                            │
│  Language: [🇮🇳 English (India) ▾]                        │
│  Gender:   [♀ Female] [♂ Male]                           │
│  Voice:    [Microsoft Heera ▾]                           │
├──────────────────────────────────────────────────────────┤
│  🎭 CARD 3 — Voice Style                                 │
│  [😊 Natural] [🧘 Calm] [💼 Confident] [🎉 Excited]     │
│  [📺 News]    [📖 Story] [🎓 Academic] [😄 Friendly]    │
│  [🎯 Serious] [🤖 Robot] [🤫 Whisper] [🎭 Dramatic]    │
├──────────────────────────────────────────────────────────┤
│  🎚️ CARD 4 — Fine Tune                                   │
│  ⚡ Speed [━━●━━━━] 1.0×                                 │
│  🎵 Pitch [━━━●━━━] 1.0                                  │
│  🔊 Volume[━━━━━●━] 1.0                                  │
├──────────────────────────────────────────────────────────┤
│  ▶️  CARD 5 — Playback                                   │
│  ██████████████░░░░ 72%  Sentence 8 of 11               │
│  [▶ Play] [⏸ Pause] [▶ Resume] [⏹ Stop]                 │
│  🔊 Speaking...                                          │
│  Currently reading: "...highlighted sentence..."         │
│  ────────────────────────────────                        │
│  💾 Download as MP3                                      │
│  [⬇ Normal Speed] [⬇ Slow Speed]                        │
└──────────────────────────────────────────────────────────┘
```

---

## 🏗️ Project Structure

```
VoiceForge/
│
├── 📄 app.py               # Flask backend — routes & gTTS MP3 logic
├── 🌐 templates/
│   └── index.html          # Full frontend — UI, Web Speech API, PDF.js
│
├── 📦 requirements.txt     # Python dependencies (Flask + gTTS)
│
├── 🚀 START.bat            # One-click Windows launcher
│
├── ☁️ vercel.json           # Vercel serverless deployment config
└── 🔗 api/
    └── index.py            # Vercel entry point (imports app from app.py)
```

---

## ⚙️ How It Works

### 🔈 Live Playback (Browser-Side)
```
User types text
      ↓
Text split into sentences
      ↓
Web Speech API (SpeechSynthesisUtterance)
      ↓
Voice Style presets apply Rate / Pitch settings
      ↓
Real-time progress tracking + sentence highlighting
```

The browser's built-in **Web Speech API** handles all live audio — no server round-trip needed. Sentences are split by punctuation, spoken one-by-one, and tracked for the progress bar and word highlighter.

### 💾 MP3 Download (Server-Side)
```
User clicks "Download MP3"
      ↓
POST /download-mp3  {text, lang, slow}
      ↓
Flask → gTTS(text, lang=lang_code, slow=slow)
      ↓
Audio written to BytesIO buffer
      ↓
send_file() → browser triggers download
```

Google Text-to-Speech (`gTTS`) is used on the server. The language code is extracted (e.g. `en-IN` → `en`) and passed to gTTS, which returns high-quality MP3 bytes streamed directly to the client.

### 📄 PDF Extraction (Client-Side)
```
User uploads PDF
      ↓
PDF.js (CDN) parses ArrayBuffer
      ↓
getTextContent() called per page
      ↓
All text joined and dropped into textarea
```

No server upload required — PDF parsing happens entirely in-browser using **PDF.js v3.11.174**.

---

## 🌐 Language Support

### 🇮🇳 Indian Languages (12)
| Language | Code | Language | Code |
|---|---|---|---|
| Telugu | `te-IN` | Gujarati | `gu-IN` |
| Hindi | `hi-IN` | Kannada | `kn-IN` |
| Marathi | `mr-IN` | Malayalam | `ml-IN` |
| Tamil | `ta-IN` | Bengali | `bn-IN` |
| Punjabi | `pa-IN` | Odia | `or-IN` |
| Urdu | `ur-PK` | Nepali | `ne-NP` |

### 🌍 English Variants (4)
`en-IN` · `en-US` · `en-GB` · `en-AU`

### 🌐 International Languages (13)
`es-ES` · `fr-FR` · `de-DE` · `it-IT` · `pt-BR` · `ru-RU` · `ja-JP` · `zh-CN` · `ko-KR` · `ar-SA` · `tr-TR` · `nl-NL` · `pl-PL` · `sv-SE` · `th-TH` · `vi-VN` · `id-ID`

> **Note:** Live browser playback depends on voices installed on the OS. MP3 download uses Google TTS and works for all supported languages.

---

## 🎭 Voice Styles

Each style preset adjusts the **Rate** and **Pitch** of the speech engine:

| Style | Emoji | Rate | Pitch | Best For |
|---|:---:|:---:|:---:|---|
| Natural | 😊 | 1.00× | 1.00 | General use |
| Calm | 🧘 | 0.82× | 0.88 | Meditation, ASMR |
| Confident | 💼 | 1.05× | 1.00 | Presentations |
| Excited | 🎉 | 1.35× | 1.30 | Promos, ads |
| News Anchor | 📺 | 1.10× | 1.00 | News reading |
| Storyteller | 📖 | 0.95× | 1.08 | Audiobooks |
| Academic | 🎓 | 0.95× | 1.00 | Lectures |
| Friendly | 😄 | 1.10× | 1.20 | Tutorials |
| Serious | 🎯 | 0.90× | 0.85 | Formal docs |
| Robot | 🤖 | 0.88× | 0.52 | Fun / effects |
| Whisper | 🤫 | 0.78× | 0.75 | Quiet narration |
| Dramatic | 🎭 | 0.88× | 1.28 | Theatre, films |

---

## 🚀 Quick Start (Local)

### Option A — One Click (Windows)
```
Double-click START.bat
```
This auto-installs dependencies and opens `http://localhost:5000` in your browser.

### Option B — Manual Setup

**1. Clone the repo**
```bash
git clone https://github.com/your-username/voiceforge.git
cd voiceforge
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the server**
```bash
python app.py
```

**4. Open in browser**
```
http://localhost:5000
```

### Requirements
- Python 3.8+
- pip
- A modern browser (Chrome / Edge recommended for best voice support)

---

## ☁️ Deploy to Vercel

VoiceForge is pre-configured for **Vercel serverless** deployment.

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel
```

The `vercel.json` routes all traffic through `api/index.py`, which imports the Flask `app` from `app.py`. Python 3.12 runtime is specified.

```json
{
  "version": 2,
  "functions": {
    "api/index.py": { "runtime": "python3.12" }
  },
  "routes": [
    { "src": "/(.*)", "dest": "/api/index.py" }
  ]
}
```

> ⚠️ **Note:** On Vercel, `gTTS` requires outbound HTTP access to Google's TTS servers. Ensure your Vercel plan supports this. Live browser playback works anywhere.

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python + Flask 3.0 | Web server, MP3 download route |
| **TTS Engine (Server)** | gTTS 2.5.1 | Google Text-to-Speech MP3 generation |
| **TTS Engine (Browser)** | Web Speech API | Live in-browser playback |
| **PDF Parsing** | PDF.js 3.11.174 | Client-side PDF text extraction |
| **Frontend** | Vanilla HTML/CSS/JS | Full UI with no framework |
| **Fonts** | Plus Jakarta Sans | Google Fonts — clean, modern typeface |
| **Deployment** | Vercel | Serverless cloud hosting |

---

## 📡 API Reference

### `GET /`
Renders the main application page. Passes `gtts_available` boolean to the template to conditionally show/hide MP3 download UI.

---

### `POST /download-mp3`
Generates and streams an MP3 file using Google TTS.

**Request Body (JSON):**
```json
{
  "text": "Hello, this is VoiceForge!",
  "lang": "en-IN",
  "slow": false
}
```

| Field | Type | Description |
|---|---|---|
| `text` | `string` | The text to convert to speech |
| `lang` | `string` | BCP-47 language tag (e.g. `hi-IN`, `en-US`) |
| `slow` | `boolean` | `true` for slower speech speed |

**Response:** Binary MP3 stream (`audio/mpeg`) downloaded as `voiceforge_speech.mp3`

**Error Response:**
```json
{ "error": "No text provided" }
```

---

### `GET /check-gtts`
Health check to verify if gTTS is installed and available.

**Response:**
```json
{ "available": true }
```

---

## 🗂️ File Reference

| File | Role |
|---|---|
| `app.py` | Core Flask app: defines routes `/`, `/download-mp3`, `/check-gtts`. Handles gTTS import gracefully with `try/except`. |
| `templates/index.html` | Entire frontend in a single file: HTML structure, CSS (1000+ lines), and JavaScript (300+ lines). Manages voice loading, style presets, slider fine-tuning, PDF.js integration, Web Speech API playback, progress tracking, toast system, and MP3 download fetch. |
| `requirements.txt` | Pins `flask==3.0.0` and `gtts==2.5.1` for reproducible installs. |
| `START.bat` | Windows batch script: installs deps silently, opens browser, runs `app.py`. |
| `vercel.json` | Vercel v2 config routing all requests to `api/index.py` on Python 3.12. |
| `api/index.py` | Vercel entry-point — a single line: `from app import app`. |

---

## 🔮 Roadmap

- [ ] 🎙️ **Voice Cloning** — custom voice upload support
- [ ] 📁 **Batch Processing** — convert multiple files at once
- [ ] 🔄 **SSML Support** — fine-grained speech markup
- [ ] 🕓 **Playback History** — recent conversions list
- [ ] 🌙 **Dark Mode** — full dark theme toggle
- [ ] 📲 **PWA** — installable Progressive Web App
- [ ] 🔐 **API Keys** — user-configurable Google TTS API key

---

## 📄 License

```
MIT License — Free to use, modify, and distribute.
Attribution appreciated but not required.
```

---

<div align="center">

**Made with ❤️ using Flask, gTTS & the Web Speech API**

⭐ If you found this useful, please give it a star!

`🎙️ VoiceForge — Because every word deserves to be heard`

</div>
