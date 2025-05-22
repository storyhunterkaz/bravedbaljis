from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from .agent_routes import router as agent_router

# Create FastAPI app
app = FastAPI(title="BRAVED BALAJIS API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(agent_router, prefix="", tags=["agents"])

@app.get("/")
async def root():
    return {
        "name": "BRAVED BALAJIS API",
        "version": "1.0.0",
        "status": "online",
        "documentation": "/docs"
    }

# Run the application if executed directly
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 