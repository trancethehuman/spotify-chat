from ai_agents import initialize_agent_zero_shot
from ai_tools import tool_start_playing_song_by_lyrics, tool_start_playing_song_by_name, tool_pause_playback

# Initialize agent
tools = [
    tool_start_playing_song_by_lyrics(),
    tool_start_playing_song_by_name(),
    tool_pause_playback()
]

agent = initialize_agent_zero_shot(tools=tools)

print("\nWhat's up! It's your boi DJ GPT. Can I take your requests?")

while True:
    request = input(
        "\n\nRequest: ")
    result = agent({"input": request})
    answer = result["output"]
    print(answer)
