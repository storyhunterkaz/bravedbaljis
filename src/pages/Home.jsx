import React, { useState, useEffect } from 'react';
import { useSession } from 'next-auth/react';
import { useRouter } from 'next/router';
import styles from '../styles/Home.module.css';

const Home = () => {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [learningPath, setLearningPath] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [neuroscienceInsights, setNeuroscienceInsights] = useState(null);

  useEffect(() => {
    if (status === 'unauthenticated') {
      router.push('/auth/signin');
    }
  }, [status, router]);

  const startAnalysis = async () => {
    setIsAnalyzing(true);
    try {
      const response = await fetch('/api/agent/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userId: session?.user?.id }),
      });
      const data = await response.json();
      setLearningPath(data);
    } catch (error) {
      console.error('Error analyzing profile:', error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  const fetchNeuroscienceInsights = async () => {
    try {
      const response = await fetch('/api/agent/neuroscience', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ userId: session?.user?.id }),
      });
      const data = await response.json();
      setNeuroscienceInsights(data);
    } catch (error) {
      console.error('Error fetching neuroscience insights:', error);
    }
  };

  useEffect(() => {
    if (session?.user?.id) {
      fetchNeuroscienceInsights();
    }
  }, [session]);

  if (status === 'loading') {
    return <div className={styles.loading}>Loading...</div>;
  }

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to Your Learning Journey
        </h1>
        
        <div className={styles.agentSection}>
          <h2>Your AI Learning Companion</h2>
          <p>Let our AI analyze your interests and create a personalized learning path</p>
          
          <button 
            className={styles.analyzeButton}
            onClick={startAnalysis}
            disabled={isAnalyzing}
          >
            {isAnalyzing ? 'Analyzing...' : 'Start Analysis'}
          </button>
        </div>

        {learningPath && (
          <div className={styles.learningPath}>
            <h2>Your Personalized Learning Path</h2>
            <div className={styles.pathContent}>
              {learningPath.modules.map((module, index) => (
                <div key={index} className={styles.module}>
                  <h3>{module.title}</h3>
                  <p>{module.description}</p>
                  <div className={styles.resources}>
                    {module.resources.map((resource, rIndex) => (
                      <a 
                        key={rIndex}
                        href={resource.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className={styles.resourceLink}
                      >
                        {resource.title}
                      </a>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {neuroscienceInsights && (
          <div className={styles.neuroscienceSection}>
            <h2>Neuroscience Insights</h2>
            <div className={styles.insightsContent}>
              <h3>Learning Style Preferences</h3>
              <ul>
                {Object.entries(neuroscienceInsights.learning_style_preferences).map(([style, data]) => (
                  <li key={style}>
                    <strong>{style}:</strong> {data.score.toFixed(2)} (Weight: {data.weight})
                  </li>
                ))}
              </ul>
              <h3>Recommendations</h3>
              <ul>
                {neuroscienceInsights.recommendations.map((rec, index) => (
                  <li key={index}>
                    <strong>{rec.type}:</strong> {rec.message}
                    <ul>
                      {rec.suggestions.map((suggestion, sIndex) => (
                        <li key={sIndex}>{suggestion}</li>
                      ))}
                    </ul>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        )}
      </main>
    </div>
  );
};

export default Home; 