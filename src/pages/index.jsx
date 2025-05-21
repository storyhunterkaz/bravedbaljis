import React, { useState, useEffect } from 'react';
import { getUserProfile } from '../api/user';
import Dashboard from '../components/Dashboard';
import TwitterAnalyzer from '../components/TwitterAnalyzer';

const Home = () => {
  const [userId, setUserId] = useState(null);
  const [userProfile, setUserProfile] = useState(null);
  const [loading, setLoading] = useState(true);
  const [showAnalyzer, setShowAnalyzer] = useState(false);
  
  useEffect(() => {
    // Simulate user authentication
    // In a real app, this would come from your auth system
    const mockUserId = 'user-123';
    setUserId(mockUserId);
    
    const loadUserProfile = async () => {
      try {
        setLoading(true);
        const profile = await getUserProfile(mockUserId);
        setUserProfile(profile);
        
        // Show analyzer if user has no interests or learning path
        if (!profile.interests || profile.interests.length === 0 || 
            !profile.learningPath || profile.learningPath.length === 0) {
          setShowAnalyzer(true);
        }
      } catch (error) {
        console.error('Error loading user profile:', error);
      } finally {
        setLoading(false);
      }
    };
    
    loadUserProfile();
  }, []);
  
  const handleAnalysisComplete = () => {
    setShowAnalyzer(false);
    // Refresh user profile
    getUserProfile(userId).then(setUserProfile);
  };
  
  if (loading) {
    return (
      <div className="loading-screen">
        <div className="loading-animation"></div>
        <p>Loading your personalized learning experience...</p>
      </div>
    );
  }
  
  return (
    <div className="app">
      <header className="app-header">
        <div className="logo">
          <h1>BRAVED BALAJIS</h1>
          <p>Beyond materialism, toward meaningful growth</p>
        </div>
        <nav className="main-nav">
          <ul>
            <li><a href="#" className="active">Dashboard</a></li>
            <li><a href="#">Lessons</a></li>
            <li><a href="#">Resources</a></li>
            <li><a href="#">Community</a></li>
          </ul>
        </nav>
        <div className="user-menu">
          <span className="username">{userProfile?.username || 'User'}</span>
          <div className="avatar">
            <img src="/avatar-placeholder.png" alt="User avatar" />
          </div>
        </div>
      </header>
      
      <main className="app-main">
        {showAnalyzer ? (
          <div className="analyzer-container">
            <div className="analyzer-intro">
              <h2>Welcome to Your Learning Journey</h2>
              <p>
                Let's start by understanding your interests and goals.
                Connect your Twitter account to help us create a personalized
                learning path that aligns with your passions.
              </p>
            </div>
            <TwitterAnalyzer 
              userId={userId} 
              onAnalysisComplete={handleAnalysisComplete} 
            />
          </div>
        ) : (
          <Dashboard userId={userId} />
        )}
      </main>
      
      <footer className="app-footer">
        <div className="footer-content">
          <div className="footer-section">
            <h3>About BRAVED BALAJIS</h3>
            <p>
              An educational platform designed to help you develop skills and knowledge
              that transcend materialism, focusing on lasting growth and value creation.
            </p>
          </div>
          <div className="footer-section">
            <h3>Quick Links</h3>
            <ul>
              <li><a href="#">How It Works</a></li>
              <li><a href="#">About BRAVED Framework</a></li>
              <li><a href="#">About BALAJIS Framework</a></li>
              <li><a href="#">Privacy Policy</a></li>
            </ul>
          </div>
          <div className="footer-section">
            <h3>Connect</h3>
            <div className="social-links">
              <a href="#" className="social-link">Twitter</a>
              <a href="#" className="social-link">Discord</a>
              <a href="#" className="social-link">GitHub</a>
            </div>
          </div>
        </div>
        <div className="footer-bottom">
          <p>&copy; {new Date().getFullYear()} BRAVED BALAJIS. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
};

export default Home; 