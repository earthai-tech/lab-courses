@echo off
REM Lance Jupyter Notebook dans ce dossier, sans connexion Internet.
REM Fonctionne avec Anaconda (installe) ou WinPython (portable, sur cle USB).
cd /d "%~dp0"

REM 1) WinPython portable place dans ce dossier (sous-dossier WPy64-*)
for /d %%W in ("%~dp0WPy64-*") do (
    if exist "%%W\scripts\env.bat" (
        call "%%W\scripts\env.bat"
        goto LANCER
    )
)

REM 2) Anaconda / Miniconda installe sur le poste
if exist "%USERPROFILE%\anaconda3\Scripts\activate.bat" call "%USERPROFILE%\anaconda3\Scripts\activate.bat"
if exist "%ProgramData%\anaconda3\Scripts\activate.bat" call "%ProgramData%\anaconda3\Scripts\activate.bat"
if exist "%USERPROFILE%\miniconda3\Scripts\activate.bat" call "%USERPROFILE%\miniconda3\Scripts\activate.bat"

:LANCER
where python >nul 2>nul || (
    echo Python introuvable. Installez Anaconda ou copiez WinPython dans ce dossier ^(voir LISEZMOI.txt^).
    pause
    exit /b 1
)
echo Ouverture de Jupyter dans le navigateur... (ne fermez pas cette fenetre)
python -m notebook --notebook-dir="%~dp0"
pause
