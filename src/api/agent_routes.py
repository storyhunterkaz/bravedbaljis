from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from ..agents.orchestrator import OrchestratorAgent
from ..agents.social_media_agent import SocialMediaAgent
from ..agents.interest_analysis_agent import InterestAnalysisAgent
from ..agents.learning_path_agent import LearningPathAgent
from ..agents.braved_analysis_agent import BRAVEDAnalysisAgent
from ..agents.balajis_analysis_agent import BALAJISAnalysisAgent
from ..agents.neuroscience_agent import NeuroscienceAgent
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

# Initialize agents
orchestrator = OrchestratorAgent()

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

# Register all agents with orchestrator
orchestrator.register_agent(social_media_agent)
orchestrator.register_agent(interest_analysis_agent)
orchestrator.register_agent(learning_path_agent)
orchestrator.register_agent(braved_analysis_agent)
orchestrator.register_agent(balajis_analysis_agent)
orchestrator.register_agent(neuroscience_agent)

class AnalysisRequest(BaseModel):
    user_id: str
    task: str
    params: Dict[str, Any]

class NeuroscienceRequest(BaseModel):
    user_id: str

@router.post("/analyze")
async def analyze_profile(request: AnalysisRequest):
    try:
        result = await orchestrator.execute(request.task, request.params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/neuroscience")
async def get_neuroscience_insights(request: NeuroscienceRequest):
    try:
        # Get user data from your database or other sources
        user_data = {
            "activities": [
                {"type": "visual", "engagement_score": 0.8},
                {"type": "auditory", "engagement_score": 0.6},
                {"type": "kinesthetic", "engagement_score": 0.9},
                {"type": "reading_writing", "engagement_score": 0.7}
            ],
            "activity_times": [
                {"timestamp": "2024-03-20T10:00:00", "success_rate": 0.9},
                {"timestamp": "2024-03-20T14:00:00", "success_rate": 0.8},
                {"timestamp": "2024-03-20T16:00:00", "success_rate": 0.95}
            ],
            "quiz_results": [
                {"topic": "Web3", "total_questions": 10, "correct_answers": 8},
                {"topic": "AI", "total_questions": 10, "correct_answers": 7}
            ]
        }
        
        # Get insights from neuroscience agent
        insights = await neuroscience_agent.analyze_learning_patterns(user_data)
        return insights
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/agents")
async def list_agents():
    return {
        "agents": list(orchestrator.specialized_agents.keys()),
        "orchestrator": orchestrator.name
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