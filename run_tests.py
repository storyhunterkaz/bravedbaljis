import os
import sys
import asyncio
from src.tests.test_profile import test_profile_operations

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    asyncio.run(test_profile_operations()) 