from pydantic import BaseModel, Field
from spotify import start_playing_song_by_name, start_playing_song_by_lyrics, start_music, pause_music, start_playlist_by_name, next_track, previous_track
from langchain.tools import tool


class LyricsInput(BaseModel):
    lyrics: str = Field(
        description="lyrics in the user's request")


class SongNameInput(BaseModel):
    song: str = Field(
        description="song name in the user's request")


class PlaylistNameInput(BaseModel):
    playlist: str = Field(
        description="playlist name")


@tool("play_song_by_lyrics", return_direct=True, args_schema=LyricsInput)
def by_lyrics(lyrics: str) -> str:
    """Extract the lyrics from user's request and play the song."""
    return start_playing_song_by_lyrics(lyrics)


@tool("play_song_by_name", return_direct=True, args_schema=SongNameInput)
def by_name(song: str) -> str:
    """Extract the song name from user's request and play the song."""
    return start_playing_song_by_name(song)


@tool("start_music", return_direct=True)
def tool_start_music(query: str) -> str:
    """Start music player."""
    return start_music()


@tool("pause_music", return_direct=True)
def tool_pause_music(query: str) -> str:
    """Pause music player."""
    return pause_music()


@tool("next_track", return_direct=True)
def tool_next_track(query: str) -> str:
    """Play next track."""
    return next_track()


@tool("previous_track", return_direct=True)
def tool_previous_track(query: str) -> str:
    """Play previous track."""
    return previous_track()


@tool("play_playlist_by_name", return_direct=True, args_schema=PlaylistNameInput)
def tool_play_by_playlist(playlist: str) -> str:
    """Extract the playlist name from user's request and play the playlist."""
    return start_playlist_by_name(playlist)


music_player_tools = [
    by_lyrics,
    by_name,
    tool_start_music,
    tool_pause_music,
    tool_play_by_playlist,
    tool_next_track,
    tool_previous_track
]
