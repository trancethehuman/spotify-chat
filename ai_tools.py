import os
from dotenv import load_dotenv
from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from consts import llm_model_type
from spotify import add_song_to_queue_by_song_name


# Load .env variables
load_dotenv()


# LLM Initialization
openai_api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(max_retries=3, temperature=0,  # type: ignore
                 model_name=llm_model_type)


def tool_add_song_to_queue_by_song_name():
    return Tool(name="Add a song to playlist by song name", func=lambda song_name: add_song_to_queue_by_song_name(song_name), description=f"""add song to playlist or queue by song name. Action Input is a string of song_name.""", return_direct=True)  # type: ignore


def tool_add_song_to_queue_by_lyrics():
    return Tool(name="Add a song to playlist by song lyrics", func=lambda song_name: add_song_to_queue_by_song_name(song_name), description=f"""add song to playlist or queue by lyrics. Action Input is a string of lyrics.""", return_direct=True)  # type: ignore
