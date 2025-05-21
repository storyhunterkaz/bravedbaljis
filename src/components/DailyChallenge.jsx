import React, { useState } from 'react';
import { trackCompletedLesson } from '../api/user';

const DailyChallenge = ({ challenge, userId }) => {
  const [currentStep, setCurrentStep] = useState(0);
  const [isCompleted, setIsCompleted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  
  const handleNextStep = () => {
    if (currentStep < challenge.steps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      completeChallenge();
    }
  };
  
  const completeChallenge = async () => {
    setIsLoading(true);
    try {
      // Assuming challenge has an ID
      await trackCompletedLesson(userId, challenge.id || 'daily-challenge');
      setIsCompleted(true);
    } catch (error) {
      console.error('Error completing challenge:', error);
    } finally {
      setIsLoading(false);
    }
  };
  
  if (isCompleted) {
    return (
      <div className="challenge-completed">
        <div className="completion-animation">
          <div className="checkmark">✓</div>
        </div>
        <h3>Challenge Completed!</h3>
        <p>You've earned {challenge.xpReward} XP</p>
        <div className="anti-materialism-reflection">
          <h4>Reflection</h4>
          <p>How did this challenge help you focus on knowledge and growth rather than material possessions?</p>
          <textarea 
            placeholder="Write your thoughts here..."
            className="reflection-input"
          />
          <button className="save-reflection-btn">Save Reflection</button>
        </div>
      </div>
    );
  }
  
  return (
    <div className="daily-challenge">
      <div className="challenge-header">
        <h3>{challenge.title}</h3>
        <div className="challenge-meta">
          <span className="time-estimate">{challenge.timeEstimate}</span>
          <span className="xp-reward">+{challenge.xpReward} XP</span>
        </div>
      </div>
      
      <p className="challenge-description">{challenge.description}</p>
      
      <div className="challenge-progress">
        <div className="progress-bar">
          <div 
            className="progress" 
            style={{ width: `${((currentStep + 1) / challenge.steps.length) * 100}%` }}
          />
        </div>
        <span className="progress-text">
          Step {currentStep + 1} of {challenge.steps.length}
        </span>
      </div>
      
      <div className="challenge-step">
        <h4>Step {currentStep + 1}: {challenge.steps[currentStep]}</h4>
        
        {currentStep === 0 && (
          <div className="challenge-content">
            <p>Let's learn about this topic together!</p>
            <div className="learning-module">
              {/* Content would be dynamically loaded here */}
              <p className="placeholder">Learning content about {challenge.title}</p>
            </div>
          </div>
        )}
        
        {currentStep === 1 && (
          <div className="challenge-quiz">
            <div className="quiz-question">
              <p>What is the primary benefit of learning about this topic?</p>
              <div className="quiz-options">
                <label className="quiz-option">
                  <input type="radio" name="quiz" value="option1" />
                  <span>To make more money</span>
                </label>
                <label className="quiz-option">
                  <input type="radio" name="quiz" value="option2" />
                  <span>To develop valuable skills and knowledge</span>
                </label>
                <label className="quiz-option">
                  <input type="radio" name="quiz" value="option3" />
                  <span>To impress others</span>
                </label>
                <label className="quiz-option">
                  <input type="radio" name="quiz" value="option4" />
                  <span>To acquire more possessions</span>
                </label>
              </div>
            </div>
          </div>
        )}
        
        {currentStep === 2 && (
          <div className="challenge-application">
            <p>Now apply what you've learned to a real-world scenario.</p>
            <div className="application-exercise">
              <p>How would you use this knowledge to create value for others?</p>
              <textarea 
                placeholder="Write your answer here..."
                className="application-input"
              />
            </div>
          </div>
        )}
      </div>
      
      <button 
        className="next-step-btn"
        onClick={handleNextStep}
        disabled={isLoading}
      >
        {isLoading ? 'Loading...' : 
          currentStep < challenge.steps.length - 1 ? 
          'Next Step' : 'Complete Challenge'}
      </button>
    </div>
  );
};

export default DailyChallenge; 