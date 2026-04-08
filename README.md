<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=4f6ef7&height=200&section=header&text=VoiceForge&fontSize=70&fontColor=ffffff&fontAlignY=38&desc=Text%20to%20Speech%20Studio&descAlignY=58&descColor=c7d2fe" width="100%"/>

<br/>

<p>
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-3.0.0-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google_TTS-gTTS_2.5.1-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/Vercel-Deployed-000000?style=for-the-badge&logo=vercel&logoColor=white"/>
</p>

<p>
  <img src="https://img.shields.io/badge/29%2B%20Languages-Supported-4f6ef7?style=flat-square"/>
  <img src="https://img.shields.io/badge/12%20Voice%20Styles-Available-8b5cf6?style=flat-square"/>
  <img src="https://img.shields.io/badge/MP3%20Export-Enabled-22c55e?style=flat-square"/>
  <img src="https://img.shields.io/badge/PDF%20Import-Enabled-f97316?style=flat-square"/>
  <img src="https://img.shields.io/badge/License-MIT-22c55e?style=flat-square"/>
</p>

<br/>

### 🎙️ *Convert text, PDFs, and files into natural-sounding speech — in any language, any style.*

<br/>

### 🚀 [**Try it Live → voiceforge-studio-liart.vercel.app**](https://voiceforge-studio-liart.vercel.app/)

[![Live Demo](https://img.shields.io/badge/🎙️%20LIVE%20DEMO-Click%20to%20Try%20Now!-4f6ef7?style=for-the-badge&labelColor=1a1d2e)](https://voiceforge-studio-liart.vercel.app/)

<br/>

</div>

---

## 🌟 What is VoiceForge?

**VoiceForge** is a full-stack, browser-based **Text-to-Speech Studio** built with Flask and the Web Speech API. Type or paste text, upload a PDF or `.txt` file, choose your language, pick a voice style, fine-tune the settings — and either **listen live** or **download an MP3**.

No complicated setup. No cloud account needed for live playback. Just run and speak.

---

## ✨ Features at a Glance

<div align="center">

| 🗣️ Live Playback | 💾 MP3 Download | 📄 File Import |
|:---:|:---:|:---:|
| Native Web Speech API | Google TTS via gTTS | PDF & `.txt` support |

| 🌐 29+ Languages | 🎭 12 Voice Styles | ⚡ Fine-Tune Controls |
|:---:|:---:|:---:|
| Indian, EU, Asian & more | Natural to Dramatic | Speed · Pitch · Volume |

| 📊 Live Progress | 🌊 Waveform Viz | ☁️ Vercel Ready |
|:---:|:---:|:---:|
| Sentence-by-sentence | Animated header bars | One-command deploy |

</div>

---

## 🖼️ App Preview

```
┌──────────────────────────────────────────────────────────┐
│  🎙️ VoiceForge   Text to Speech Studio   ≋≋≋ ● Speaking │
├──────────────────────────────────────────────────────────┤
│  📝 Enter Your Text                                      │
│  [📄 Upload PDF] [📝 Upload .txt] [✨ Sample] [✕ Clear]  │
│  ┌────────────────────────────────────────────────────┐  │
│  │  Type, paste, or upload your content here...       │  │
│  └────────────────────────────────────────────────────┘  │
│  1,234 chars · 210 words                   ~2 min read   │
├──────────────────────────────────────────────────────────┤
│  🌐 Language & Voice                                     │
│  [🇮🇳 English (India) ▾]  [♀ Female] [♂ Male]           │
├──────────────────────────────────────────────────────────┤
│  🎭 Voice Style                                          │
│  [😊 Natural ✓] [🧘 Calm] [💼 Confident] [🎉 Excited]   │
│  [📺 News]      [📖 Story] [🎓 Academic] [🤖 Robot]     │
├──────────────────────────────────────────────────────────┤
│  🎚️ Fine Tune   Speed 1.0×  Pitch 1.0  Volume 1.0       │
├──────────────────────────────────────────────────────────┤
│  ▶ Play  ⏸ Pause  ▶ Resume  ⏹ Stop                      │
│  ████████████████░░░░  72%  Sentence 8 of 11 🔊          │
│  ──────────────────────────────────────────              │
│  💾 [⬇ Download MP3 — Normal]  [⬇ Download MP3 — Slow]  │
└──────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### ⚡ Windows — One Click
```batch
Double-click  START.bat
```
> Auto-installs dependencies, opens the browser, starts the server. Done.

### 🛠️ Manual Setup
```bash
# 1. Clone the repo
git clone https://github.com/your-username/voiceforge.git
cd voiceforge

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python app.py
```
Then open → **http://localhost:5000**

> 💡 **Tip:** Chrome or Edge gives the best voice support for live playback.

---

## 🏗️ Project Structure

```
VoiceForge/
│
├── 🐍 app.py                 ← Flask server · gTTS MP3 route · 3 API endpoints
│
├── 🌐 templates/
│   └── index.html            ← Entire frontend (UI + Speech API + PDF.js)
│
├── 📦 requirements.txt       ← flask==3.0.0 · gtts==2.5.1
│
├── 🚀 START.bat              ← One-click Windows launcher
│
├── ☁️  vercel.json            ← Serverless deployment config (Python 3.12)
│
└── 🔗 api/
    └── index.py              ← Vercel entry point → from app import app
```

---

## ⚙️ How It Works

```
                    ┌─────────────────────────────┐
                    │         User's Browser       │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────┼────────────────────┐
              │                    │                    │
              ▼                    ▼                    ▼
      [ Type / Paste ]    [ Upload PDF ]      [ Upload .txt ]
              │                    │                    │
              │            PDF.js extracts        FileReader
              │            text client-side       reads file
              └──────────────────► ◄───────────────────┘
                                   │
                            Text in Textarea
                                   │
                    ┌──────────────┴──────────────┐
                    │                             │
             [ ▶ Play Live ]           [ ⬇ Download MP3 ]
                    │                             │
           Web Speech API                POST /download-mp3
          (browser-native,              Flask → gTTS → Google
           no server call)              → MP3 bytes → download
```

---

## 🌐 Languages Supported

<details>
<summary><b>🇮🇳 Indian Languages (12)</b></summary>

| Language | Code | Language | Code |
|---|---|---|---|
| Telugu | `te-IN` | Kannada | `kn-IN` |
| Hindi | `hi-IN` | Malayalam | `ml-IN` |
| Marathi | `mr-IN` | Bengali | `bn-IN` |
| Tamil | `ta-IN` | Punjabi | `pa-IN` |
| Gujarati | `gu-IN` | Odia | `or-IN` |
| Urdu | `ur-PK` | Nepali | `ne-NP` |

</details>

<details>
<summary><b>🇬🇧 English Variants (4)</b></summary>

`en-IN` India &nbsp;·&nbsp; `en-US` United States &nbsp;·&nbsp; `en-GB` United Kingdom &nbsp;·&nbsp; `en-AU` Australia

</details>

<details>
<summary><b>🌍 International Languages (13+)</b></summary>

`es-ES` Spanish &nbsp;·&nbsp; `fr-FR` French &nbsp;·&nbsp; `de-DE` German &nbsp;·&nbsp; `it-IT` Italian &nbsp;·&nbsp; `pt-BR` Portuguese &nbsp;·&nbsp; `ru-RU` Russian &nbsp;·&nbsp; `ja-JP` Japanese &nbsp;·&nbsp; `zh-CN` Chinese &nbsp;·&nbsp; `ko-KR` Korean &nbsp;·&nbsp; `ar-SA` Arabic &nbsp;·&nbsp; `tr-TR` Turkish &nbsp;·&nbsp; `nl-NL` Dutch &nbsp;·&nbsp; `sv-SE` Swedish &nbsp;·&nbsp; `th-TH` Thai &nbsp;·&nbsp; `vi-VN` Vietnamese &nbsp;·&nbsp; `id-ID` Indonesian

</details>

---

## 🎭 Voice Styles

| Style | Mood | Speed | Pitch |
|:---:|---|:---:|:---:|
| 😊 Natural | Clear, friendly everyday voice | 1.00× | 1.00 |
| 🧘 Calm | Slow, relaxed, peaceful | 0.82× | 0.88 |
| 💼 Confident | Authoritative, professional | 1.05× | 1.00 |
| 🎉 Excited | Energetic, enthusiastic | 1.35× | 1.30 |
| 📺 News Anchor | Crisp, neutral, broadcast-ready | 1.10× | 1.00 |
| 📖 Storyteller | Warm, expressive, engaging | 0.95× | 1.08 |
| 🎓 Academic | Measured, precise, clear | 0.95× | 1.00 |
| 😄 Friendly | Warm, cheerful, upbeat | 1.10× | 1.20 |
| 🎯 Serious | Deep, formal, authoritative | 0.90× | 0.85 |
| 🤖 Robot | Flat, monotone, mechanical | 0.88× | 0.52 |
| 🤫 Whisper | Soft, hushed, quiet | 0.78× | 0.75 |
| 🎭 Dramatic | Theatrical, bold, expressive | 0.88× | 1.28 |

---

## 📡 API Reference

<details>
<summary><b>POST /download-mp3</b></summary>

Generates and streams an MP3 using Google TTS.

**Request Body:**
```json
{
  "text": "Hello, this is VoiceForge!",
  "lang": "en-IN",
  "slow": false
}
```

**Response:** Binary MP3 stream → auto-downloaded as `voiceforge_speech.mp3`

</details>

<details>
<summary><b>GET /check-gtts</b></summary>

Health check — returns whether gTTS is available on the server.

```json
{ "available": true }
```

</details>

---

## ☁️ Deploy to Vercel

```bash
npm install -g vercel
vercel
```

The included `vercel.json` routes all traffic through `api/index.py` on **Python 3.12**. Zero additional config needed.

> ⚠️ gTTS requires outbound HTTP to Google's servers — ensure your Vercel plan allows it.

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|---|---|
| 🐍 Backend | Python + Flask 3.0 |
| 🔊 Server TTS | gTTS 2.5.1 (Google Text-to-Speech) |
| 🗣️ Browser TTS | Web Speech API (SpeechSynthesis) |
| 📄 PDF Parsing | PDF.js 3.11.174 (client-side) |
| 🎨 Frontend | Vanilla HTML · CSS · JavaScript |
| ☁️ Deployment | Vercel Serverless |

</div>

---

## 📄 License

```
MIT License — Free to use, modify, and distribute.
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=4f6ef7&height=120&section=footer" width="100%"/>

**Made with ❤️ using Flask · gTTS · Web Speech API**

⭐ **Star this repo if VoiceForge helped you!** ⭐

[![Live Demo](https://img.shields.io/badge/🎙️%20Try%20VoiceForge%20Live-voiceforge--studio--liart.vercel.app-4f6ef7?style=for-the-badge&labelColor=1a1d2e)](https://voiceforge-studio-liart.vercel.app/)

`🎙️ VoiceForge — Because every word deserves to be heard`

</div>
