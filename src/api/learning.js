// Learning content generator API
import axios from 'axios';

// BRAVED topics
const BRAVED_TOPICS = {
  B: {
    name: 'Bitcoin & Cryptocurrency',
    subtopics: ['Bitcoin basics', 'Cryptocurrency markets', 'Blockchain fundamentals', 'DeFi']
  },
  R: {
    name: 'Real world assets & NFTs',
    subtopics: ['Tokenization', 'Digital collectibles', 'NFT marketplaces', 'Digital ownership']
  },
  A: {
    name: 'AI & AI Agents',
    subtopics: ['AI fundamentals', 'Prompt engineering', 'AI agents', 'Machine learning basics']
  },
  V: {
    name: 'VR/AR & Spatial Computing',
    subtopics: ['VR basics', 'AR applications', 'Metaverse concepts', 'Spatial design']
  },
  E: {
    name: 'Emotional Intelligence',
    subtopics: ['Self-awareness', 'Empathy', 'Social skills', 'Relationship management']
  },
  D: {
    name: 'Decentralization & Cryptography',
    subtopics: ['Decentralized systems', 'Cryptographic principles', 'Zero-knowledge proofs', 'Privacy tech']
  }
};

// BALAJIS framework
const BALAJIS_FRAMEWORK = {
  B: {
    name: 'Build',
    skills: ['Product development', 'Technical skills', 'Project management', 'Innovation']
  },
  A: {
    name: 'Attention',
    skills: ['Focus techniques', 'Mindfulness', 'Deep work', 'Distraction management']
  },
  L: {
    name: 'Leverage',
    skills: ['Resource optimization', 'Network effects', 'Strategic partnerships', 'Scaling']
  },
  A2: {
    name: 'Algorithms',
    skills: ['Computational thinking', 'Systems design', 'Data structures', 'Problem-solving']
  },
  J: {
    name: 'Joy',
    skills: ['Finding purpose', 'Work-life harmony', 'Flow states', 'Meaningful creation']
  },
  I: {
    name: 'Influence',
    skills: ['Communication', 'Leadership', 'Community building', 'Personal branding']
  },
  S: {
    name: 'Skills',
    skills: ['Continuous learning', 'Skill acquisition', 'Knowledge management', 'Expertise building']
  }
};

// Generate personalized learning path based on user interests
export async function generateLearningPath(userInterests, userGoals) {
  try {
    // This would call an AI service to generate personalized content
    const response = await axios.post('/api/generate/learning-path', {
      interests: userInterests,
      goals: userGoals,
      frameworks: {
        BRAVED: BRAVED_TOPICS,
        BALAJIS: BALAJIS_FRAMEWORK
      }
    });
    
    return response.data;
  } catch (error) {
    console.error('Error generating learning path:', error);
    
    // Fallback to basic recommendation
    return generateBasicLearningPath(userInterests);
  }
}

// Generate basic learning content without AI service
function generateBasicLearningPath(userInterests) {
  const learningPath = [];
  
  // Map user interests to BRAVED topics
  const bravedTopics = Object.entries(BRAVED_TOPICS)
    .filter(([_, topic]) => 
      userInterests.some(interest => 
        topic.name.toLowerCase().includes(interest.toLowerCase()) ||
        topic.subtopics.some(subtopic => 
          subtopic.toLowerCase().includes(interest.toLowerCase())
        )
      )
    )
    .map(([key, topic]) => ({ key, ...topic }));
  
  // Create daily lessons
  for (let i = 0; i < 7; i++) {
    const topicIndex = i % bravedTopics.length;
    const topic = bravedTopics[topicIndex];
    
    if (topic) {
      const subtopicIndex = Math.floor(i / bravedTopics.length) % topic.subtopics.length;
      const subtopic = topic.subtopics[subtopicIndex];
      
      // Match with a BALAJIS skill
      const balajisKeys = Object.keys(BALAJIS_FRAMEWORK);
      const balajisKey = balajisKeys[i % balajisKeys.length];
      const balajisSkill = BALAJIS_FRAMEWORK[balajisKey];
      
      learningPath.push({
        day: i + 1,
        topic: topic.name,
        subtopic,
        balajisSkill: balajisSkill.name,
        balajisSkillDetail: balajisSkill.skills[i % balajisSkill.skills.length],
        content: `Learn about ${subtopic} in the context of ${topic.name}, while developing your ${balajisSkill.name} skills through ${balajisSkill.skills[i % balajisSkill.skills.length]}.`,
        exercises: [
          `Research one real-world application of ${subtopic}`,
          `Practice ${balajisSkill.skills[i % balajisSkill.skills.length]} by applying it to ${subtopic}`,
          `Reflect on how this knowledge reduces materialistic thinking`
        ]
      });
    }
  }
  
  return {
    personalizedPath: learningPath,
    message: "Here's your personalized learning path combining BRAVED topics with BALAJIS skills."
  };
}

// Generate gamified daily challenge
export function generateDailyChallenge(userProfile) {
  const { interests, completedLessons, level } = userProfile;
  
  // Select a BRAVED topic based on interests and lesson history
  const availableTopics = Object.entries(BRAVED_TOPICS)
    .filter(([_, topic]) => 
      interests.some(interest => 
        topic.name.toLowerCase().includes(interest.toLowerCase())
      )
    )
    .map(([key, topic]) => ({ key, ...topic }));
  
  // Select topic with lowest completion rate
  const selectedTopic = availableTopics[0] || Object.values(BRAVED_TOPICS)[0];
  
  // Select a BALAJIS skill to incorporate
  const balajisSkill = BALAJIS_FRAMEWORK.B; // Default to Build
  
  return {
    title: `${selectedTopic.name} Challenge`,
    description: `Apply ${balajisSkill.name} principles to learn about ${selectedTopic.subtopics[0]}`,
    xpReward: 50 * (level || 1),
    timeEstimate: '10 minutes',
    steps: [
      `Read a short article about ${selectedTopic.subtopics[0]}`,
      `Complete a quick quiz to test your understanding`,
      `Apply what you've learned by completing a mini-project`
    ]
  };
} 