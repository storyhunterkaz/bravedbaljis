from agno import Agent, Tool
from typing import List, Dict, Any
import json

class MrsBeens(Agent):
    def __init__(self):
        super().__init__(
            name="Mrs Beens",
            description="Lead agent who coordinates all other specialized agents - funny like Mr Bean, tech-savvy like Balaji Srinivasan, and swarmy like a bee",
            tools=[
                Tool(
                    name="delegate_task",
                    description="Delegate a task to a specialized agent",
                    function=self.delegate_task
                ),
                Tool(
                    name="aggregate_results",
                    description="Aggregate results from multiple agents",
                    function=self.aggregate_results
                )
            ]
        )
        self.specialized_agents = {}

    def register_agent(self, agent: Agent):
        """Register a specialized agent with the orchestrator"""
        self.specialized_agents[agent.name] = agent

    async def delegate_task(self, task: str, agent_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Delegate a task to a specialized agent"""
        if agent_name not in self.specialized_agents:
            raise ValueError(f"Agent {agent_name} not found")
        
        agent = self.specialized_agents[agent_name]
        return await agent.execute(task, params)

    async def aggregate_results(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aggregate results from multiple agents"""
        # Implement aggregation logic based on your needs
        return {
            "aggregated_results": results,
            "summary": "Combined analysis from all agents"
        }

    async def execute(self, task: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task by coordinating multiple agents"""
        # Example task execution flow
        if task == "analyze_user_profile":
            # 1. Delegate social media analysis
            social_media_results = await self.delegate_task(
                "analyze_posts",
                "SocialMediaAgent",
                params
            )
            
            # 2. Delegate interest analysis
            interest_results = await self.delegate_task(
                "analyze_interests",
                "InterestAnalysisAgent",
                params
            )
            
            # 3. Delegate learning path generation
            learning_path = await self.delegate_task(
                "generate_learning_path",
                "LearningPathAgent",
                {
                    "social_media_analysis": social_media_results,
                    "interest_analysis": interest_results
                }
            )
            
            # 4. Aggregate all results
            return await self.aggregate_results([
                social_media_results,
                interest_results,
                learning_path
            ])
        
        raise ValueError(f"Unknown task: {task}") 