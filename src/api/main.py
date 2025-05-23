from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="BRAVED BALAJIS API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Supabase client
supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

# Models
class Profile(BaseModel):
    id: str
    username: str
    interests: List[str]
    braved_scores: Dict[str, int]
    balajis_scores: Dict[str, int]
    learning_path: Dict[str, Any]
    created_at: str

class SocialMediaAnalysis(BaseModel):
    twitter_handle: str
    interests: List[str]
    braved_scores: Dict[str, int]
    balajis_scores: Dict[str, int]

# Routes
@app.get("/")
async def root():
    return {"message": "Welcome to BRAVED BALAJIS API"}

@app.get("/profiles/{profile_id}")
async def get_profile(profile_id: str):
    try:
        response = supabase.table("profiles").select("*").eq("id", profile_id).execute()
        if not response.data:
            raise HTTPException(status_code=404, detail="Profile not found")
        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/analyze-social-media")
async def analyze_social_media(data: SocialMediaAnalysis):
    """
    Analyze social media posts and update profile with insights
    This is where Mrs Beens and other agents would work together
    """
    try:
        # TODO: Implement social media analysis
        # 1. Mrs Beens coordinates the analysis
        # 2. Social Media Agent fetches and analyzes posts
        # 3. Interest Analysis Agent categorizes interests
        # 4. BRAVED Analysis Agent calculates scores
        # 5. BALAJIS Analysis Agent calculates scores
        # 6. Learning Path Agent generates path
        # 7. Neuroscience Agent provides insights
        
        return {
            "message": "Analysis completed",
            "interests": data.interests,
            "braved_scores": data.braved_scores,
            "balajis_scores": data.balajis_scores
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/update-learning-path/{profile_id}")
async def update_learning_path(profile_id: str):
    """
    Update learning path based on current scores and interests
    """
    try:
        # TODO: Implement learning path generation
        # 1. Get current profile data
        # 2. Analyze scores and interests
        # 3. Generate personalized learning path
        # 4. Update profile in Supabase
        
        return {"message": "Learning path updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 