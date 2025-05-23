import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Supabase configuration
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

def setup_database():
    try:
        # Create profiles table using SQL
        headers = {
            "apikey": SUPABASE_KEY,
            "Authorization": f"Bearer {SUPABASE_KEY}",
            "Content-Type": "application/json",
            "Prefer": "return=minimal"
        }
        
        # SQL to create the table
        sql = """
        CREATE TABLE IF NOT EXISTS profiles (
            id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
            username TEXT,
            interests TEXT[] DEFAULT '{}',
            braved_scores JSONB DEFAULT '{
                "bitcoin": 0,
                "real_world": 0,
                "ai": 0,
                "vrar": 0,
                "emotional": 0,
                "decentralization": 0
            }',
            balajis_scores JSONB DEFAULT '{
                "build": 0,
                "attention": 0,
                "leverage": 0,
                "algorithms": 0,
                "joy": 0,
                "influence": 0,
                "skills": 0
            }',
            learning_path JSONB DEFAULT '{
                "steps": []
            }',
            created_at TIMESTAMPTZ DEFAULT NOW()
        );

        -- Enable Row Level Security
        ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;

        -- Create policy to allow public read access
        CREATE POLICY IF NOT EXISTS "Allow public read access"
            ON profiles FOR SELECT
            USING (true);

        -- Create policy to allow authenticated users to update their own profile
        CREATE POLICY IF NOT EXISTS "Allow users to update own profile"
            ON profiles FOR UPDATE
            USING (auth.uid() = id);
        """
        
        # Execute SQL through REST API
        response = requests.post(
            f"{SUPABASE_URL}/rest/v1/rpc/exec_sql",
            headers=headers,
            json={"sql": sql}
        )
        response.raise_for_status()
        print("Successfully set up database schema!")
        return True
    except Exception as e:
        print("Error setting up database:", str(e))
        return False

if __name__ == "__main__":
    setup_database() 