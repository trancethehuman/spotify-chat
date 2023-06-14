from ai_agents import initialize_agent_with_new_openai_functions
from ai_tools import music_player_tools

# Initialize agent

agent = initialize_agent_with_new_openai_functions(
    tools=music_player_tools)


print("\nWhat's up! It's your boi DJ GPT. Can I take your requests?")

while True:
    request = input(
        "\n\nRequest: ")
    result = agent({"input": request})
    answer = result["output"]
    print(answer)
