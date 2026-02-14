@echo off
REM ========================================
REM Brain Tumor Detector - Launcher
REM ========================================

title Brain Tumor Detector

echo.
echo ====================================
echo  Brain Tumor Detector - Launcher
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Python n'est pas installe ou n'est pas dans le PATH
    echo.
    echo Veuillez installer Python depuis https://www.python.org
    echo N'oubliez pas de cocher "Add Python to PATH"
    echo.
    pause
    exit /b 1
)

echo [OK] Python detecte
echo.

REM Check if the model file exists
if not exist "best_brain_tumor_model.keras" (
    echo [ERREUR] Le fichier modele "best_brain_tumor_model.keras" est introuvable
    echo.
    echo Assurez-vous que le fichier est dans le meme dossier que ce script.
    echo.
    pause
    exit /b 1
)

echo [OK] Fichier modele trouve
echo.

REM Check if the main script exists
if not exist "brain_tumor_detector_app.py" (
    echo [ERREUR] Le fichier "brain_tumor_detector_app.py" est introuvable
    echo.
    pause
    exit /b 1
)

echo [OK] Script principal trouve
echo.

REM Check dependencies
echo Verification des dependances...
echo.

python -c "import tensorflow" >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] TensorFlow n'est pas installe
    echo Installation en cours... (cela peut prendre quelques minutes)
    echo.
    pip install tensorflow
)

python -c "import cv2" >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] OpenCV n'est pas installe
    echo Installation en cours...
    echo.
    pip install opencv-python
)

python -c "import PIL" >nul 2>&1
if errorlevel 1 (
    echo [ATTENTION] Pillow n'est pas installe
    echo Installation en cours...
    echo.
    pip install pillow
)

echo.
echo [OK] Toutes les dependances sont installees
echo.
echo Lancement de l'application...
echo.

REM Launch the application
pythonw brain_tumor_detector_app.py

if errorlevel 1 (
    echo.
    echo [ERREUR] L'application a rencontre une erreur
    echo Relancement avec la console pour voir les details...
    echo.
    pause
    python brain_tumor_detector_app.py
    pause
)

exit /b 0
