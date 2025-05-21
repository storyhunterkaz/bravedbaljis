from agno import Agent, Tool
from typing import Dict, Any, List
import json
from datetime import datetime, timedelta

class LearningPathAgent(Agent):
    def __init__(self):
        super().__init__(
            name="LearningPathAgent",
            description="Agent responsible for generating personalized learning paths",
            tools=[
                Tool(
                    name="generate_learning_modules",
                    description="Generate learning modules based on interests",
                    function=self.generate_learning_modules
                ),
                Tool(
                    name="create_learning_schedule",
                    description="Create a personalized learning schedule",
                    function=self.create_learning_schedule
                ),
                Tool(
                    name="recommend_resources",
                    description="Recommend learning resources for each module",
                    function=self.recommend_resources
                )
            ]
        )
        
        # Learning resource types
        self.resource_types = {
            "courses": ["udemy", "coursera", "edx", "khan academy"],
            "books": ["technical", "business", "self-help"],
            "videos": ["youtube", "vimeo", "ted talks"],
            "communities": ["discord", "slack", "reddit"],
            "practice": ["exercises", "projects", "challenges"]
        }

    async def generate_learning_modules(self, 
                                      interests: Dict[str, Any], 
                                      skill_level: str = "beginner") -> List[Dict[str, Any]]:
        """Generate learning modules based on interests and skill level"""
        modules = []
        
        for category, data in interests.items():
            if not data.get("primary_interest"):
                continue
                
            module = {
                "title": f"{data['primary_interest'].title()} Fundamentals",
                "category": category,
                "skill_level": skill_level,
                "duration_weeks": 4,
                "objectives": [
                    f"Understand core concepts of {data['primary_interest']}",
                    f"Apply {data['primary_interest']} principles in practice",
                    f"Build a foundation for advanced {data['primary_interest']} topics"
                ],
                "prerequisites": [],
                "resources": await self.recommend_resources(
                    data['primary_interest'],
                    category,
                    skill_level
                )
            }
            modules.append(module)
            
        return modules

    async def create_learning_schedule(self, 
                                     modules: List[Dict[str, Any]], 
                                     start_date: datetime = None) -> Dict[str, Any]:
        """Create a personalized learning schedule"""
        if not start_date:
            start_date = datetime.now()
            
        schedule = {
            "start_date": start_date.isoformat(),
            "modules": []
        }
        
        current_date = start_date
        for module in modules:
            module_schedule = {
                "module_title": module["title"],
                "start_date": current_date.isoformat(),
                "end_date": (current_date + timedelta(weeks=module["duration_weeks"])).isoformat(),
                "weekly_commitment": "5-7 hours",
                "milestones": [
                    {
                        "week": i + 1,
                        "description": f"Week {i + 1} objectives",
                        "tasks": module["objectives"][i % len(module["objectives"])]
                    }
                    for i in range(module["duration_weeks"])
                ]
            }
            schedule["modules"].append(module_schedule)
            current_date += timedelta(weeks=module["duration_weeks"])
            
        return schedule

    async def recommend_resources(self, 
                                topic: str, 
                                category: str, 
                                skill_level: str) -> Dict[str, List[Dict[str, str]]]:
        """Recommend learning resources for a specific topic"""
        resources = {}
        
        for resource_type, platforms in self.resource_types.items():
            resources[resource_type] = []
            
            # Example resource recommendations
            if resource_type == "courses":
                resources[resource_type].extend([
                    {
                        "title": f"{topic.title()} for {skill_level.title()}s",
                        "platform": "udemy",
                        "url": f"https://udemy.com/courses/{topic}-{skill_level}"
                    },
                    {
                        "title": f"Introduction to {topic}",
                        "platform": "coursera",
                        "url": f"https://coursera.org/learn/{topic}"
                    }
                ])
            elif resource_type == "books":
                resources[resource_type].append({
                    "title": f"The Complete Guide to {topic.title()}",
                    "author": "Expert Author",
                    "url": f"https://books.com/{topic}"
                })
            elif resource_type == "videos":
                resources[resource_type].append({
                    "title": f"{topic.title()} Tutorial Series",
                    "platform": "youtube",
                    "url": f"https://youtube.com/playlist?list={topic}"
                })
            elif resource_type == "communities":
                resources[resource_type].append({
                    "title": f"{topic.title()} Community",
                    "platform": "discord",
                    "url": f"https://discord.gg/{topic}"
                })
            elif resource_type == "practice":
                resources[resource_type].append({
                    "title": f"{topic.title()} Practice Projects",
                    "platform": "github",
                    "url": f"https://github.com/topics/{topic}-projects"
                })
                
        return resources

    async def execute(self, task: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a learning path generation task"""
        if task == "generate_learning_path":
            interests = params.get("interests", {})
            skill_level = params.get("skill_level", "beginner")
            start_date = params.get("start_date")
            
            if start_date:
                start_date = datetime.fromisoformat(start_date)
            
            # Step 1: Generate learning modules
            modules = await self.generate_learning_modules(interests, skill_level)
            
            # Step 2: Create learning schedule
            schedule = await self.create_learning_schedule(modules, start_date)
            
            return {
                "modules": modules,
                "schedule": schedule,
                "total_duration_weeks": sum(module["duration_weeks"] for module in modules)
            }
        
        raise ValueError(f"Unknown task: {task}") 