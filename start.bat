@echo off
echo Starting BRAVED BALAJIS application...

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python.
    pause
    exit /b 1
)

REM Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo Node.js is not installed or not in PATH. Please install Node.js.
    pause
    exit /b 1
)

REM Start FastAPI backend server
start cmd /k "echo Starting Backend Server... && cd /d %~dp0 && python -m uvicorn src.api.main:app --reload --port 8000"

REM Wait a moment for the backend to start
timeout /t 3 /nobreak

REM Start Vite frontend dev server
start cmd /k "echo Starting Frontend Server... && cd /d %~dp0\bravedbalajis-2c58cadb && npm install && npm run dev"

echo.
echo Servers are starting in separate windows.
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Press any key to close this window...
pause >nul 