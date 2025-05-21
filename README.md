# BRAVED BALAJIS - Web3 EdTech Companion

A Web3 edtech companion that analyzes social media posts to create personalized learning paths based on the BRAVED and BALAJIS frameworks.

## Features

- **Social Media Analysis**: Analyzes Twitter posts to understand user interests and goals
- **Personalized Learning Paths**: Creates customized learning journeys based on user interests
- **BRAVED Framework Integration**: Analyzes creative and technical interests (Building, Research, Art, Ventures, Engineering, Design)
- **BALAJIS Framework Integration**: Analyzes future-oriented interests (Bitcoin, AI, Longevity, Autonomous, Jobs, Internet, Space)
- **Neuroscience-Based Learning**: Analyzes learning patterns and provides personalized recommendations
- **Web3 Integration**: Built with modern Web3 technologies

## Tech Stack

- **Frontend**: Next.js, React, TailwindCSS
- **Backend**: FastAPI, Python
- **AI/ML**: Custom AI agents for analysis and recommendations
- **Authentication**: NextAuth.js
- **Database**: (To be implemented)
- **Web3**: ethers.js, web3.storage

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- Python (v3.8 or higher)
- Twitter API credentials
- Web3 wallet (for future features)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bravedbalajis.git
cd bravedbalajis
```

2. Install frontend dependencies:
```bash
npm install
```

3. Install backend dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
NEXTAUTH_SECRET=your_nextauth_secret
NEXTAUTH_URL=http://localhost:3000
```

5. Start the development server:
```bash
# Terminal 1 - Frontend
npm run dev

# Terminal 2 - Backend
uvicorn src.api.main:app --reload
```

## Project Structure

```
bravedbalajis/
├── src/
│   ├── agents/           # AI agents for analysis
│   ├── api/             # FastAPI backend
│   ├── components/      # React components
│   ├── pages/          # Next.js pages
│   └── styles/         # CSS modules
├── public/             # Static assets
├── requirements.txt    # Python dependencies
└── package.json       # Node.js dependencies
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the BRAVED and BALAJIS frameworks
- Built with modern Web3 technologies
- Powered by AI and neuroscience principles 