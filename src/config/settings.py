import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase settings
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000

# CORS settings
CORS_ORIGINS = [
    "http://localhost:5173",  # Frontend development server
    "http://localhost:3000",  # Alternative frontend port
]

# Framework settings
BRAVED_FRAMEWORK = {
    "bitcoin": "Bitcoin & Cryptocurrency",
    "real_world": "Real World Assets/NFTs/Web3 Gaming",
    "ai": "AI/AI Agents & Prompting",
    "vrar": "VR/AR & Spatial Computing/Metaverse",
    "emotional": "Emotional Intelligence",
    "decentralization": "Decentralization & Cryptography"
}

BALAJIS_FRAMEWORK = {
    "build": "Build",
    "attention": "Attention",
    "leverage": "Leverage",
    "algorithms": "Algorithms",
    "joy": "Joy",
    "influence": "Influence",
    "skills": "Skills"
} 