import os
from dotenv import load_dotenv
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from consts import llm_model_type
from spotify import start_playing_song_by_name, start_playing_song_by_lyrics, pause_music


# Load .env variables
load_dotenv()


# LLM Initialization
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(max_retries=3, temperature=0,  # type: ignore
                 model_name=llm_model_type)


def tool_pause_playback():
    return Tool(name="Pause music", func=lambda n: pause_music(), description=f"""Pause music. No Action Input required.""", return_direct=True)  # type: ignore


def tool_start_playing_song_by_name():
    return Tool(name="Start playing a song by it's name", func=lambda song_name: start_playing_song_by_name(song_name), description=f"""start playing a song by it's name. Action Input is a string of song_name.""", return_direct=True)  # type: ignore


def tool_start_playing_song_by_lyrics():
    return Tool(name="Start playing a song by it's lyrics", func=lambda lyrics: start_playing_song_by_lyrics(lyrics), description=f"""start playing a song by it's lyrics. Action Input is a string of lyrics.""", return_direct=True)  # type: ignore
