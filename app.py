from flask import Flask, render_template, request, jsonify, send_file
import io, os, tempfile

app = Flask(__name__)

# Try to import gTTS for MP3 download feature
try:
    from gtts import gTTS
    GTTS_AVAILABLE = True
except ImportError:
    GTTS_AVAILABLE = False

@app.route('/')
def index():
    return render_template('index.html', gtts_available=GTTS_AVAILABLE)

@app.route('/download-mp3', methods=['POST'])
def download_mp3():
    if not GTTS_AVAILABLE:
        return jsonify({'error': 'gTTS not installed. Run: pip install gtts'}), 500
    try:
        data   = request.get_json()
        text   = data.get('text', '').strip()
        lang   = data.get('lang', 'en')
        slow   = data.get('slow', False)
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        # gTTS uses 2-letter lang code
        lang_code = lang.split('-')[0]
        tts = gTTS(text=text, lang=lang_code, slow=slow)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        return send_file(
            buf,
            mimetype='audio/mpeg',
            as_attachment=True,
            download_name='voiceforge_speech.mp3'
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/check-gtts')
def check_gtts():
    return jsonify({'available': GTTS_AVAILABLE})

if __name__ == '__main__':
    print()
    print("╔══════════════════════════════════════════╗")
    print("║   🎙️  VoiceForge — TTS Studio v3         ║")
    print("╠══════════════════════════════════════════╣")
    print("║  Open browser → http://localhost:5000    ║")
    print("╠══════════════════════════════════════════╣")
    if GTTS_AVAILABLE:
        print("║  ✅ MP3 Download  → ENABLED              ║")
    else:
        print("║  ⚠️  MP3 Download → Run: pip install gtts║")
    print("╚══════════════════════════════════════════╝")
    print()
    app.run(debug=False, port=5000)
