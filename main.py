from ai_agents import initialize_agent_zero_shot
from ai_tools import tool_add_song_to_queue_by_song_name, tool_add_song_to_queue_by_lyrics

# Initialize agent
tools = [tool_add_song_to_queue_by_song_name(
), tool_add_song_to_queue_by_lyrics()]
agent = initialize_agent_zero_shot(tools=tools)

while True:
    request = input("What would you like to do: ")
    result = agent({"input": request})
    answer = result["output"]
    print(answer)
