import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

def create_test_profile():
    try:
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=representation"
        }
        
        # Test profile data
        profile_data = {
            "username": "test_user",
            "interests": ["bitcoin", "ai", "web3"],
            "braved_scores": {
                "bitcoin": 75,
                "real_world": 60,
                "ai": 80,
                "vrar": 45,
                "emotional": 55,
                "decentralization": 70
            },
            "balajis_scores": {
                "build": 85,
                "attention": 70,
                "leverage": 65,
                "algorithms": 90,
                "joy": 75,
                "influence": 60,
                "skills": 80
            },
            "learning_path": {
                "steps": [
                    {
                        "title": "Master Bitcoin Fundamentals",
                        "description": "Learn the basics of Bitcoin and cryptocurrency",
                        "resources": ["Bitcoin Whitepaper", "Mastering Bitcoin"]
                    }
                ]
            }
        }
        
        # Create profile
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/profiles",
            headers=headers,
            json=profile_data
        )
        response.raise_for_status()
        print("Successfully created test profile!")
        print("Response:", response.json())
        return True
    except Exception as e:
        print("Error creating test profile:", str(e))
        return False

if __name__ == "__main__":
    create_test_profile() 