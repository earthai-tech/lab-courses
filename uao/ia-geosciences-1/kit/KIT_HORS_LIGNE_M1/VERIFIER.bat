@echo off
REM Verifie Python, les bibliotheques et les donnees (sans Internet).
cd /d "%~dp0"
for /d %%W in ("%~dp0WPy64-*") do if exist "%%W\scripts\env.bat" call "%%W\scripts\env.bat"
if exist "%USERPROFILE%\anaconda3\Scripts\activate.bat" call "%USERPROFILE%\anaconda3\Scripts\activate.bat"
if exist "%ProgramData%\anaconda3\Scripts\activate.bat" call "%ProgramData%\anaconda3\Scripts\activate.bat"
if exist "%USERPROFILE%\miniconda3\Scripts\activate.bat" call "%USERPROFILE%\miniconda3\Scripts\activate.bat"
python verifier_installation.py
