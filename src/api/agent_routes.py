from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from ..agents.orchestrator import MrsBeens
from ..agents.social_media_agent import SocialMediaAgent
from ..agents.interest_analysis_agent import InterestAnalysisAgent
from ..agents.learning_path_agent import LearningPathAgent
from ..agents.braved_analysis_agent import BRAVEDAnalysisAgent
from ..agents.balajis_analysis_agent import BALAJISAnalysisAgent
from ..agents.neuroscience_agent import NeuroscienceAgent
from ..lib.supabase_client import update_profile, get_profile
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Initialize agents
mrs_beens = MrsBeens()

# Initialize specialized agents
social_media_agent = SocialMediaAgent(
    twitter_api_key=os.getenv("TWITTER_API_KEY"),
    twitter_api_secret=os.getenv("TWITTER_API_SECRET")
)
interest_analysis_agent = InterestAnalysisAgent()
learning_path_agent = LearningPathAgent()
braved_analysis_agent = BRAVEDAnalysisAgent()
balajis_analysis_agent = BALAJISAnalysisAgent()
neuroscience_agent = NeuroscienceAgent()

# Register all agents with Mrs Beens
mrs_beens.register_agent(social_media_agent)
mrs_beens.register_agent(interest_analysis_agent)
mrs_beens.register_agent(learning_path_agent)
mrs_beens.register_agent(braved_analysis_agent)
mrs_beens.register_agent(balajis_analysis_agent)
mrs_beens.register_agent(neuroscience_agent)

class AnalysisRequest(BaseModel):
    user_id: str
    task: str
    params: Dict[str, Any]

class NeuroscienceRequest(BaseModel):
    user_id: str

@router.post("/analyze")
async def analyze_profile(request: AnalysisRequest):
    try:
        # Get the analysis from Mrs Beens and her team
        result = await mrs_beens.execute(request.task, request.params)
        
        # Store the results in Supabase
        await update_profile(request.user_id, {
            "braved_scores": result.get("braved_scores", {}),
            "balajis_scores": result.get("balajis_scores", {}),
            "learning_path": result.get("learning_path", {})
        })
        
        return {
            "status": "success",
            "data": result,
            "message": "Analysis completed and stored in Supabase"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/neuroscience")
async def get_neuroscience_insights(request: NeuroscienceRequest):
    try:
        # Get user data from Supabase
        user_data = await get_profile(request.user_id)
        
        # Get insights from neuroscience agent
        insights = await neuroscience_agent.analyze_learning_patterns({
            "user_id": request.user_id,
            "profile": user_data
        })
        
        # Store insights in Supabase
        await update_profile(request.user_id, {
            "neuroscience_insights": insights
        })
        
        return insights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/agents")
async def list_agents():
    return {
        "agents": list(mrs_beens.specialized_agents.keys()),
        "orchestrator": mrs_beens.name
    }

@router.get("/frameworks")
async def list_frameworks():
    return {
        "frameworks": [
            {
                "name": "BRAVED",
                "components": ["Building", "Research", "Art", "Ventures", "Engineering", "Design"],
                "description": "Framework for analyzing creative and technical interests"
            },
            {
                "name": "BALAJIS",
                "components": ["Bitcoin", "AI", "Longevity", "Autonomous", "Jobs", "Internet", "Space"],
                "description": "Framework for analyzing future-oriented interests"
            }
        ]
    } 