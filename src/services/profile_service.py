from typing import List, Optional
from src.config.database import get_supabase_headers, get_supabase_url
from src.models.profile import Profile
import requests

class ProfileService:
    def __init__(self):
        self.headers = get_supabase_headers()
        self.base_url = get_supabase_url()
        self.table = "profiles"

    async def create_profile(self, profile: Profile) -> Profile:
        """Create a new profile"""
        data = profile.dict(exclude={'id', 'created_at'})
        response = requests.post(
            f"{self.base_url}/rest/v1/{self.table}",
            headers=self.headers,
            json=data
        )
        response.raise_for_status()
        return Profile(**response.json()[0])

    async def get_profile(self, profile_id: str) -> Optional[Profile]:
        """Get a profile by ID"""
        response = requests.get(
            f"{self.base_url}/rest/v1/{self.table}",
            headers=self.headers,
            params={"id": f"eq.{profile_id}"}
        )
        response.raise_for_status()
        data = response.json()
        if data:
            return Profile(**data[0])
        return None

    async def get_all_profiles(self) -> List[Profile]:
        """Get all profiles"""
        response = requests.get(
            f"{self.base_url}/rest/v1/{self.table}",
            headers=self.headers
        )
        response.raise_for_status()
        return [Profile(**profile) for profile in response.json()]

    async def update_profile(self, profile_id: str, profile: Profile) -> Optional[Profile]:
        """Update a profile"""
        data = profile.dict(exclude={'id', 'created_at'})
        response = requests.patch(
            f"{self.base_url}/rest/v1/{self.table}",
            headers=self.headers,
            params={"id": f"eq.{profile_id}"},
            json=data
        )
        response.raise_for_status()
        data = response.json()
        if data:
            return Profile(**data[0])
        return None

    async def delete_profile(self, profile_id: str) -> bool:
        """Delete a profile"""
        response = requests.delete(
            f"{self.base_url}/rest/v1/{self.table}",
            headers=self.headers,
            params={"id": f"eq.{profile_id}"}
        )
        response.raise_for_status()
        return bool(response.json()) 