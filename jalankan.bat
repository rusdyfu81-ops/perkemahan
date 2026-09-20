@echo off
title Lorong Waktu - 42 Perkemahan (jangan ditutup selama acara)
cd /d "%~dp0"
echo.
echo  LORONG WAKTU - server game
echo  Buka di Chrome: http://localhost:8765/
echo  Jendela ini JANGAN ditutup selama game dipakai.
echo.
start "" chrome "http://localhost:8765/"
python -m http.server 8765 --bind 127.0.0.1
echo.
echo  Server berhenti. Kalau ada error "address already in use", port 8765 sedang dipakai program lain.
pause
