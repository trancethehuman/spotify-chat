import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from spotify import get_tracks_by_genre, add_track_to_queue, find_song_by_name

load_dotenv()  # Required to load .env

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return "hello"


@app.post("/get_tracks_by_genre")
async def get_tracks(request):
    return get_tracks_by_genre(request)


@app.post("/add_song_to_queue")
async def add_song_to_queue(request):
    return add_track_to_queue(request)


@app.post("/find_song_uri_by_name")
async def find_song_uri_by_name(request):
    return find_song_by_name(request)
