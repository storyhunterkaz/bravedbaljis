// User profile management API
import axios from 'axios';

// User profile structure
const defaultUserProfile = {
  id: null,
  username: '',
  email: '',
  twitterHandle: '',
  interests: [],
  goals: [],
  passions: [],
  learningPath: [],
  completedLessons: [],
  level: 1,
  xp: 0,
  streak: 0,
  lastActive: null,
  bravedScores: {
    bitcoin: 0,
    realWorldAssets: 0,
    ai: 0,
    vr: 0,
    emotionalIntelligence: 0,
    decentralization: 0
  },
  balajisScores: {
    build: 0,
    attention: 0,
    leverage: 0,
    algorithms: 0,
    joy: 0,
    influence: 0,
    skills: 0
  }
};

// Get user profile
export async function getUserProfile(userId) {
  try {
    const response = await axios.get(`/api/users/${userId}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user profile:', error);
    return { ...defaultUserProfile, id: userId };
  }
}

// Update user profile
export async function updateUserProfile(userId, profileData) {
  try {
    const response = await axios.put(`/api/users/${userId}`, profileData);
    return response.data;
  } catch (error) {
    console.error('Error updating user profile:', error);
    return null;
  }
}

// Update user interests based on social media analysis
export async function updateUserInterests(userId, interests) {
  try {
    const response = await axios.patch(`/api/users/${userId}/interests`, { interests });
    return response.data;
  } catch (error) {
    console.error('Error updating user interests:', error);
    return null;
  }
}

// Track completed lesson
export async function trackCompletedLesson(userId, lessonId) {
  try {
    const response = await axios.post(`/api/users/${userId}/lessons/${lessonId}/complete`);
    return response.data;
  } catch (error) {
    console.error('Error tracking completed lesson:', error);
    return null;
  }
}

// Calculate user level based on XP
export function calculateLevel(xp) {
  // Simple level calculation: each level requires 100 * level XP
  return Math.floor(Math.sqrt(xp / 50)) + 1;
}

// Update user streak
export async function updateStreak(userId) {
  try {
    const today = new Date().toISOString().split('T')[0];
    const response = await axios.post(`/api/users/${userId}/streak`, { date: today });
    return response.data;
  } catch (error) {
    console.error('Error updating streak:', error);
    return null;
  }
}

// Get user learning stats
export async function getUserStats(userId) {
  try {
    const response = await axios.get(`/api/users/${userId}/stats`);
    return response.data;
  } catch (error) {
    console.error('Error fetching user stats:', error);
    return {
      lessonsCompleted: 0,
      topicsExplored: 0,
      currentStreak: 0,
      longestStreak: 0,
      topSkill: null
    };
  }
} 