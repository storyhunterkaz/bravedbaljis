from agno import Agent, Tool
from typing import Dict, Any, List
import json
from collections import Counter
import re

class InterestAnalysisAgent(Agent):
    def __init__(self):
        super().__init__(
            name="InterestAnalysisAgent",
            description="Agent responsible for analyzing and categorizing user interests",
            tools=[
                Tool(
                    name="categorize_interests",
                    description="Categorize interests into predefined domains",
                    function=self.categorize_interests
                ),
                Tool(
                    name="calculate_interest_scores",
                    description="Calculate interest scores based on engagement and frequency",
                    function=self.calculate_interest_scores
                ),
                Tool(
                    name="identify_learning_opportunities",
                    description="Identify potential learning opportunities based on interests",
                    function=self.identify_learning_opportunities
                )
            ]
        )
        
        # Predefined interest categories
        self.categories = {
            "technology": ["programming", "ai", "blockchain", "web3", "crypto"],
            "business": ["entrepreneurship", "startups", "investing", "finance"],
            "personal_development": ["productivity", "mindfulness", "leadership"],
            "creative": ["design", "art", "writing", "music"],
            "science": ["physics", "biology", "chemistry", "mathematics"]
        }

    async def categorize_interests(self, topics: List[str]) -> Dict[str, Any]:
        """Categorize topics into predefined interest domains"""
        categorized = {category: [] for category in self.categories.keys()}
        uncategorized = []

        for topic in topics:
            categorized_flag = False
            for category, keywords in self.categories.items():
                if any(keyword in topic.lower() for keyword in keywords):
                    categorized[category].append(topic)
                    categorized_flag = True
                    break
            if not categorized_flag:
                uncategorized.append(topic)

        return {
            "categorized_interests": categorized,
            "uncategorized_topics": uncategorized
        }

    async def calculate_interest_scores(self, 
                                     topics: List[str], 
                                     engagement_data: Dict[str, int]) -> Dict[str, float]:
        """Calculate interest scores based on engagement metrics"""
        scores = {}
        total_engagement = sum(engagement_data.values())
        
        for topic in topics:
            # Calculate base score from frequency
            frequency_score = topics.count(topic) / len(topics)
            
            # Calculate engagement score
            engagement_score = engagement_data.get(topic, 0) / total_engagement if total_engagement > 0 else 0
            
            # Combined score (weighted average)
            scores[topic] = (frequency_score * 0.4 + engagement_score * 0.6)

        return scores

    async def identify_learning_opportunities(self, 
                                           interests: Dict[str, List[str]], 
                                           scores: Dict[str, float]) -> Dict[str, Any]:
        """Identify learning opportunities based on interests and scores"""
        opportunities = {}
        
        for category, topics in interests.items():
            if not topics:
                continue
                
            # Sort topics by score
            sorted_topics = sorted(
                [(topic, scores.get(topic, 0)) for topic in topics],
                key=lambda x: x[1],
                reverse=True
            )
            
            # Get top 3 interests for each category
            top_interests = sorted_topics[:3]
            
            opportunities[category] = {
                "primary_interest": top_interests[0][0] if top_interests else None,
                "secondary_interests": [topic for topic, _ in top_interests[1:]],
                "confidence_score": sum(score for _, score in top_interests) / len(top_interests)
            }

        return opportunities

    async def execute(self, task: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute an interest analysis task"""
        if task == "analyze_interests":
            topics = params.get("topics", [])
            engagement_data = params.get("engagement_data", {})
            
            # Step 1: Categorize interests
            categorized = await self.categorize_interests(topics)
            
            # Step 2: Calculate interest scores
            scores = await self.calculate_interest_scores(topics, engagement_data)
            
            # Step 3: Identify learning opportunities
            opportunities = await self.identify_learning_opportunities(
                categorized["categorized_interests"],
                scores
            )
            
            return {
                "categorized_interests": categorized,
                "interest_scores": scores,
                "learning_opportunities": opportunities
            }
        
        raise ValueError(f"Unknown task: {task}") 