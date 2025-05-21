// Twitter API integration for analyzing user posts
import axios from 'axios';

// Function to fetch user tweets
export async function fetchUserTweets(username, count = 100) {
  try {
    // This would use Twitter API v2 with proper authentication
    // For implementation, you'll need a Twitter Developer account and API keys
    const response = await axios.get(`/api/twitter/${username}?count=${count}`);
    return response.data;
  } catch (error) {
    console.error('Error fetching tweets:', error);
    return [];
  }
}

// Function to analyze tweets for interests and goals
export async function analyzeTweets(tweets) {
  try {
    // This would call an AI service to analyze the tweets
    const response = await axios.post('/api/analyze/tweets', { tweets });
    return response.data;
  } catch (error) {
    console.error('Error analyzing tweets:', error);
    return {
      interests: [],
      goals: [],
      passions: []
    };
  }
}

// Function to extract key topics from tweets
export function extractTopics(tweets) {
  // This is a simplified version - would be replaced with NLP processing
  const topics = {};
  
  tweets.forEach(tweet => {
    const text = tweet.text.toLowerCase();
    
    // Check for BRAVED topics
    if (text.includes('bitcoin') || text.includes('crypto') || text.includes('btc'))
      topics.bitcoin = (topics.bitcoin || 0) + 1;
      
    if (text.includes('nft') || text.includes('web3') || text.includes('gaming'))
      topics.nft = (topics.nft || 0) + 1;
      
    if (text.includes('ai') || text.includes('artificial intelligence') || text.includes('prompt'))
      topics.ai = (topics.ai || 0) + 1;
      
    if (text.includes('vr') || text.includes('ar') || text.includes('metaverse'))
      topics.vr = (topics.vr || 0) + 1;
      
    if (text.includes('emotional') || text.includes('eq') || text.includes('intelligence'))
      topics.emotional = (topics.emotional || 0) + 1;
      
    if (text.includes('defi') || text.includes('decentralization') || text.includes('blockchain'))
      topics.decentralization = (topics.decentralization || 0) + 1;
  });
  
  return Object.entries(topics)
    .sort((a, b) => b[1] - a[1])
    .map(([topic]) => topic);
} 