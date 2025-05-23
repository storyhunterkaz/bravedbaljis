from typing import Dict, Any, List
import numpy as np
from datetime import datetime, timedelta

class NeuroscienceAgent:
    def __init__(self):
        self.learning_patterns = {
            "visual": {"weight": 0.3, "indicators": ["diagrams", "videos", "images"]},
            "auditory": {"weight": 0.3, "indicators": ["podcasts", "discussions", "lectures"]},
            "kinesthetic": {"weight": 0.2, "indicators": ["projects", "exercises", "hands-on"]},
            "reading_writing": {"weight": 0.2, "indicators": ["articles", "notes", "documentation"]}
        }
        
        self.mastery_levels = {
            "novice": {"threshold": 0.3, "description": "Basic understanding"},
            "intermediate": {"threshold": 0.6, "description": "Good working knowledge"},
            "advanced": {"threshold": 0.8, "description": "Deep understanding"},
            "expert": {"threshold": 0.95, "description": "Mastery level"}
        }

    async def analyze_learning_patterns(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Analyze user's learning patterns based on their activity data
        """
        pattern_analysis = {
            "learning_style_preferences": {},
            "optimal_learning_times": [],
            "retention_patterns": {},
            "recommendations": []
        }

        # Analyze learning style preferences
        for style, data in self.learning_patterns.items():
            score = self._calculate_style_score(user_data, data["indicators"])
            pattern_analysis["learning_style_preferences"][style] = {
                "score": score,
                "weight": data["weight"]
            }

        # Analyze optimal learning times
        if "activity_times" in user_data:
            pattern_analysis["optimal_learning_times"] = self._analyze_optimal_times(
                user_data["activity_times"]
            )

        # Analyze retention patterns
        if "quiz_results" in user_data:
            pattern_analysis["retention_patterns"] = self._analyze_retention(
                user_data["quiz_results"]
            )

        # Generate recommendations
        pattern_analysis["recommendations"] = self._generate_recommendations(
            pattern_analysis
        )

        return pattern_analysis

    async def assess_mastery_level(self, topic_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Assess mastery level for a specific topic
        """
        assessment = {
            "topic": topic_data.get("name"),
            "mastery_level": None,
            "score": 0.0,
            "strengths": [],
            "areas_for_improvement": [],
            "recommendations": []
        }

        # Calculate mastery score
        assessment["score"] = self._calculate_mastery_score(topic_data)

        # Determine mastery level
        for level, data in self.mastery_levels.items():
            if assessment["score"] >= data["threshold"]:
                assessment["mastery_level"] = level
                break

        # Analyze strengths and areas for improvement
        assessment["strengths"] = self._identify_strengths(topic_data)
        assessment["areas_for_improvement"] = self._identify_improvement_areas(topic_data)

        # Generate recommendations
        assessment["recommendations"] = self._generate_mastery_recommendations(
            assessment
        )

        return assessment

    def _calculate_style_score(self, user_data: Dict[str, Any], indicators: List[str]) -> float:
        """Calculate score for a specific learning style"""
        score = 0.0
        total_activities = 0

        for activity in user_data.get("activities", []):
            if any(indicator in activity.get("type", "").lower() for indicator in indicators):
                score += activity.get("engagement_score", 0)
                total_activities += 1

        return score / total_activities if total_activities > 0 else 0.0

    def _analyze_optimal_times(self, activity_times: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Analyze optimal learning times based on activity data"""
        time_slots = {}
        
        for activity in activity_times:
            hour = activity["timestamp"].hour
            if hour not in time_slots:
                time_slots[hour] = {
                    "count": 0,
                    "success_rate": 0
                }
            time_slots[hour]["count"] += 1
            time_slots[hour]["success_rate"] += activity.get("success_rate", 0)

        optimal_times = []
        for hour, data in time_slots.items():
            if data["count"] > 0:
                optimal_times.append({
                    "hour": hour,
                    "success_rate": data["success_rate"] / data["count"],
                    "activity_count": data["count"]
                })

        return sorted(optimal_times, key=lambda x: x["success_rate"], reverse=True)

    def _analyze_retention(self, quiz_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze retention patterns from quiz results"""
        retention_analysis = {
            "overall_retention": 0.0,
            "topic_retention": {},
            "time_based_retention": {}
        }

        # Calculate overall retention
        total_questions = sum(quiz["total_questions"] for quiz in quiz_results)
        correct_answers = sum(quiz["correct_answers"] for quiz in quiz_results)
        retention_analysis["overall_retention"] = (correct_answers / total_questions) * 100

        # Analyze retention by topic
        for quiz in quiz_results:
            topic = quiz["topic"]
            if topic not in retention_analysis["topic_retention"]:
                retention_analysis["topic_retention"][topic] = {
                    "total_questions": 0,
                    "correct_answers": 0
                }
            retention_analysis["topic_retention"][topic]["total_questions"] += quiz["total_questions"]
            retention_analysis["topic_retention"][topic]["correct_answers"] += quiz["correct_answers"]

        return retention_analysis

    def _calculate_mastery_score(self, topic_data: Dict[str, Any]) -> float:
        """Calculate mastery score based on various factors"""
        weights = {
            "quiz_scores": 0.3,
            "project_completion": 0.3,
            "time_spent": 0.2,
            "engagement": 0.2
        }

        quiz_score = np.mean(topic_data.get("quiz_scores", [0])) * 100
        project_score = topic_data.get("project_completion", 0) * 100
        time_score = min(topic_data.get("time_spent", 0) / topic_data.get("expected_time", 1), 1) * 100
        engagement_score = topic_data.get("engagement_score", 0) * 100

        return (
            quiz_score * weights["quiz_scores"] +
            project_score * weights["project_completion"] +
            time_score * weights["time_spent"] +
            engagement_score * weights["engagement"]
        )

    def _identify_strengths(self, topic_data: Dict[str, Any]) -> List[str]:
        """Identify strengths in the topic"""
        strengths = []
        
        if topic_data.get("quiz_scores", []):
            avg_quiz_score = np.mean(topic_data["quiz_scores"])
            if avg_quiz_score > 0.8:
                strengths.append("Strong theoretical understanding")
        
        if topic_data.get("project_completion", 0) > 0.8:
            strengths.append("Excellent practical application")
        
        if topic_data.get("engagement_score", 0) > 0.8:
            strengths.append("High engagement and participation")

        return strengths

    def _identify_improvement_areas(self, topic_data: Dict[str, Any]) -> List[str]:
        """Identify areas for improvement"""
        improvement_areas = []
        
        if topic_data.get("quiz_scores", []):
            avg_quiz_score = np.mean(topic_data["quiz_scores"])
            if avg_quiz_score < 0.6:
                improvement_areas.append("Need to strengthen theoretical understanding")
        
        if topic_data.get("project_completion", 0) < 0.6:
            improvement_areas.append("Need more practical experience")
        
        if topic_data.get("engagement_score", 0) < 0.6:
            improvement_areas.append("Need to increase engagement")

        return improvement_areas

    def _generate_recommendations(self, pattern_analysis: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate personalized learning recommendations"""
        recommendations = []

        # Add recommendations based on learning style preferences
        for style, data in pattern_analysis["learning_style_preferences"].items():
            if data["score"] > 0.7:
                recommendations.append({
                    "type": "learning_style",
                    "message": f"Leverage your strong {style} learning preference",
                    "suggestions": self._get_style_specific_suggestions(style)
                })

        # Add recommendations based on optimal learning times
        if pattern_analysis["optimal_learning_times"]:
            best_time = pattern_analysis["optimal_learning_times"][0]
            recommendations.append({
                "type": "timing",
                "message": f"Schedule learning sessions around {best_time['hour']}:00",
                "suggestions": ["Plan intensive learning during optimal hours"]
            })

        return recommendations

    def _generate_mastery_recommendations(self, assessment: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Generate recommendations based on mastery assessment"""
        recommendations = []

        if assessment["mastery_level"] == "novice":
            recommendations.extend([
                {
                    "type": "foundation",
                    "message": "Focus on building strong fundamentals",
                    "suggestions": [
                        "Complete basic tutorials",
                        "Practice with simple exercises",
                        "Review core concepts regularly"
                    ]
                }
            ])
        elif assessment["mastery_level"] == "intermediate":
            recommendations.extend([
                {
                    "type": "practice",
                    "message": "Enhance practical application",
                    "suggestions": [
                        "Work on more complex projects",
                        "Participate in peer reviews",
                        "Teach basic concepts to others"
                    ]
                }
            ])
        elif assessment["mastery_level"] == "advanced":
            recommendations.extend([
                {
                    "type": "expertise",
                    "message": "Develop advanced expertise",
                    "suggestions": [
                        "Contribute to open-source projects",
                        "Write technical articles",
                        "Mentor others"
                    ]
                }
            ])

        return recommendations

    def _get_style_specific_suggestions(self, style: str) -> List[str]:
        """Get style-specific learning suggestions"""
        suggestions = {
            "visual": [
                "Use mind maps for note-taking",
                "Watch video tutorials",
                "Create visual diagrams"
            ],
            "auditory": [
                "Listen to educational podcasts",
                "Participate in group discussions",
                "Record and listen to your notes"
            ],
            "kinesthetic": [
                "Build hands-on projects",
                "Use physical models",
                "Practice with real-world applications"
            ],
            "reading_writing": [
                "Write detailed notes",
                "Read technical documentation",
                "Create written summaries"
            ]
        }
        return suggestions.get(style, [])
