from agno import Agent, Tool
from typing import Dict, Any, List
import json

class BRAVEDAnalysisAgent(Agent):
    def __init__(self):
        super().__init__(
            name="BRAVEDAnalysisAgent",
            description="Agent responsible for applying the BRAVED framework to learning analysis",
            tools=[
                Tool(
                    name="analyze_braved_components",
                    description="Analyze user interests through BRAVED framework",
                    function=self.analyze_braved_components
                ),
                Tool(
                    name="generate_braved_recommendations",
                    description="Generate recommendations based on BRAVED analysis",
                    function=self.generate_braved_recommendations
                ),
                Tool(
                    name="assess_braved_balance",
                    description="Assess the balance of BRAVED components in user's interests",
                    function=self.assess_braved_balance
                )
            ]
        )
        
        # BRAVED framework components with correct definitions
        self.braved_components = {
            "B": {
                "name": "Bitcoin & Cryptocurrency",
                "keywords": ["bitcoin", "crypto", "blockchain", "digital assets", "trading", "defi", "web3"],
                "description": "Understanding Bitcoin, cryptocurrency markets, and digital asset fundamentals"
            },
            "R": {
                "name": "Real World Assets & Web3 Gaming",
                "keywords": ["nft", "gaming", "real estate", "entertainment", "digital ownership", "web3 gaming", "metaverse"],
                "description": "Real world asset tokenization, NFTs, and Web3 gaming ecosystems"
            },
            "A": {
                "name": "AI & AI Agents",
                "keywords": ["artificial intelligence", "ai agents", "prompting", "machine learning", "automation", "ai tools"],
                "description": "AI technologies, agent systems, and effective AI prompting techniques"
            },
            "V": {
                "name": "VR/AR & Spatial Computing",
                "keywords": ["virtual reality", "augmented reality", "spatial computing", "metaverse", "3d", "immersive"],
                "description": "Virtual and augmented reality technologies, spatial computing, and metaverse development"
            },
            "E": {
                "name": "Emotional Intelligence",
                "keywords": ["trading psychology", "work-life balance", "emotional control", "mindfulness", "stress management"],
                "description": "Emotional intelligence in trading, work-life balance, and personal development"
            },
            "D": {
                "name": "Decentralization & Cryptography",
                "keywords": ["decentralization", "cryptography", "zero knowledge", "zk proofs", "privacy", "security"],
                "description": "Decentralized systems, cryptography, and zero-knowledge proof technologies"
            }
        }

    async def analyze_braved_components(self, interests: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze interests through the BRAVED framework"""
        analysis = {component: 0 for component in self.braved_components.keys()}
        component_details = {}
        
        for category, data in interests.items():
            if not data.get("primary_interest"):
                continue
                
            interest = data["primary_interest"].lower()
            for component, info in self.braved_components.items():
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

    async def generate_braved_recommendations(self, 
                                           analysis: Dict[str, Any], 
                                           skill_level: str = "beginner") -> Dict[str, Any]:
        """Generate recommendations based on BRAVED analysis"""
        recommendations = {}
        
        for component, score in analysis["component_scores"].items():
            if score > 0:
                component_info = self.braved_components[component]
                recommendations[component] = {
                    "name": component_info["name"],
                    "description": component_info["description"],
                    "current_score": score,
                    "learning_path": {},
                    "resources": {},
                    "projects": []
                }

                # Component-specific recommendations
                if component == "B":  # Bitcoin & Cryptocurrency
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Crypto Fundamentals",
                            "steps": [
                                "Understanding blockchain basics",
                                "Bitcoin whitepaper study",
                                "Wallet setup and security",
                                "Basic trading concepts"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Trading & DeFi",
                            "steps": [
                                "Technical analysis",
                                "DeFi protocols",
                                "Yield farming",
                                "Smart contract basics"
                            ]
                        },
                        "advanced": {
                            "title": "Professional Trading & Development",
                            "steps": [
                                "Algorithmic trading",
                                "Smart contract development",
                                "Protocol design",
                                "Security auditing"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "udemy",
                                "title": "Complete Cryptocurrency Course",
                                "url": "https://udemy.com/crypto-fundamentals",
                                "level": "beginner"
                            },
                            {
                                "platform": "coursera",
                                "title": "Blockchain Specialization",
                                "url": "https://coursera.org/blockchain",
                                "level": "intermediate"
                            }
                        ],
                        "books": [
                            {
                                "title": "The Bitcoin Standard",
                                "author": "Saifedean Ammous",
                                "url": "https://saifedean.com/book"
                            },
                            {
                                "title": "Mastering Bitcoin",
                                "author": "Andreas Antonopoulos",
                                "url": "https://github.com/bitcoinbook/bitcoinbook"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "Andreas Antonopoulos",
                                "url": "https://youtube.com/aantonop",
                                "focus": "Bitcoin education"
                            },
                            {
                                "name": "Coin Bureau",
                                "url": "https://youtube.com/coinbureau",
                                "focus": "Crypto analysis"
                            }
                        ],
                        "podcasts": [
                            {
                                "name": "What Bitcoin Did",
                                "url": "https://whatbitcoindid.com",
                                "focus": "Bitcoin interviews"
                            },
                            {
                                "name": "Unchained",
                                "url": "https://unchained.com",
                                "focus": "Crypto news and analysis"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "discord",
                                "name": "Bitcoin Beginners",
                                "url": "https://discord.gg/bitcoin",
                                "focus": "Learning and support"
                            },
                            {
                                "platform": "telegram",
                                "name": "Crypto Traders",
                                "url": "https://t.me/cryptotraders",
                                "focus": "Trading discussion"
                            }
                        ],
                        "tools": [
                            {
                                "name": "TradingView",
                                "url": "https://tradingview.com",
                                "purpose": "Technical analysis"
                            },
                            {
                                "name": "CoinGecko",
                                "url": "https://coingecko.com",
                                "purpose": "Market data"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Crypto Portfolio Tracker",
                            "level": "beginner",
                            "description": "Build a web application to track cryptocurrency portfolios",
                            "technologies": ["React", "Node.js", "CoinGecko API"],
                            "learning_outcomes": [
                                "API integration",
                                "Data visualization",
                                "Portfolio management"
                            ],
                            "resources": [
                                "https://github.com/portfolio-tracker",
                                "https://coingecko.com/api"
                            ]
                        },
                        {
                            "title": "DeFi Yield Optimizer",
                            "level": "intermediate",
                            "description": "Create a tool to find and optimize DeFi yield opportunities",
                            "technologies": ["Solidity", "Web3.js", "Ethers.js"],
                            "learning_outcomes": [
                                "Smart contract interaction",
                                "Yield calculation",
                                "Risk assessment"
                            ],
                            "resources": [
                                "https://github.com/defi-yield",
                                "https://ethereum.org/developers"
                            ]
                        },
                        {
                            "title": "Automated Trading Bot",
                            "level": "advanced",
                            "description": "Develop an algorithmic trading bot with risk management",
                            "technologies": ["Python", "CCXT", "Pandas"],
                            "learning_outcomes": [
                                "Algorithmic trading",
                                "Risk management",
                                "Backtesting"
                            ],
                            "resources": [
                                "https://github.com/trading-bot",
                                "https://ccxt.trade"
                            ]
                        }
                    ]

                elif component == "R":  # Real World Assets & Web3 Gaming
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "NFT & Web3 Gaming Basics",
                            "steps": [
                                "Understanding NFTs",
                                "Web3 wallet setup",
                                "Basic game mechanics",
                                "Digital asset ownership"
                            ]
                        },
                        "intermediate": {
                            "title": "Game Development & NFT Creation",
                            "steps": [
                                "Unity/Unreal basics",
                                "Smart contract development",
                                "NFT marketplace integration",
                                "Game economy design"
                            ]
                        },
                        "advanced": {
                            "title": "Advanced Game Development",
                            "steps": [
                                "Complex game mechanics",
                                "Token economics",
                                "Cross-chain integration",
                                "Community building"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "buildspace",
                                "title": "NFT & Web3 Game Development",
                                "url": "https://buildspace.so",
                                "level": "beginner"
                            },
                            {
                                "platform": "learnweb3",
                                "title": "Advanced Web3 Gaming",
                                "url": "https://learnweb3.io",
                                "level": "intermediate"
                            }
                        ],
                        "books": [
                            {
                                "title": "The NFT Handbook",
                                "author": "QuHarrison Terry",
                                "url": "https://nftbook.com"
                            },
                            {
                                "title": "Web3 Game Development",
                                "author": "Various Authors",
                                "url": "https://web3gamedev.com"
                            }
                        ],
                        "youtube_channels": [
                            {
                                "name": "Dapp University",
                                "url": "https://youtube.com/dappuniversity",
                                "focus": "Web3 development"
                            },
                            {
                                "name": "NFT Evening",
                                "url": "https://youtube.com/nftevening",
                                "focus": "NFT news and trends"
                            }
                        ],
                        "communities": [
                            {
                                "platform": "discord",
                                "name": "Web3 Gaming Guild",
                                "url": "https://discord.gg/web3gaming",
                                "focus": "Game development"
                            },
                            {
                                "platform": "telegram",
                                "name": "NFT Creators",
                                "url": "https://t.me/nftcreators",
                                "focus": "NFT creation"
                            }
                        ],
                        "tools": [
                            {
                                "name": "Unity",
                                "url": "https://unity.com",
                                "purpose": "Game development"
                            },
                            {
                                "name": "OpenSea",
                                "url": "https://opensea.io",
                                "purpose": "NFT marketplace"
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "NFT Collection Creator",
                            "level": "beginner",
                            "description": "Create and deploy an NFT collection",
                            "technologies": ["Solidity", "IPFS", "OpenSea"],
                            "learning_outcomes": [
                                "NFT standards",
                                "Metadata creation",
                                "Marketplace integration"
                            ],
                            "resources": [
                                "https://github.com/nft-creator",
                                "https://docs.opensea.io"
                            ]
                        },
                        {
                            "title": "Web3 Game Prototype",
                            "level": "intermediate",
                            "description": "Develop a simple blockchain-based game",
                            "technologies": ["Unity", "Web3.js", "Solidity"],
                            "learning_outcomes": [
                                "Game development",
                                "Smart contract integration",
                                "Asset tokenization"
                            ],
                            "resources": [
                                "https://github.com/web3-game",
                                "https://unity.com/learn"
                            ]
                        },
                        {
                            "title": "Cross-chain Game Economy",
                            "level": "advanced",
                            "description": "Build a game with assets across multiple chains",
                            "technologies": ["Rust", "Substrate", "Polkadot"],
                            "learning_outcomes": [
                                "Cross-chain development",
                                "Token economics",
                                "Scalability solutions"
                            ],
                            "resources": [
                                "https://github.com/cross-chain-game",
                                "https://substrate.dev"
                            ]
                        }
                    ]

                elif component == "A":  # AI & AI Agents
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "AI Basics",
                            "steps": [
                                "Understanding AI fundamentals",
                                "AI applications in business",
                                "AI in personal life",
                                "AI in education"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced AI Techniques",
                            "steps": [
                                "Deep learning",
                                "Natural language processing",
                                "Computer vision",
                                "AI ethics"
                            ]
                        },
                        "advanced": {
                            "title": "AI in Industry",
                            "steps": [
                                "AI in manufacturing",
                                "AI in healthcare",
                                "AI in finance",
                                "AI in agriculture"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "promptbase",
                                "title": "AI Prompting Techniques",
                                "url": "https://promptbase.com",
                                "level": "beginner"
                            },
                            {
                                "platform": "learnprompting",
                                "title": "Advanced AI Prompting",
                                "url": "https://learnprompting.org",
                                "level": "intermediate"
                            }
                        ],
                        "projects": [
                            {
                                "title": "AI Agent Development",
                                "level": "beginner",
                                "description": "Building and deploying AI agents",
                                "technologies": ["Python", "Hugging Face"],
                                "learning_outcomes": [
                                    "AI model understanding",
                                    "Agent development",
                                    "Deployment"
                                ],
                                "resources": [
                                    "https://github.com/features/ai",
                                    "https://huggingface.co"
                                ]
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "AI Project Proposal",
                            "level": "beginner",
                            "description": "Propose an AI project for your business",
                            "technologies": ["AI", "Business Analysis"],
                            "learning_outcomes": [
                                "Project proposal",
                                "Business case",
                                "AI integration"
                            ],
                            "resources": [
                                "https://example.com/ai-project-proposal"
                            ]
                        },
                        {
                            "title": "AI in Healthcare",
                            "level": "intermediate",
                            "description": "Implement AI in a healthcare setting",
                            "technologies": ["AI", "Healthcare"],
                            "learning_outcomes": [
                                "AI application",
                                "Healthcare integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/ai-healthcare"
                            ]
                        },
                        {
                            "title": "AI in Finance",
                            "level": "advanced",
                            "description": "Implement AI in a financial setting",
                            "technologies": ["AI", "Finance"],
                            "learning_outcomes": [
                                "AI application",
                                "Financial integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/ai-finance"
                            ]
                        }
                    ]

                elif component == "V":  # VR/AR & Spatial Computing
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "VR/AR Basics",
                            "steps": [
                                "Understanding VR/AR technology",
                                "VR/AR applications",
                                "VR/AR in personal life",
                                "VR/AR in education"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced VR/AR Development",
                            "steps": [
                                "VR/AR in industry",
                                "VR/AR in healthcare",
                                "VR/AR in gaming",
                                "VR/AR in architecture"
                            ]
                        },
                        "advanced": {
                            "title": "VR/AR in Metaverse",
                            "steps": [
                                "VR/AR in metaverse development",
                                "VR/AR in cross-chain integration",
                                "VR/AR in AI",
                                "VR/AR in AI agents"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "unity",
                                "title": "VR/AR Development",
                                "url": "https://unity.com/learn",
                                "level": "beginner"
                            },
                            {
                                "platform": "unreal",
                                "title": "VR/AR Development",
                                "url": "https://unrealengine.com/learn",
                                "level": "intermediate"
                            }
                        ],
                        "projects": [
                            {
                                "title": "Metaverse Development",
                                "level": "beginner",
                                "description": "Building in virtual worlds",
                                "technologies": ["Unity", "Unreal", "DeFi"],
                                "learning_outcomes": [
                                    "VR/AR integration",
                                    "Metaverse development",
                                    "Cross-chain integration"
                                ],
                                "resources": [
                                    "https://docs.decentraland.org",
                                    "https://spatial.io/developers"
                                ]
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "VR/AR Project Proposal",
                            "level": "beginner",
                            "description": "Propose a VR/AR project for your business",
                            "technologies": ["VR/AR", "Business Analysis"],
                            "learning_outcomes": [
                                "Project proposal",
                                "VR/AR integration",
                                "Business case"
                            ],
                            "resources": [
                                "https://example.com/vr-ar-project-proposal"
                            ]
                        },
                        {
                            "title": "VR/AR in Healthcare",
                            "level": "intermediate",
                            "description": "Implement VR/AR in a healthcare setting",
                            "technologies": ["VR/AR", "Healthcare"],
                            "learning_outcomes": [
                                "VR/AR integration",
                                "Healthcare integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/vr-ar-healthcare"
                            ]
                        },
                        {
                            "title": "VR/AR in Gaming",
                            "level": "advanced",
                            "description": "Implement VR/AR in a gaming setting",
                            "technologies": ["VR/AR", "Gaming"],
                            "learning_outcomes": [
                                "VR/AR integration",
                                "Gaming integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/vr-ar-gaming"
                            ]
                        }
                    ]

                elif component == "E":  # Emotional Intelligence
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Emotional Intelligence Basics",
                            "steps": [
                                "Understanding emotional intelligence",
                                "Emotional intelligence in personal life",
                                "Emotional intelligence in business",
                                "Emotional intelligence in education"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Emotional Intelligence",
                            "steps": [
                                "Emotional intelligence in personal development",
                                "Emotional intelligence in business development",
                                "Emotional intelligence in healthcare",
                                "Emotional intelligence in finance"
                            ]
                        },
                        "advanced": {
                            "title": "Emotional Intelligence in Metaverse",
                            "steps": [
                                "Emotional intelligence in metaverse development",
                                "Emotional intelligence in cross-chain integration",
                                "Emotional intelligence in AI",
                                "Emotional intelligence in AI agents"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "tradingview",
                                "title": "Trading Psychology",
                                "url": "https://tradingview.com/education",
                                "level": "beginner"
                            },
                            {
                                "platform": "babypips",
                                "title": "Trading Psychology",
                                "url": "https://babypips.com/learn",
                                "level": "beginner"
                            }
                        ],
                        "projects": [
                            {
                                "title": "Mindfulness & Work-Life Balance",
                                "level": "beginner",
                                "description": "Developing emotional resilience",
                                "technologies": ["Mindfulness", "Work-Life Balance"],
                                "learning_outcomes": [
                                    "Emotional resilience",
                                    "Work-Life balance",
                                    "Personal development"
                                ],
                                "resources": [
                                    "https://headspace.com",
                                    "https://calm.com"
                                ]
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Emotional Intelligence Project",
                            "level": "beginner",
                            "description": "Implement emotional intelligence in your business",
                            "technologies": ["Emotional Intelligence", "Business"],
                            "learning_outcomes": [
                                "Emotional intelligence",
                                "Business integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/emotional-intelligence-business"
                            ]
                        },
                        {
                            "title": "Emotional Intelligence in Healthcare",
                            "level": "intermediate",
                            "description": "Implement emotional intelligence in a healthcare setting",
                            "technologies": ["Emotional Intelligence", "Healthcare"],
                            "learning_outcomes": [
                                "Emotional intelligence",
                                "Healthcare integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/emotional-intelligence-healthcare"
                            ]
                        },
                        {
                            "title": "Emotional Intelligence in Finance",
                            "level": "advanced",
                            "description": "Implement emotional intelligence in a financial setting",
                            "technologies": ["Emotional Intelligence", "Finance"],
                            "learning_outcomes": [
                                "Emotional intelligence",
                                "Finance integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/emotional-intelligence-finance"
                            ]
                        }
                    ]

                elif component == "D":  # Decentralization & Cryptography
                    # Learning Path
                    recommendations[component]["learning_path"] = {
                        "beginner": {
                            "title": "Decentralization Basics",
                            "steps": [
                                "Understanding decentralized systems",
                                "Decentralization in personal life",
                                "Decentralization in business",
                                "Decentralization in education"
                            ]
                        },
                        "intermediate": {
                            "title": "Advanced Decentralization",
                            "steps": [
                                "Decentralization in industry",
                                "Decentralization in healthcare",
                                "Decentralization in finance",
                                "Decentralization in gaming"
                            ]
                        },
                        "advanced": {
                            "title": "Decentralization in Metaverse",
                            "steps": [
                                "Decentralization in metaverse development",
                                "Decentralization in cross-chain integration",
                                "Decentralization in AI",
                                "Decentralization in AI agents"
                            ]
                        }
                    }
                    
                    # Resources
                    recommendations[component]["resources"] = {
                        "courses": [
                            {
                                "platform": "cryptozombies",
                                "title": "Cryptography Basics",
                                "url": "https://cryptozombies.io",
                                "level": "beginner"
                            },
                            {
                                "platform": "ethereum",
                                "title": "Ethereum Developer",
                                "url": "https://ethereum.org/developers",
                                "level": "intermediate"
                            }
                        ],
                        "projects": [
                            {
                                "title": "ZK Proof Development",
                                "level": "beginner",
                                "description": "Building privacy-preserving applications",
                                "technologies": ["ZK Proofs", "Solidity"],
                                "learning_outcomes": [
                                    "Privacy-preserving applications",
                                    "ZK Proof development",
                                    "Smart contract interaction"
                                ],
                                "resources": [
                                    "https://github.com/zkproofs",
                                    "https://docs.zksync.io"
                                ]
                            }
                        ]
                    }
                    
                    # Projects
                    recommendations[component]["projects"] = [
                        {
                            "title": "Decentralization Project",
                            "level": "beginner",
                            "description": "Implement decentralized systems in your business",
                            "technologies": ["Decentralization", "Business"],
                            "learning_outcomes": [
                                "Decentralization",
                                "Business integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/decentralization-business"
                            ]
                        },
                        {
                            "title": "Decentralization in Healthcare",
                            "level": "intermediate",
                            "description": "Implement decentralized systems in a healthcare setting",
                            "technologies": ["Decentralization", "Healthcare"],
                            "learning_outcomes": [
                                "Decentralization",
                                "Healthcare integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/decentralization-healthcare"
                            ]
                        },
                        {
                            "title": "Decentralization in Finance",
                            "level": "advanced",
                            "description": "Implement decentralized systems in a financial setting",
                            "technologies": ["Decentralization", "Finance"],
                            "learning_outcomes": [
                                "Decentralization",
                                "Finance integration",
                                "AI ethics"
                            ],
                            "resources": [
                                "https://example.com/decentralization-finance"
                            ]
                        }
                    ]
        
        return recommendations

    async def assess_braved_balance(self, analysis: Dict[str, Any]) -> Dict[str, Any]:
        """Assess the balance of BRAVED components in user's interests"""
        scores = analysis["component_scores"]
        total_score = sum(scores.values())
        
        if total_score == 0:
            return {
                "balance_score": 0,
                "assessment": "No BRAVED components detected",
                "recommendations": ["Explore interests across all BRAVED components"]
            }
        
        # Calculate balance score (0-1, where 1 is perfectly balanced)
        normalized_scores = {k: v/total_score for k, v in scores.items()}
        ideal_balance = 1/len(scores)
        balance_score = 1 - sum(abs(score - ideal_balance) for score in normalized_scores.values())
        
        # Generate assessment
        if balance_score > 0.8:
            assessment = "Well-balanced across BRAVED components"
        elif balance_score > 0.6:
            assessment = "Moderately balanced, some components could use more attention"
        else:
            assessment = "Heavily focused on specific components, consider diversifying"
        
        # Generate specific recommendations
        recommendations = []
        for component, score in normalized_scores.items():
            if score < ideal_balance * 0.5:  # Significantly underrepresented
                recommendations.append(
                    f"Consider exploring more {self.braved_components[component]['name']} related interests"
                )
        
        return {
            "balance_score": balance_score,
            "assessment": assessment,
            "recommendations": recommendations,
            "component_distribution": normalized_scores
        }

    async def execute(self, task: str, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a BRAVED analysis task"""
        if task == "analyze_braved":
            interests = params.get("interests", {})
            skill_level = params.get("skill_level", "beginner")
            
            # Step 1: Analyze BRAVED components
            analysis = await self.analyze_braved_components(interests)
            
            # Step 2: Generate recommendations
            recommendations = await self.generate_braved_recommendations(analysis, skill_level)
            
            # Step 3: Assess balance
            balance = await self.assess_braved_balance(analysis)
            
            return {
                "analysis": analysis,
                "recommendations": recommendations,
                "balance_assessment": balance
            }
        
        raise ValueError(f"Unknown task: {task}") 