from agno.agent import Agent
from agno.models.anthropic import Claude
from agno.tools.reasoning import ReasoningTools

def create_simple_agent():
    agent = Agent(
        model=Claude(id="claude-3-sonnet-20240229"),
        tools=[
            ReasoningTools(add_instructions=True),
        ],
        instructions=[
            "You are a helpful assistant that can reason through complex problems.",
            "Always show your reasoning process step by step.",
            "Be concise but thorough in your explanations.",
        ],
        markdown=True,
    )
    return agent

if __name__ == "__main__":
    agent = create_simple_agent()
    # Example interaction
    response = agent.print_response(
        "What are the key considerations when designing a scalable system?",
        stream=True,
        show_full_reasoning=True
    ) 