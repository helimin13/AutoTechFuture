@echo off
echo ========================================
echo    AutoTech Future - Starting Server
echo ========================================

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install requirements if needed
echo Checking dependencies...
pip install -r requirements.txt

REM Setup database
echo Setting up database...
python setup.py

REM Start the application
echo Starting Flask server...
echo.
echo Access the application at: http://localhost:5000
echo Admin login: admin / admin123
echo.
echo Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause