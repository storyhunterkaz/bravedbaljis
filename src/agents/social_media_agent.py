from agno import Agent, Tool
from typing import Dict, Any
import tweepy
import json

class SocialMediaAgent(Agent):
    def __init__(self, twitter_api_key: str, twitter_api_secret: str):
        super().__init__(
            name="SocialMediaAgent",
            description="Agent responsible for analyzing social media posts",
            tools=[
                Tool(
                    name="analyze_twitter_posts",
                    description="Analyze Twitter posts for interests and topics",
                    function=self.analyze_twitter_posts
                ),
                Tool(
                    name="extract_topics",
                    description="Extract main topics from social media content",
                    function=self.extract_topics
                )
            ]
        )
        self.twitter_client = tweepy.Client(
            bearer_token=twitter_api_key,
            consumer_key=twitter_api_key,
            consumer_secret=twitter_api_secret
        )

    async def analyze_twitter_posts(self, username: str, limit: int = 100) -> Dict[str, Any]:
        """Analyze Twitter posts for a given username"""
        try:
            # Get user's recent tweets
            tweets = self.twitter_client.get_users_tweets(
                username=username,
                max_results=limit,
                tweet_fields=['created_at', 'public_metrics']
            )

            # Analyze tweet content
            analysis = {
                "topics": await self.extract_topics([tweet.text for tweet in tweets.data]),
                "engagement_metrics": {
                    "total_likes": sum(tweet.public_metrics['like_count'] for tweet in tweets.data),
                    "total_retweets": sum(tweet.public_metrics['retweet_count'] for tweet in tweets.data)
                },
                "post_frequency": len(tweets.data) / 30  # posts per month
            }

            return analysis
        except Exception as e:
            return {"error": str(e)}

    async def extract_topics(self, texts: list) -> Dict[str, Any]:
        """Extract main topics from a list of texts"""
        # Implement topic extraction logic here
        # This could use NLP libraries or external APIs
        return {
            "main_topics": ["topic1", "topic2"],  # Example
            "topic_confidence": 0.85
        }

    async def execute(self, task: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a social media analysis task"""
        if task == "analyze_posts":
            return await self.analyze_twitter_posts(
                username=params.get("username"),
                limit=params.get("limit", 100)
            )
        elif task == "extract_topics":
            return await self.extract_topics(params.get("texts", []))
        
        raise ValueError(f"Unknown task: {task}") 