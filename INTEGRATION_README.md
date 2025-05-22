# BRAVED BALAJIS - Integrated Application

This document describes how to run the integrated application with both the backend and frontend components.

## Project Structure

- `bravedbalajis/` - Main repository (Backend)
  - `src/` - Backend source code
  - `bravedbalajis-2c58cadb/` - Frontend code (cloned from separate repo)

## Integration Details

The integration uses an API-driven approach:

1. The backend exposes FastAPI endpoints in `src/api/main.py`
2. The frontend calls these endpoints via an API service in `bravedbalajis-2c58cadb/src/lib/api.ts`
3. During development, API requests from the frontend are proxied to the backend

## Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- NPM or Yarn

## Running the Application

### Option 1: Using the Startup Script (Recommended)

Simply run the startup script to launch both servers:

```bash
# On Windows
start.bat

# On Linux/Mac
# chmod +x start.sh
# ./start.sh
```

### Option 2: Manual Startup

#### Backend (FastAPI)

```bash
# Navigate to the project root
cd bravedbalajis

# Install dependencies
pip install -r requirements.txt

# Start the server
python -m uvicorn src.api.main:app --reload --port 8000
```

#### Frontend (React/Vite)

```bash
# Navigate to the frontend directory
cd bravedbalajis/bravedbalajis-2c58cadb

# Install dependencies
npm install

# Start the development server
npm run dev
```

## Accessing the Application

- Backend API: http://localhost:8000
  - API documentation: http://localhost:8000/docs

- Frontend: http://localhost:5173

## API Endpoints

The backend exposes the following endpoints:

- `GET /` - API status check
- `GET /frameworks` - Lists available learning frameworks
- `GET /agents` - Lists available agents
- `POST /analyze` - Analyzes user data
- `POST /neuroscience` - Gets neuroscience insights

## Development Notes

- API requests in the frontend are configured to use a proxy in development mode
- For production, update the API_URL in `bravedbalajis-2c58cadb/src/lib/api.ts` 