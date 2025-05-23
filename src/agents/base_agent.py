from abc import ABC, abstractmethod
from typing import Dict, List, Any
from supabase import create_client, Client
from ..config.settings import SUPABASE_URL, SUPABASE_SERVICE_KEY

class BaseAgent(ABC):
    def __init__(self):
        self.supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

    @abstractmethod
    async def process(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process the input data and return results
        Must be implemented by each agent
        """
        pass

    async def save_to_supabase(self, table: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Save data to Supabase
        """
        try:
            response = self.supabase.table(table).insert(data).execute()
            return response.data[0]
        except Exception as e:
            print(f"Error saving to Supabase: {str(e)}")
            raise

    async def get_from_supabase(self, table: str, query: Dict[str, Any]) -> Dict[str, Any]:
        """
        Get data from Supabase
        """
        try:
            response = self.supabase.table(table).select("*").match(query).execute()
            return response.data[0] if response.data else None
        except Exception as e:
            print(f"Error getting from Supabase: {str(e)}")
            raise 