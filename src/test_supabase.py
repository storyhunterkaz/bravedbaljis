import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

def test_connection():
    try:
        # Try to fetch a single row from profiles table
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}"
        }
        response = requests.get(
            f"{SUPABASE_URL}/rest/v1/profiles?select=*&limit=1",
            headers=headers
        )
        response.raise_for_status()
        print("Successfully connected to Supabase!")
        print("Response:", response.json())
        return True
    except Exception as e:
        print("Error connecting to Supabase:", str(e))
        return False

if __name__ == "__main__":
    test_connection() 