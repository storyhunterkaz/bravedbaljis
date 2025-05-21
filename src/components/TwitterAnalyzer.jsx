import React, { useState } from 'react';
import { fetchUserTweets, analyzeTweets, extractTopics } from '../api/twitter';
import { updateUserInterests, updateUserProfile } from '../api/user';
import { generateLearningPath } from '../api/learning';

const TwitterAnalyzer = ({ userId, onAnalysisComplete }) => {
  const [twitterHandle, setTwitterHandle] = useState('');
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisResults, setAnalysisResults] = useState(null);
  const [error, setError] = useState(null);
  const [step, setStep] = useState(1); // 1: Input, 2: Analyzing, 3: Results
  
  const handleInputChange = (e) => {
    setTwitterHandle(e.target.value);
  };
  
  const startAnalysis = async () => {
    if (!twitterHandle) {
      setError('Please enter your Twitter handle');
      return;
    }
    
    setError(null);
    setIsAnalyzing(true);
    setStep(2);
    
    try {
      // Fetch tweets
      const tweets = await fetchUserTweets(twitterHandle);
      
      if (!tweets || tweets.length === 0) {
        throw new Error('Could not fetch tweets. Please check your Twitter handle.');
      }
      
      // Analyze tweets
      const analysis = await analyzeTweets(tweets);
      
      // Extract topics as fallback if AI analysis fails
      if (!analysis.interests || analysis.interests.length === 0) {
        analysis.interests = extractTopics(tweets);
      }
      
      // Update user profile with interests
      await updateUserInterests(userId, analysis.interests);
      
      // Generate learning path based on interests
      const learningPath = await generateLearningPath(
        analysis.interests, 
        analysis.goals || []
      );
      
      // Update user profile with learning path
      await updateUserProfile(userId, { 
        learningPath: learningPath.personalizedPath,
        twitterHandle
      });
      
      setAnalysisResults({
        interests: analysis.interests,
        goals: analysis.goals,
        passions: analysis.passions,
        learningPath: learningPath.personalizedPath
      });
      
      setStep(3);
      
      // Notify parent component
      if (onAnalysisComplete) {
        onAnalysisComplete(analysis);
      }
    } catch (error) {
      console.error('Error analyzing Twitter profile:', error);
      setError(error.message || 'An error occurred during analysis');
      setStep(1);
    } finally {
      setIsAnalyzing(false);
    }
  };
  
  const renderInputStep = () => (
    <div className="twitter-input-step">
      <h3>Connect Your Twitter Account</h3>
      <p>
        We'll analyze your Twitter posts to identify your interests, passions, and goals.
        This helps us create a personalized learning path for you.
      </p>
      <div className="input-group">
        <span className="input-prefix">@</span>
        <input
          type="text"
          value={twitterHandle}
          onChange={handleInputChange}
          placeholder="yourusername"
          className="twitter-handle-input"
        />
      </div>
      {error && <p className="error-message">{error}</p>}
      <button 
        onClick={startAnalysis}
        className="analyze-btn"
        disabled={!twitterHandle || isAnalyzing}
      >
        Start Analysis
      </button>
      <p className="privacy-note">
        Your data is analyzed securely and only used to personalize your learning experience.
        We don't store or share your tweets.
      </p>
    </div>
  );
  
  const renderAnalyzingStep = () => (
    <div className="analyzing-step">
      <div className="analyzing-animation">
        <div className="pulse-circle"></div>
        <div className="brain-icon">🧠</div>
      </div>
      <h3>Analyzing Your Twitter Activity</h3>
      <div className="analyzing-status">
        <p>Discovering your interests, passions, and goals...</p>
        <div className="progress-bar">
          <div className="progress analyzing"></div>
        </div>
      </div>
    </div>
  );
  
  const renderResultsStep = () => (
    <div className="analysis-results">
      <div className="success-icon">✓</div>
      <h3>Analysis Complete!</h3>
      
      <div className="results-section">
        <h4>Your Interests</h4>
        <div className="interests-tags">
          {analysisResults.interests.map((interest, index) => (
            <span key={index} className="interest-tag">{interest}</span>
          ))}
        </div>
      </div>
      
      {analysisResults.goals && analysisResults.goals.length > 0 && (
        <div className="results-section">
          <h4>Your Goals</h4>
          <ul className="goals-list">
            {analysisResults.goals.map((goal, index) => (
              <li key={index}>{goal}</li>
            ))}
          </ul>
        </div>
      )}
      
      <div className="anti-materialism-insight">
        <h4>Beyond Materialism</h4>
        <p>
          Your learning path focuses on building skills and knowledge that transcend 
          material possessions. We've created a personalized journey based on your 
          interests that will help you develop lasting value.
        </p>
      </div>
      
      <button 
        onClick={onAnalysisComplete}
        className="view-path-btn"
      >
        View Your Learning Path
      </button>
    </div>
  );
  
  return (
    <div className="twitter-analyzer">
      {step === 1 && renderInputStep()}
      {step === 2 && renderAnalyzingStep()}
      {step === 3 && renderResultsStep()}
    </div>
  );
};

export default TwitterAnalyzer; 