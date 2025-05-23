import asyncio
from src.models.profile import Profile
from src.services.profile_service import ProfileService

async def test_profile_operations():
    service = ProfileService()
    
    # Create test profile
    test_profile = Profile(
        username="test_user",
        interests=["bitcoin", "ai", "web3"],
        learning_path={
            "steps": [
                {
                    "title": "Master Bitcoin Fundamentals",
                    "description": "Learn the basics of Bitcoin and cryptocurrency",
                    "resources": ["Bitcoin Whitepaper", "Mastering Bitcoin"]
                }
            ]
        }
    )
    
    # Test create
    created_profile = await service.create_profile(test_profile)
    print("Created profile:", created_profile.dict())
    
    # Test get
    retrieved_profile = await service.get_profile(created_profile.id)
    print("Retrieved profile:", retrieved_profile.dict())
    
    # Test update
    if retrieved_profile:
        retrieved_profile.interests.append("blockchain")
        updated_profile = await service.update_profile(retrieved_profile.id, retrieved_profile)
        if updated_profile:
            print("Updated profile:", updated_profile.dict())
        else:
            print("Failed to update profile")
    else:
        print("Failed to retrieve profile for update")
    
    # Test get all
    all_profiles = await service.get_all_profiles()
    print("All profiles:", [p.dict() for p in all_profiles])
    
    # Test delete
    if created_profile:
        success = await service.delete_profile(created_profile.id)
        print("Delete success:", success)
    else:
        print("Failed to delete profile - no profile ID available")

if __name__ == "__main__":
    asyncio.run(test_profile_operations()) 