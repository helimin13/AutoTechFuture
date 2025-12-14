@echo off
echo ========================================
echo    AutoTech Future - Complete Setup
echo ========================================
echo.

REM Check Python installation
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python found: OK

REM Create project structure
echo Creating project structure...
mkdir static\css 2>nul
mkdir static\js 2>nul
mkdir static\images 2>nul
mkdir static\uploads 2>nul
mkdir templates 2>nul
mkdir data 2>nul

echo Project structure created: OK

REM Create virtual environment
echo Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    echo Virtual environment created: OK
) else (
    echo Virtual environment already exists: OK
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt

if errorlevel 1 (
    echo WARNING: Some dependencies failed to install.
    echo You may need to install them manually.
) else (
    echo Dependencies installed: OK
)

REM Initialize database
echo Initializing database...
python setup.py

if errorlevel 1 (
    echo ERROR: Database setup failed.
    pause
    exit /b 1
)

REM Create default images directory
echo Creating default images...
mkdir static\images 2>nul
echo Default images directory created: OK

echo.
echo ========================================
echo    SETUP COMPLETE!
echo ========================================
echo.
echo To start the application:
echo 1. Double-click 'run.bat'
echo 2. Or run manually:
echo    - Open Command Prompt
echo    - Navigate to this folder
echo    - Run: venv\Scripts\activate.bat
echo    - Run: python app.py
echo.
echo Access at: http://localhost:5000
echo Admin login: admin / admin123
echo.
pause