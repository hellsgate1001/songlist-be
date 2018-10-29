import os
import json
import time
from datetime import date

from flask import request
from app import app


@app.route('/update_practiced')
def update_practiced():
  songs = get_songlist()
  return json.dumps(sorted(songs, key=lambda x: (x['lastPracticed'], x['name'])))


@app.route('/add_song', methods=['POST'])
def add_song():
  songs = get_songlist()
  new_song = {
    'name': request.json['name'],
    'lastPracticed': time.mktime(date.today().timetuple())
  }
  songs.append(new_song)
  write_songlist(songs)
  return json.dumps(sorted(songs, key=lambda x: (x['lastPracticed'], x['name'])))


def get_songlist():
  with open(os.path.join(os.path.dirname(__file__), 'songlist.json'), 'r') as f:
    return json.load(f)


def write_songlist(songs):
  with open(os.path.join(os.path.dirname(__file__), 'songlist.json'), 'w') as f:
    json.dump(songs, f)
