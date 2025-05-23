from fastapi import APIRouter, HTTPException
from typing import List
from src.models.profile import Profile
from src.services.profile_service import ProfileService

router = APIRouter(prefix="/profiles", tags=["profiles"])
profile_service = ProfileService()

@router.post("/", response_model=Profile)
async def create_profile(profile: Profile):
    """Create a new profile"""
    try:
        return await profile_service.create_profile(profile)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{profile_id}", response_model=Profile)
async def get_profile(profile_id: str):
    """Get a profile by ID"""
    profile = await profile_service.get_profile(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.get("/", response_model=List[Profile])
async def get_all_profiles():
    """Get all profiles"""
    return await profile_service.get_all_profiles()

@router.put("/{profile_id}", response_model=Profile)
async def update_profile(profile_id: str, profile: Profile):
    """Update a profile"""
    updated_profile = await profile_service.update_profile(profile_id, profile)
    if not updated_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated_profile

@router.delete("/{profile_id}")
async def delete_profile(profile_id: str):
    """Delete a profile"""
    success = await profile_service.delete_profile(profile_id)
    if not success:
        raise HTTPException(status_code=404, detail="Profile not found")
    return {"message": "Profile deleted successfully"} 