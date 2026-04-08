@echo off
title VoiceForge TTS Studio
color 0A
echo.
echo  ==========================================
echo    VoiceForge TTS Studio - Starting...
echo  ==========================================
echo.
echo  Installing required packages...
pip install flask gtts --quiet
echo.
echo  ==========================================
echo   Opening at http://localhost:5000
echo   Press CTRL+C to stop the server
echo  ==========================================
echo.
start http://localhost:5000
python app.py
pause
