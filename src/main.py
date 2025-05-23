from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import profile_routes

app = FastAPI(
    title="BRAVED/BALAJIS Framework API",
    description="API for managing user profiles and learning paths",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(profile_routes.router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to BRAVED/BALAJIS Framework API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    } 