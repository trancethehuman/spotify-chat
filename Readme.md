Create a new Python virtual environment

- `python -m venv spotify-chat` (Mac)
- `py -m venv spotify-chat` (Windows 11)

Start virtual environment manually by running: `source spotify-chat/bin/activate` (Mac)

Or start it automatically by opening a new Terminal or Powershell and entering the project's directory.
Install Python requirements in the project repository: `pip install -r requirements.txt`

If new dependencies are added, add them manually to `requirements.txt`

- Start server: `uvicorn main:app --reload`
