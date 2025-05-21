import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

const SkillsRadar = ({ bravedScores, balajisScores }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);
  
  useEffect(() => {
    if (!chartRef.current || !bravedScores || !balajisScores) return;
    
    // Destroy previous chart if it exists
    if (chartInstance.current) {
      chartInstance.current.destroy();
    }
    
    // Prepare data for radar chart
    const data = {
      labels: [
        'Bitcoin & Crypto',
        'Real World Assets',
        'AI & Agents',
        'VR/AR & Spatial',
        'Emotional Intelligence',
        'Decentralization',
        'Build',
        'Attention',
        'Leverage',
        'Algorithms',
        'Joy',
        'Influence',
        'Skills'
      ],
      datasets: [
        {
          label: 'Your Skills',
          data: [
            bravedScores.bitcoin || 0,
            bravedScores.realWorldAssets || 0,
            bravedScores.ai || 0,
            bravedScores.vr || 0,
            bravedScores.emotionalIntelligence || 0,
            bravedScores.decentralization || 0,
            balajisScores.build || 0,
            balajisScores.attention || 0,
            balajisScores.leverage || 0,
            balajisScores.algorithms || 0,
            balajisScores.joy || 0,
            balajisScores.influence || 0,
            balajisScores.skills || 0
          ],
          fill: true,
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgb(54, 162, 235)',
          pointBackgroundColor: 'rgb(54, 162, 235)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(54, 162, 235)'
        }
      ]
    };
    
    // Create radar chart
    chartInstance.current = new Chart(chartRef.current, {
      type: 'radar',
      data: data,
      options: {
        elements: {
          line: {
            borderWidth: 3
          }
        },
        scales: {
          r: {
            angleLines: {
              display: true
            },
            suggestedMin: 0,
            suggestedMax: 100,
            ticks: {
              stepSize: 20
            }
          }
        },
        plugins: {
          legend: {
            position: 'top',
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                return `${context.dataset.label}: ${context.raw}%`;
              }
            }
          }
        }
      }
    });
    
    return () => {
      if (chartInstance.current) {
        chartInstance.current.destroy();
      }
    };
  }, [bravedScores, balajisScores]);
  
  const findHighestSkill = () => {
    if (!bravedScores || !balajisScores) return null;
    
    const allScores = {
      'Bitcoin & Crypto': bravedScores.bitcoin || 0,
      'Real World Assets': bravedScores.realWorldAssets || 0,
      'AI & Agents': bravedScores.ai || 0,
      'VR/AR & Spatial': bravedScores.vr || 0,
      'Emotional Intelligence': bravedScores.emotionalIntelligence || 0,
      'Decentralization': bravedScores.decentralization || 0,
      'Build': balajisScores.build || 0,
      'Attention': balajisScores.attention || 0,
      'Leverage': balajisScores.leverage || 0,
      'Algorithms': balajisScores.algorithms || 0,
      'Joy': balajisScores.joy || 0,
      'Influence': balajisScores.influence || 0,
      'Skills': balajisScores.skills || 0
    };
    
    return Object.entries(allScores)
      .sort((a, b) => b[1] - a[1])
      .map(([skill]) => skill)[0];
  };
  
  const findWeakestSkill = () => {
    if (!bravedScores || !balajisScores) return null;
    
    const allScores = {
      'Bitcoin & Crypto': bravedScores.bitcoin || 0,
      'Real World Assets': bravedScores.realWorldAssets || 0,
      'AI & Agents': bravedScores.ai || 0,
      'VR/AR & Spatial': bravedScores.vr || 0,
      'Emotional Intelligence': bravedScores.emotionalIntelligence || 0,
      'Decentralization': bravedScores.decentralization || 0,
      'Build': balajisScores.build || 0,
      'Attention': balajisScores.attention || 0,
      'Leverage': balajisScores.leverage || 0,
      'Algorithms': balajisScores.algorithms || 0,
      'Joy': balajisScores.joy || 0,
      'Influence': balajisScores.influence || 0,
      'Skills': balajisScores.skills || 0
    };
    
    // Only consider skills with a value > 0
    const nonZeroScores = Object.entries(allScores).filter(([_, value]) => value > 0);
    
    if (nonZeroScores.length === 0) {
      return Object.keys(allScores)[0]; // Return first skill if all are zero
    }
    
    return nonZeroScores
      .sort((a, b) => a[1] - b[1])
      .map(([skill]) => skill)[0];
  };
  
  const highestSkill = findHighestSkill();
  const weakestSkill = findWeakestSkill();
  
  return (
    <div className="skills-radar-container">
      <canvas ref={chartRef} height="300" />
      
      <div className="skills-insights">
        {highestSkill && (
          <div className="skill-highlight">
            <h4>Your Strongest Area</h4>
            <p>{highestSkill}</p>
          </div>
        )}
        
        {weakestSkill && (
          <div className="skill-highlight">
            <h4>Area for Growth</h4>
            <p>{weakestSkill}</p>
          </div>
        )}
        
        <div className="anti-materialism-note">
          <p>
            Balanced growth across these areas will help you develop skills that create lasting value,
            rather than focusing on short-term material gains.
          </p>
        </div>
      </div>
    </div>
  );
};

export default SkillsRadar; 