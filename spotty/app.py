import config
import os
import spotipy
import spotipy.util as util
import sys

from flask import Flask, jsonify, Response
from spotipy.oauth2 import SpotifyClientCredentials

# pull our Spotify API credentials from environment
cid = os.getenv("SPOTTY_CID")
secret = os.getenv("SPOTTY_SECRET")
if not config.CID or not config.SECRET:
    raise SystemExit("no credentials found")

# set up our Spotify API client handle
app = Flask(__name__)
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# finally set our Flask context and endpoint handlers
app = Flask(__name__)

# basic health check
@app.route('/ping')
def health():
    return Response("pong", status=200)

# return a 15-track playlist based upon a seed artist
@app.route('/playlist/<artist>', methods=['GET'])
def get_suggestions(artist):
    try:
        resp = sp.search(q='artist:' + artist, type='artist')["artists"]["items"]
        if not resp:
            return Response("{'error': 'artist not found'}", status=422, mimetype='application/json')
    except Exception as err:
        return Response("{'error': 'internal error'}", status=500, mimetype='application/json')

    seed_artist = resp[0]["uri"]
    rec = sp.recommendations(seed_artists=[seed_artist], limit=15)
    tracks = []
    for track in rec["tracks"]:
        entry = {
            "artist": track["album"]["artists"][0]["name"],
            "track": track["name"]
        }
        tracks.append(entry)
    return jsonify({'tracks': tracks})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)