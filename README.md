# 🎙️ VoiceForge — Text to Speech Studio

> Convert text, PDFs, and `.txt` files into natural-sounding speech in 29+ languages. Listen in the browser or download as MP3.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.0-000000?style=flat-square&logo=flask&logoColor=white)
![gTTS](https://img.shields.io/badge/gTTS-2.5.1-4285F4?style=flat-square&logo=google&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-Ready-000000?style=flat-square&logo=vercel&logoColor=white)

---

## ✨ Features

- 🗣️ **Live Playback** — Browser-native speech via Web Speech API (no server needed)
- 💾 **MP3 Download** — High-quality audio export powered by Google TTS
- 📄 **PDF & TXT Import** — Extract text from files instantly, in-browser
- 🌐 **29+ Languages** — Indian, European, Asian & Middle-Eastern languages
- 🎭 **12 Voice Styles** — Natural, Calm, Robot, Whisper, Dramatic & more
- ⚡ **Fine-Tune Controls** — Adjust Speed, Pitch, and Volume with sliders
- 📊 **Live Progress** — Sentence-by-sentence tracking with word highlighting
- ☁️ **Vercel Ready** — One-command serverless deployment

---

## 🚀 Quick Start

**Windows — One Click**
```
Double-click START.bat
```

**Manual Setup**
```bash
git clone https://github.com/your-username/voiceforge.git
cd voiceforge
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.

---

## 🏗️ Project Structure

```
VoiceForge/
├── app.py              # Flask backend + gTTS MP3 route
├── templates/
│   └── index.html      # Full frontend (UI, Speech API, PDF.js)
├── requirements.txt    # Flask + gTTS
├── START.bat           # One-click Windows launcher
├── vercel.json         # Vercel deployment config
└── api/
    └── index.py        # Vercel entry point
```

---

## ☁️ Deploy to Vercel

```bash
npm install -g vercel
vercel
```

All routes are handled by `api/index.py` on Python 3.12 — no extra config needed.

---

## 🌐 Languages Supported

**Indian:** Telugu · Hindi · Marathi · Tamil · Gujarati · Kannada · Malayalam · Bengali · Punjabi · Odia · Urdu · Nepali

**English:** India · US · UK · Australia

**International:** Spanish · French · German · Italian · Portuguese · Russian · Japanese · Chinese · Korean · Arabic · Turkish · Dutch · Polish · Swedish · Thai · Vietnamese · Indonesian

---

## 🛠️ Tech Stack

| | Technology |
|---|---|
| Backend | Python + Flask |
| Server TTS | gTTS (Google Text-to-Speech) |
| Browser TTS | Web Speech API |
| PDF Parsing | PDF.js |
| Deployment | Vercel |

---

## 📄 License

MIT — free to use and modify.

---

<div align="center">
  <b>🎙️ VoiceForge — Because every word deserves to be heard</b><br/>
  ⭐ Star this repo if you found it useful!
</div>
