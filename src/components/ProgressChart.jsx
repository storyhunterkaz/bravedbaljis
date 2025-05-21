import React, { useEffect, useRef } from 'react';
import Chart from 'chart.js/auto';

const ProgressChart = ({ bravedScores, balajisScores }) => {
  const chartRef = useRef(null);
  const chartInstance = useRef(null);
  
  useEffect(() => {
    if (!chartRef.current || !bravedScores || !balajisScores) return;
    
    // Destroy previous chart if it exists
    if (chartInstance.current) {
      chartInstance.current.destroy();
    }
    
    // Prepare BRAVED data
    const bravedLabels = [
      'Bitcoin & Crypto',
      'Real World Assets',
      'AI & Agents',
      'VR/AR & Spatial',
      'Emotional Intelligence',
      'Decentralization'
    ];
    
    const bravedData = [
      bravedScores.bitcoin || 0,
      bravedScores.realWorldAssets || 0,
      bravedScores.ai || 0,
      bravedScores.vr || 0,
      bravedScores.emotionalIntelligence || 0,
      bravedScores.decentralization || 0
    ];
    
    // Prepare BALAJIS data
    const balajisLabels = [
      'Build',
      'Attention',
      'Leverage',
      'Algorithms',
      'Joy',
      'Influence',
      'Skills'
    ];
    
    const balajisData = [
      balajisScores.build || 0,
      balajisScores.attention || 0,
      balajisScores.leverage || 0,
      balajisScores.algorithms || 0,
      balajisScores.joy || 0,
      balajisScores.influence || 0,
      balajisScores.skills || 0
    ];
    
    // Create chart
    chartInstance.current = new Chart(chartRef.current, {
      type: 'bar',
      data: {
        labels: [...bravedLabels, ...balajisLabels],
        datasets: [
          {
            label: 'BRAVED',
            data: [...bravedData, ...Array(balajisLabels.length).fill(0)],
            backgroundColor: 'rgba(75, 192, 192, 0.7)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
          },
          {
            label: 'BALAJIS',
            data: [...Array(bravedLabels.length).fill(0), ...balajisData],
            backgroundColor: 'rgba(153, 102, 255, 0.7)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 1
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          y: {
            beginAtZero: true,
            max: 100,
            title: {
              display: true,
              text: 'Progress (%)'
            }
          },
          x: {
            title: {
              display: true,
              text: 'Skills & Knowledge'
            }
          }
        },
        plugins: {
          tooltip: {
            callbacks: {
              title: function(tooltipItems) {
                const index = tooltipItems[0].dataIndex;
                const dataset = tooltipItems[0].dataset;
                if (dataset.label === 'BRAVED' && index < bravedLabels.length) {
                  return bravedLabels[index];
                } else if (dataset.label === 'BALAJIS' && index >= bravedLabels.length) {
                  return balajisLabels[index - bravedLabels.length];
                }
                return '';
              }
            }
          },
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Your Learning Progress'
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
  
  return (
    <div className="progress-chart-container">
      <canvas ref={chartRef} height="250" />
      <div className="anti-materialism-insight">
        <p>
          Growth in knowledge and skills is the true measure of wealth.
          Your progress shows how you're building lasting value beyond material possessions.
        </p>
      </div>
    </div>
  );
};

export default ProgressChart; 