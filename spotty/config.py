from os import environ as env
import multiprocessing

# pull our Spotify API credentials from environment
CID = env.get("SPOTTY_CID")
SECRET = env.get("SPOTTY_SECRET")

# and server configuration as well, with defaults
PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

# Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()
