import React, { useState, useEffect } from 'react';
import { getUserProfile, getUserStats } from '../api/user';
import { generateDailyChallenge } from '../api/learning';
import LearningPath from './LearningPath';
import DailyChallenge from './DailyChallenge';
import ProgressChart from './ProgressChart';
import SkillsRadar from './SkillsRadar';

const Dashboard = ({ userId }) => {
  const [userProfile, setUserProfile] = useState(null);
  const [userStats, setUserStats] = useState(null);
  const [dailyChallenge, setDailyChallenge] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        // Fetch user profile
        const profile = await getUserProfile(userId);
        setUserProfile(profile);
        
        // Fetch user stats
        const stats = await getUserStats(userId);
        setUserStats(stats);
        
        // Generate daily challenge
        const challenge = generateDailyChallenge(profile);
        setDailyChallenge(challenge);
      } catch (error) {
        console.error('Error loading dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };
    
    fetchData();
  }, [userId]);

  if (loading) {
    return <div className="loading-spinner">Loading your personalized dashboard...</div>;
  }

  if (!userProfile) {
    return <div className="error-message">Unable to load your profile. Please try again later.</div>;
  }

  return (
    <div className="dashboard">
      <header className="dashboard-header">
        <h1>Welcome back, {userProfile.username}!</h1>
        <div className="user-stats">
          <div className="stat">
            <span className="stat-value">{userProfile.level}</span>
            <span className="stat-label">Level</span>
          </div>
          <div className="stat">
            <span className="stat-value">{userProfile.streak}</span>
            <span className="stat-label">Day Streak</span>
          </div>
          <div className="stat">
            <span className="stat-value">{userStats?.lessonsCompleted || 0}</span>
            <span className="stat-label">Lessons</span>
          </div>
        </div>
      </header>
      
      <div className="dashboard-content">
        <div className="main-content">
          <section className="daily-challenge-section">
            <h2>Today's Challenge</h2>
            {dailyChallenge ? (
              <DailyChallenge challenge={dailyChallenge} userId={userId} />
            ) : (
              <p>No challenge available today. Check back tomorrow!</p>
            )}
          </section>
          
          <section className="learning-path-section">
            <h2>Your Learning Path</h2>
            <LearningPath 
              learningPath={userProfile.learningPath} 
              completedLessons={userProfile.completedLessons}
              userId={userId}
            />
          </section>
        </div>
        
        <aside className="dashboard-sidebar">
          <section className="progress-section">
            <h3>Your Progress</h3>
            <ProgressChart 
              bravedScores={userProfile.bravedScores} 
              balajisScores={userProfile.balajisScores} 
            />
          </section>
          
          <section className="skills-section">
            <h3>Your Skills</h3>
            <SkillsRadar 
              bravedScores={userProfile.bravedScores} 
              balajisScores={userProfile.balajisScores} 
            />
          </section>
          
          <section className="anti-materialism-insights">
            <h3>Moving Beyond Materialism</h3>
            <p className="insight-quote">
              "True wealth is not measured by what you own, but by what you learn, create, and share."
            </p>
            <div className="progress-bar">
              <div 
                className="progress" 
                style={{ 
                  width: `${Math.min(
                    (userStats?.lessonsCompleted || 0) * 2, 
                    100
                  )}%` 
                }}
              />
            </div>
            <p className="insight-text">
              You're making great progress on your journey beyond materialistic thinking. 
              Keep learning and growing!
            </p>
          </section>
        </aside>
      </div>
    </div>
  );
};

export default Dashboard; 