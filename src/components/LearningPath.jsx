import React from 'react';
import { Link } from 'react-router-dom';

const LearningPath = ({ learningPath, completedLessons, userId }) => {
  // Check if a lesson has been completed
  const isLessonCompleted = (lessonId) => {
    return completedLessons.includes(lessonId);
  };
  
  // Calculate the next unlocked lesson
  const getNextUnlockedLesson = () => {
    if (!learningPath || learningPath.length === 0) return 0;
    
    for (let i = 0; i < learningPath.length; i++) {
      if (!isLessonCompleted(learningPath[i].id)) {
        return i;
      }
    }
    
    return learningPath.length; // All lessons completed
  };
  
  // Determine if a lesson is unlocked
  const isLessonUnlocked = (index) => {
    const nextUnlocked = getNextUnlockedLesson();
    return index <= nextUnlocked;
  };
  
  if (!learningPath || learningPath.length === 0) {
    return (
      <div className="empty-learning-path">
        <p>Your personalized learning path is being created. Check back soon!</p>
        <button className="generate-path-btn">Generate Path Now</button>
      </div>
    );
  }
  
  return (
    <div className="learning-path">
      <div className="path-progress">
        <div className="progress-bar">
          <div 
            className="progress" 
            style={{ 
              width: `${(completedLessons.length / learningPath.length) * 100}%` 
            }}
          />
        </div>
        <span className="progress-text">
          {completedLessons.length} of {learningPath.length} lessons completed
        </span>
      </div>
      
      <div className="path-timeline">
        {learningPath.map((lesson, index) => (
          <div 
            key={lesson.id || index}
            className={`path-item ${
              isLessonCompleted(lesson.id) 
                ? 'completed' 
                : isLessonUnlocked(index) 
                  ? 'unlocked' 
                  : 'locked'
            }`}
          >
            <div className="path-item-connector">
              <div className="connector-line" />
              <div className="connector-dot" />
            </div>
            
            <div className="path-item-content">
              <div className="path-item-header">
                <h4>
                  Day {index + 1}: {lesson.topic}
                </h4>
                <div className="path-item-tags">
                  <span className="braved-tag">{lesson.topic}</span>
                  <span className="balajis-tag">{lesson.balajisSkill}</span>
                </div>
              </div>
              
              <p className="path-item-description">
                {lesson.content}
              </p>
              
              {isLessonCompleted(lesson.id) ? (
                <button className="revisit-btn">Revisit Lesson</button>
              ) : isLessonUnlocked(index) ? (
                <Link 
                  to={`/lesson/${lesson.id}`} 
                  className="start-lesson-btn"
                >
                  Start Lesson
                </Link>
              ) : (
                <button className="locked-btn" disabled>
                  <span className="lock-icon">🔒</span> Complete previous lessons to unlock
                </button>
              )}
            </div>
          </div>
        ))}
      </div>
      
      {completedLessons.length === learningPath.length && (
        <div className="path-completed">
          <h3>Congratulations! You've completed this learning path.</h3>
          <p>Ready for more challenges to further your growth?</p>
          <button className="new-path-btn">Generate New Path</button>
        </div>
      )}
    </div>
  );
};

export default LearningPath; 