from agno import Agent, Tool
from typing import Dict, Any, List
import json

class BALAJISAnalysisAgent(Agent):
    def __init__(self):
        super().__init__(
            name="BALAJISAnalysisAgent",
            description="Agent responsible for applying the BALAJIS framework to learning analysis",
            tools=[
                Tool(
                    name="analyze_balajis_components",
                    description="Analyze user interests through BALAJIS framework",
                    function=self.analyze_balajis_components
                ),
                Tool(
                    name="generate_balajis_recommendations",
                    description="Generate recommendations based on BALAJIS analysis",
                    function=self.generate_balajis_recommendations
                ),
                Tool(
                    name="assess_balajis_alignment",
                    description="Assess alignment with BALAJIS framework principles",
                    function=self.assess_balajis_alignment
                )
            ]
        )
        
        # BALAJIS framework components with correct definitions
        self.balajis_components = {
            "B": {
                "name": "Build",
                "keywords": ["creation", "development", "construction", "making", "building", "projects"],
                "description": "Creating and developing tangible or digital products and solutions"
            },
            "A": {
                "name": "Attention",
                "keywords": ["focus", "concentration", "mindfulness", "awareness", "presence", "mindset"],
                "description": "Developing focus, mindfulness, and present-moment awareness"
            },
            "L": {
                "name": "Leverage",
                "keywords": ["efficiency", "optimization", "automation", "systems", "scaling", "multipliers"],
                "description": "Creating systems and processes that multiply your impact and efficiency"
            },
            "A": {
                "name": "Algorithms",
                "keywords": ["patterns", "systems", "processes", "automation", "optimization", "efficiency"],
                "description": "Understanding and implementing systematic approaches to problem-solving"
            },
            "J": {
                "name": "Joy",
                "keywords": ["happiness", "fulfillment", "passion", "purpose", "meaning", "enjoyment"],
                "description": "Finding joy and fulfillment in your work and life"
            },
            "I": {
                "name": "Influence",
                "keywords": ["leadership", "impact", "persuasion", "communication", "networking", "relationships"],
                "description": "Building influence and making a positive impact on others"
            },
            "S": {
                "name": "Skills",
                "keywords": ["expertise", "competence", "mastery", "learning", "development", "capabilities"],
                "description": "Developing and mastering essential skills for success"
            }
        }

    async def analyze_balajis_components(self, interests: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze interests through the BALAJIS framework"""
        analysis = {component: 0 for component in self.balajis_components.keys()}
        component_details = {}
        
        for category, data in interests.items():
            if not data.get("primary_interest"):
                continue
                
            interest = data["primary_interest"].lower()
            for component, info in self.balajis_components.items():
                if any(keyword in interest for keyword in info["keywords"]):
                    analysis[component] += data.get("confidence_score", 0.5)
                    if component not in component_details:
                        component_details[component] = []
                    component_details[component].append({
                        "interest": data["primary_interest"],
                        "category": category,
                        "confidence": data.get("confidence_score", 0.5)
                    })
        
        return {
            "component_scores": analysis,
            "component_details": component_details,
            "dominant_components": sorted(
                analysis.items(),
                key=lambda x: x[1],
                reverse=True
            )[:3]
        }

    async def generate_balajis_recommendations(self, 
                                            analysis: Dict[str, Any], 
                                            skill_level: str = "beginner") -> Dict[str, Any]:
        """Generate recommendations based on BALAJIS analysis"""
        recommendations = {}
        
        for component, score in analysis["component_scores"].items():
            if score > 0:
                component_info = self.balajis_components[component]
                recommendations[component] = {
                    "name": component_info["name"],
                    "description": component_info["description"],
                    "current_score": score,
                    "learning_path": {},
                    "resources": {},
                    "projects": []
                }

                # Component-specific recommendations
                if component == "B":  # Build
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Product Development Fundamentals",
                            "steps": [
                                "Understanding product development",
                                "Basic prototyping",
                                "User research",
                                "MVP creation"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Product Development",
                            "steps": [
                                "Advanced prototyping",
                                "User testing",
                                "Product iteration",
                                "Market validation"
                            ]
                        },
                        "advanced": {
                            "title": "Product Strategy & Scaling",
                            "steps": [
                                "Product strategy",
                                "Team building",
                                "Scaling strategies",
                                "Product vision"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "producthunt",
                                "title": "Product Development",
                                "url": "https://producthunt.com/ship",
                                "level": "beginner"
                            },
                            {
                                "platform": "indiehackers",
                                "title": "Product Strategy",
                                "url": "https://indiehackers.com/start",
                                "level": "intermediate"
                            }
                        ],
                        "books": [
                            {
                                "title": "The Lean Product Playbook",
                                "author": "Dan Olsen",
                                "url": "https://leanproductplaybook.com"
                            },
                            {
                                "title": "Product-Led Growth",
                                "author": "Wes Bush",
                                "url": "https://productled.com"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "Product School",
                                "url": "https://youtube.com/productschool",
                                "focus": "Product management"
                            },
                            {
                                "name": "Product Hunt",
                                "url": "https://youtube.com/producthunt",
                                "focus": "Product launches"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "slack",
                                "name": "Product Hunt",
                                "url": "https://slack.producthunt.com",
                                "focus": "Product development"
                            },
                            {
                                "platform": "discord",
                                "name": "Indie Hackers",
                                "url": "https://discord.gg/indiehackers",
                                "focus": "Product building"
                            }
                        ],
                        "tools": [
                            {
                                "name": "Figma",
                                "url": "https://figma.com",
                                "purpose": "Design and prototyping"
                            },
                            {
                                "name": "Notion",
                                "url": "https://notion.so",
                                "purpose": "Product documentation"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "MVP Development",
                            "level": "beginner",
                            "description": "Create a minimum viable product",
                            "technologies": ["No-code", "Prototyping"],
                            "learning_outcomes": [
                                "Product development",
                                "User research",
                                "MVP creation"
                            ],
                            "resources": [
                                "https://nocode.tech",
                                "https://bubble.io/learn"
                            ]
                        },
                        {
                            "title": "Product Launch",
                            "level": "intermediate",
                            "description": "Launch a product to market",
                            "technologies": ["Marketing", "Analytics"],
                            "learning_outcomes": [
                                "Product launch",
                                "Market validation",
                                "User acquisition"
                            ],
                            "resources": [
                                "https://producthunt.com/launch",
                                "https://indiehackers.com/launch"
                            ]
                        },
                        {
                            "title": "Product Scaling",
                            "level": "advanced",
                            "description": "Scale a successful product",
                            "technologies": ["Growth", "Team Building"],
                            "learning_outcomes": [
                                "Product scaling",
                                "Team management",
                                "Growth strategies"
                            ],
                            "resources": [
                                "https://producthunt.com/scale",
                                "https://indiehackers.com/scale"
                            ]
                        }
                    ]

                elif component == "A":  # Attention
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Focus & Mindfulness Basics",
                            "steps": [
                                "Understanding focus",
                                "Basic mindfulness",
                                "Digital minimalism",
                                "Time management"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Focus Techniques",
                            "steps": [
                                "Deep work",
                                "Flow state",
                                "Attention management",
                                "Productivity systems"
                            ]
                        },
                        "advanced": {
                            "title": "Mastery of Attention",
                            "steps": [
                                "Attention mastery",
                                "Focus optimization",
                                "Mindfulness leadership",
                                "Teaching focus"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "wakingup",
                                "title": "Mindfulness & Focus",
                                "url": "https://wakingup.com",
                                "level": "beginner"
                            },
                            {
                                "platform": "focusmate",
                                "title": "Deep Work",
                                "url": "https://focusmate.com",
                                "level": "intermediate"
                            }
                        ],
                        "books": [
                            {
                                "title": "Deep Work",
                                "author": "Cal Newport",
                                "url": "https://calnewport.com/books/deep-work"
                            },
                            {
                                "title": "Digital Minimalism",
                                "author": "Cal Newport",
                                "url": "https://calnewport.com/books/digital-minimalism"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "Cal Newport",
                                "url": "https://youtube.com/calnewport",
                                "focus": "Focus and productivity"
                            },
                            {
                                "name": "Thomas Frank",
                                "url": "https://youtube.com/thomasfrank",
                                "focus": "Productivity and focus"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "discord",
                                "name": "Deep Work",
                                "url": "https://discord.gg/deepwork",
                                "focus": "Focus and productivity"
                            },
                            {
                                "platform": "slack",
                                "name": "Focus Mate",
                                "url": "https://slack.focusmate.com",
                                "focus": "Accountability"
                            }
                        ],
                        "tools": [
                            {
                                "name": "Freedom",
                                "url": "https://freedom.to",
                                "purpose": "Digital distraction blocking"
                            },
                            {
                                "name": "Forest",
                                "url": "https://forestapp.cc",
                                "purpose": "Focus timer"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Digital Minimalism Challenge",
                            "level": "beginner",
                            "description": "30-day digital minimalism challenge",
                            "technologies": ["Mindfulness", "Digital Minimalism"],
                            "learning_outcomes": [
                                "Digital minimalism",
                                "Focus improvement",
                                "Productivity enhancement"
                            ],
                            "resources": [
                                "https://freedom.to/challenge",
                                "https://forestapp.cc/challenge"
                            ]
                        },
                        {
                            "title": "Deep Work Implementation",
                            "level": "intermediate",
                            "description": "Implement deep work in your routine",
                            "technologies": ["Deep Work", "Productivity"],
                            "learning_outcomes": [
                                "Deep work",
                                "Focus optimization",
                                "Productivity systems"
                            ],
                            "resources": [
                                "https://calnewport.com/deep-work",
                                "https://focusmate.com/deep-work"
                            ]
                        },
                        {
                            "title": "Focus Mastery Program",
                            "level": "advanced",
                            "description": "Create a focus mastery program",
                            "technologies": ["Focus", "Teaching"],
                            "learning_outcomes": [
                                "Focus mastery",
                                "Teaching focus",
                                "Leadership in focus"
                            ],
                            "resources": [
                                "https://calnewport.com/mastery",
                                "https://focusmate.com/mastery"
                            ]
                        }
                    ]

                elif component == "L":  # Leverage
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Systems & Automation Basics",
                            "steps": [
                                "Understanding systems",
                                "Basic automation",
                                "Workflow optimization",
                                "Efficiency improvement"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Systems & Automation",
                            "steps": [
                                "Advanced automation",
                                "Complex systems",
                                "Multi-platform integration",
                                "Strategic scaling"
                            ]
                        },
                        "advanced": {
                            "title": "Systemic Leadership",
                            "steps": [
                                "Systemic thinking",
                                "Team leadership",
                                "Strategic scaling",
                                "Innovation"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "zapier",
                                "title": "Systems & Automation",
                                "url": "https://zapier.com/learn",
                                "level": "beginner"
                            },
                            {
                                "platform": "automate",
                                "title": "Advanced Automation",
                                "url": "https://automate.io/learn",
                                "level": "intermediate"
                            }
                        ],
                        "books": [
                            {
                                "title": "The 5 Elements of Effective Thinking",
                                "author": "Edward B. Burger",
                                "url": "https://edwardburger.com/books/5-elements"
                            },
                            {
                                "title": "Systems Thinking",
                                "author": "Peter Senge",
                                "url": "https://petersenge.com/books/systems-thinking"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "Zapier",
                                "url": "https://youtube.com/zapier",
                                "focus": "Automation and productivity"
                            },
                            {
                                "name": "Automate",
                                "url": "https://youtube.com/automate",
                                "focus": "Advanced automation"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "slack",
                                "name": "Zapier",
                                "url": "https://slack.zapier.com",
                                "focus": "Automation and productivity"
                            },
                            {
                                "platform": "discord",
                                "name": "Automate",
                                "url": "https://discord.gg/automate",
                                "focus": "Advanced automation"
                            }
                        ],
                        "tools": [
                            {
                                "name": "N8N",
                                "url": "https://n8n.io",
                                "purpose": "Workflow automation"
                            },
                            {
                                "name": "Make",
                                "url": "https://make.com",
                                "purpose": "Workflow automation"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Workflow Optimization",
                            "level": "beginner",
                            "description": "Optimize your workflow",
                            "technologies": ["N8N", "Make"],
                            "learning_outcomes": [
                                "Workflow optimization",
                                "Efficiency improvement",
                                "Strategic scaling"
                            ],
                            "resources": [
                                "https://n8n.io/learn",
                                "https://make.com/learn"
                            ]
                        },
                        {
                            "title": "Multi-platform Integration",
                            "level": "intermediate",
                            "description": "Integrate systems across platforms",
                            "technologies": ["N8N", "Make"],
                            "learning_outcomes": [
                                "Multi-platform integration",
                                "Strategic scaling",
                                "Innovation"
                            ],
                            "resources": [
                                "https://n8n.io/integrations",
                                "https://make.com/integrations"
                            ]
                        },
                        {
                            "title": "Strategic Scaling",
                            "level": "advanced",
                            "description": "Scale a system effectively",
                            "technologies": ["N8N", "Make"],
                            "learning_outcomes": [
                                "Strategic scaling",
                                "Innovation",
                                "Team leadership"
                            ],
                            "resources": [
                                "https://n8n.io/scaling",
                                "https://make.com/scaling"
                            ]
                        }
                    ]

                elif component == "A":  # Algorithms
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Problem-Solving Patterns",
                            "steps": [
                                "Understanding problem-solving",
                                "Basic pattern recognition",
                                "Systematic approach",
                                "Pattern application"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Problem-Solving",
                            "steps": [
                                "Advanced pattern recognition",
                                "Complex systems",
                                "Strategic problem-solving",
                                "Innovation"
                            ]
                        },
                        "advanced": {
                            "title": "Mastery of Problem-Solving",
                            "steps": [
                                "Mastery of problem-solving",
                                "Strategic thinking",
                                "Innovation",
                                "Leadership"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "leetcode",
                                "title": "Problem-Solving Patterns",
                                "url": "https://leetcode.com/learn",
                                "level": "beginner"
                            },
                            {
                                "platform": "hackerrank",
                                "title": "Advanced Problem-Solving",
                                "url": "https://hackerrank.com/learn",
                                "level": "intermediate"
                            }
                        ],
                        "books": [
                            {
                                "title": "The Art of Problem Solving",
                                "author": "Paul Zeitz",
                                "url": "https://paulzeitz.com/books/art-of-problem-solving"
                            },
                            {
                                "title": "Algorithm Design",
                                "author": "Jon Kleinberg and Éva Tardos",
                                "url": "https://jeffe.cs.illinois.edu/book/index.html"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "LeetCode",
                                "url": "https://youtube.com/leetcode",
                                "focus": "Problem-solving and coding"
                            },
                            {
                                "name": "HackerRank",
                                "url": "https://youtube.com/hackerrank",
                                "focus": "Problem-solving and coding"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "discord",
                                "name": "LeetCode",
                                "url": "https://discord.gg/leetcode",
                                "focus": "Problem-solving and coding"
                            },
                            {
                                "platform": "slack",
                                "name": "HackerRank",
                                "url": "https://slack.hackerrank.com",
                                "focus": "Problem-solving and coding"
                            }
                        ],
                        "tools": [
                            {
                                "name": "GitHub",
                                "url": "https://github.com/algorithm-patterns",
                                "purpose": "Algorithm patterns and implementations"
                            },
                            {
                                "name": "Codewars",
                                "url": "https://codewars.com",
                                "purpose": "Problem-solving and coding challenges"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Algorithm Implementation",
                            "level": "beginner",
                            "description": "Implement a basic algorithm",
                            "technologies": ["Python", "Algorithm"],
                            "learning_outcomes": [
                                "Algorithm implementation",
                                "Coding skills",
                                "Pattern recognition"
                            ],
                            "resources": [
                                "https://github.com/algorithm-patterns",
                                "https://codewars.com"
                            ]
                        },
                        {
                            "title": "Advanced Algorithm Design",
                            "level": "intermediate",
                            "description": "Design a complex algorithm",
                            "technologies": ["Python", "Algorithm"],
                            "learning_outcomes": [
                                "Advanced algorithm design",
                                "Strategic thinking",
                                "Innovation"
                            ],
                            "resources": [
                                "https://github.com/algorithm-patterns",
                                "https://codewars.com"
                            ]
                        },
                        {
                            "title": "Algorithm Mastery",
                            "level": "advanced",
                            "description": "Master a difficult algorithm",
                            "technologies": ["Python", "Algorithm"],
                            "learning_outcomes": [
                                "Algorithm mastery",
                                "Strategic thinking",
                                "Innovation"
                            ],
                            "resources": [
                                "https://github.com/algorithm-patterns",
                                "https://codewars.com"
                            ]
                        }
                    ]

                elif component == "J":  # Joy
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Finding Purpose & Joy",
                            "steps": [
                                "Understanding purpose",
                                "Discovering joy",
                                "Purpose-driven life",
                                "Joyful living"
                            ]
                        },
                        "intermediate": {
                            "title": "Purpose & Joy in Work",
                            "steps": [
                                "Purpose in work",
                                "Joyful productivity",
                                "Purpose-driven growth",
                                "Joyful leadership"
                            ]
                        },
                        "advanced": {
                            "title": "Purpose & Joy in Life",
                            "steps": [
                                "Purpose in life",
                                "Joyful living",
                                "Purpose-driven legacy",
                                "Joyful retirement"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "masterclass",
                                "title": "Purpose & Joy",
                                "url": "https://masterclass.com/purpose",
                                "level": "beginner"
                            },
                            {
                                "platform": "udemy",
                                "title": "Purpose & Joy",
                                "url": "https://udemy.com/purpose",
                                "level": "beginner"
                            }
                        ],
                        "books": [
                            {
                                "title": "The Purpose-Driven Life",
                                "author": "Rick Warren",
                                "url": "https://rickwarren.com/books/purpose-driven-life"
                            },
                            {
                                "title": "The 7 Habits of Highly Effective People",
                                "author": "Stephen R. Covey",
                                "url": "https://stephen-covey.com/books/7-habits"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "MasterClass",
                                "url": "https://youtube.com/masterclass",
                                "focus": "Purpose and personal growth"
                            },
                            {
                                "name": "Udemy",
                                "url": "https://youtube.com/udemy",
                                "focus": "Purpose and personal growth"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "meetup",
                                "name": "Purpose & Joy",
                                "url": "https://meetup.com",
                                "focus": "Purpose and personal growth"
                            },
                            {
                                "platform": "mentorcruise",
                                "name": "Purpose & Joy",
                                "url": "https://mentorcruise.com",
                                "focus": "Purpose and personal growth"
                            }
                        ],
                        "tools": [
                            {
                                "name": "Trello",
                                "url": "https://trello.com",
                                "purpose": "Purpose-driven project management"
                            },
                            {
                                "name": "Asana",
                                "url": "https://asana.com",
                                "purpose": "Purpose-driven project management"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Purpose Project Development",
                            "level": "beginner",
                            "description": "Building a purpose-driven project",
                            "technologies": ["Project Management", "Purpose"],
                            "learning_outcomes": [
                                "Purpose-driven project",
                                "Project management",
                                "Purpose discovery"
                            ],
                            "resources": [
                                "https://kickstarter.com/learn",
                                "https://patreon.com/creator"
                            ]
                        },
                        {
                            "title": "Purpose-Driven Leadership",
                            "level": "intermediate",
                            "description": "Leading with purpose",
                            "technologies": ["Leadership", "Purpose"],
                            "learning_outcomes": [
                                "Purpose-driven leadership",
                                "Leadership",
                                "Purpose discovery"
                            ],
                            "resources": [
                                "https://linkedin.com/learning",
                                "https://skillshare.com/branding"
                            ]
                        },
                        {
                            "title": "Purpose-Driven Community",
                            "level": "advanced",
                            "description": "Building a purpose-driven community",
                            "technologies": ["Community Building", "Purpose"],
                            "learning_outcomes": [
                                "Purpose-driven community",
                                "Community building",
                                "Purpose discovery"
                            ],
                            "resources": [
                                "https://meetup.com",
                                "https://mentorcruise.com"
                            ]
                        }
                    ]

                elif component == "I":  # Influence
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Personal Branding & Leadership Basics",
                            "steps": [
                                "Understanding personal branding",
                                "Basic leadership skills",
                                "Building influence",
                                "Leadership in everyday life"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Personal Branding & Leadership",
                            "steps": [
                                "Advanced personal branding",
                                "Strategic leadership",
                                "Building influence",
                                "Leadership in professional environments"
                            ]
                        },
                        "advanced": {
                            "title": "Strategic Influence",
                            "steps": [
                                "Strategic influence",
                                "Leadership",
                                "Influence in complex environments",
                                "Strategic leadership"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "linkedin",
                                "title": "Personal Branding & Leadership",
                                "url": "https://linkedin.com/learning",
                                "level": "beginner"
                            },
                            {
                                "platform": "skillshare",
                                "title": "Branding",
                                "url": "https://skillshare.com/branding",
                                "level": "beginner"
                            }
                        ],
                        "books": [
                            {
                                "title": "The 7 Habits of Highly Effective People",
                                "author": "Stephen R. Covey",
                                "url": "https://stephen-covey.com/books/7-habits"
                            },
                            {
                                "title": "Dare to Lead",
                                "author": "Brené Brown",
                                "url": "https://brenébrown.com/books/dare-to-lead"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "LinkedIn Learning",
                                "url": "https://youtube.com/linkedinlearning",
                                "focus": "Personal branding and leadership"
                            },
                            {
                                "name": "Skillshare",
                                "url": "https://youtube.com/skillshare",
                                "focus": "Branding and personal growth"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "meetup",
                                "name": "Personal Branding & Leadership",
                                "url": "https://meetup.com",
                                "focus": "Personal branding and leadership"
                            },
                            {
                                "platform": "mentorcruise",
                                "name": "Personal Branding & Leadership",
                                "url": "https://mentorcruise.com",
                                "focus": "Personal branding and leadership"
                            }
                        ],
                        "tools": [
                            {
                                "name": "LinkedIn",
                                "url": "https://linkedin.com",
                                "purpose": "Professional networking"
                            },
                            {
                                "name": "Skillshare",
                                "url": "https://skillshare.com",
                                "purpose": "Personal branding and growth"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Personal Branding Project",
                            "level": "beginner",
                            "description": "Building a personal brand",
                            "technologies": ["LinkedIn", "Branding"],
                            "learning_outcomes": [
                                "Personal branding",
                                "Professional networking",
                                "Leadership"
                            ],
                            "resources": [
                                "https://linkedin.com",
                                "https://skillshare.com"
                            ]
                        },
                        {
                            "title": "Strategic Leadership",
                            "level": "intermediate",
                            "description": "Leading a team",
                            "technologies": ["Leadership", "Strategic"],
                            "learning_outcomes": [
                                "Strategic leadership",
                                "Team management",
                                "Leadership"
                            ],
                            "resources": [
                                "https://linkedin.com/learning",
                                "https://skillshare.com/branding"
                            ]
                        },
                        {
                            "title": "Strategic Influence",
                            "level": "advanced",
                            "description": "Influencing in a complex environment",
                            "technologies": ["Strategic", "Leadership"],
                            "learning_outcomes": [
                                "Strategic influence",
                                "Leadership",
                                "Influence"
                            ],
                            "resources": [
                                "https://linkedin.com/learning",
                                "https://skillshare.com/branding"
                            ]
                        }
                    ]

                elif component == "S":  # Skills
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Skill Development Framework",
                            "steps": [
                                "Understanding skill development",
                                "Basic skill acquisition",
                                "Systematic skill acquisition",
                                "Skill mastery"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Skill Development",
                            "steps": [
                                "Advanced skill acquisition",
                                "Complex skill application",
                                "Strategic skill development",
                                "Skill mastery"
                            ]
                        },
                        "advanced": {
                            "title": "Mastery of Skills",
                            "steps": [
                                "Mastery of skills",
                                "Strategic skill application",
                                "Innovation",
                                "Leadership"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "coursera",
                                "title": "Skill Development",
                                "url": "https://coursera.org/skills",
                                "level": "beginner"
                            },
                            {
                                "platform": "edx",
                                "title": "Skill Development",
                                "url": "https://edx.org/skills",
                                "level": "beginner"
                            }
                        ],
                        "books": [
                            {
                                "title": "The 4 Disciplines of Execution",
                                "author": "Chris McChesney",
                                "url": "https://chris-mcchesney.com/books/4-disciplines"
                            },
                            {
                                "title": "The 5 Dysfunctions of a Team",
                                "author": "Patrick Lencioni",
                                "url": "https://patrick-lencioni.com/books/5-dysfunctions"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "Coursera",
                                "url": "https://youtube.com/coursera",
                                "focus": "Skill development"
                            },
                            {
                                "name": "edX",
                                "url": "https://youtube.com/edx",
                                "focus": "Skill development"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "meetup",
                                "name": "Skill Development",
                                "url": "https://meetup.com",
                                "focus": "Skill development"
                            },
                            {
                                "platform": "mentorcruise",
                                "name": "Skill Development",
                                "url": "https://mentorcruise.com",
                                "focus": "Skill development"
                            }
                        ],
                        "tools": [
                            {
                                "name": "Skillshare",
                                "url": "https://skillshare.com",
                                "purpose": "Skill development"
                            },
                            {
                                "name": "Udemy",
                                "url": "https://udemy.com",
                                "purpose": "Skill development"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Skill Development Project",
                            "level": "beginner",
                            "description": "Develop a new skill",
                            "technologies": ["Skill Development", "Skill Acquisition"],
                            "learning_outcomes": [
                                "Skill development",
                                "Skill acquisition",
                                "Skill mastery"
                            ],
                            "resources": [
                                "https://coursera.org/skills",
                                "https://edx.org/skills"
                            ]
                        },
                        {
                            "title": "Advanced Skill Application",
                            "level": "intermediate",
                            "description": "Apply a complex skill",
                            "technologies": ["Skill Development", "Skill Application"],
                            "learning_outcomes": [
                                "Advanced skill application",
                                "Skill mastery",
                                "Strategic thinking"
                            ],
                            "resources": [
                                "https://coursera.org/skills",
                                "https://edx.org/skills"
                            ]
                        },
                        {
                            "title": "Skill Mastery",
                            "level": "advanced",
                            "description": "Master a difficult skill",
                            "technologies": ["Skill Development", "Skill Mastery"],
                            "learning_outcomes": [
                                "Skill mastery",
                                "Strategic thinking",
                                "Innovation"
                            ],
                            "resources": [
                                "https://coursera.org/skills",
                                "https://edx.org/skills"
                            ]
                        }
                    ]
        
        return recommendations

    async def assess_balajis_alignment(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Assess alignment with BALAJIS framework principles"""
        scores = analysis["component_scores"]
        total_score = sum(scores.values())
        
        if total_score == 0:
            return {
                "alignment_score": 0,
                "assessment": "No BALAJIS components detected",
                "recommendations": ["Explore interests across BALAJIS components"]
            }
        
        # Calculate alignment score (0-1, where 1 is perfectly aligned)
        normalized_scores = {k: v/total_score for k, v in scores.items()}
        ideal_distribution = 1/len(scores)
        alignment_score = 1 - sum(abs(score - ideal_distribution) for score in normalized_scores.values())
        
        # Generate assessment
        if alignment_score > 0.8:
            assessment = "Well-aligned with BALAJIS framework"
        elif alignment_score > 0.6:
            assessment = "Moderately aligned, some components could use more attention"
        else:
            assessment = "Limited alignment with BALAJIS framework, consider exploring more components"
        
        # Generate specific recommendations
        recommendations = []
        for component, score in normalized_scores.items():
            if score < ideal_distribution * 0.5:  # Significantly underrepresented
                recommendations.append(
                    f"Consider exploring more {self.balajis_components[component]['name']} related interests"
                )
        
        return {
            "alignment_score": alignment_score,
            "assessment": assessment,
            "recommendations": recommendations,
            "component_distribution": normalized_scores
        }

    async def execute(self, task: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a BALAJIS analysis task"""
        if task == "analyze_balajis":
            interests = params.get("interests", {})
            skill_level = params.get("skill_level", "beginner")
            
            # Step 1: Analyze BALAJIS components
            analysis = await self.analyze_balajis_components(interests)
            
            # Step 2: Generate recommendations
            recommendations = await self.generate_balajis_recommendations(analysis, skill_level)
            
            # Step 3: Assess alignment
            alignment = await self.assess_balajis_alignment(analysis)
            
            return {
                "analysis": analysis,
                "recommendations": recommendations,
                "alignment_assessment": alignment
            }
        
        raise ValueError(f"Unknown task: {task}") 