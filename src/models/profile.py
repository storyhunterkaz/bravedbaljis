from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime

class LearningStep(BaseModel):
    title: str
    description: str
    resources: List[str]

class LearningPath(BaseModel):
    steps: List[LearningStep] = []

class BravedScores(BaseModel):
    bitcoin: int = 0
    real_world: int = 0
    ai: int = 0
    vrar: int = 0
    emotional: int = 0
    decentralization: int = 0

class BalajisScores(BaseModel):
    build: int = 0
    attention: int = 0
    leverage: int = 0
    algorithms: int = 0
    joy: int = 0
    influence: int = 0
    skills: int = 0

class Profile(BaseModel):
    id: Optional[str] = None
    username: str
    interests: List[str] = []
    braved_scores: Dict[str, int] = {
        "bitcoin": 0,
        "real_world": 0,
        "ai": 0,
        "vrar": 0,
        "emotional": 0,
        "decentralization": 0
    }
    balajis_scores: Dict[str, int] = {
        "build": 0,
        "attention": 0,
        "leverage": 0,
        "algorithms": 0,
        "joy": 0,
        "influence": 0,
        "skills": 0
    }
    learning_path: Dict[str, List[Dict[str, str]]] = {"steps": []}
    created_at: Optional[str] = None

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        } 