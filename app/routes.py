import os
import json
import time
from datetime import date

from flask import request
from app import app


@app.route('/get_songs')
def get_songs():
  songs = get_songlist()
  tolearn = get_tolearn()
  data = {'songs': songs, 'tolearn': tolearn}
  return json.dumps(data)


@app.route('/add_song', methods=['POST'])
def add_song():
  tolearn = get_tolearn()
  tolearn.append(request.json['name'])
  write_tolearn(tolearn)
  return json.dumps(tolearn)


@app.route('/set_practiced', methods=['POST'])
def set_practiced():
  songs = get_songlist()
  for song in songs:
    if song['name'] == request.json['name']:
      song['lastPracticed'] = time.mktime(date.today().timetuple())
      break
  write_songlist(songs)
  return json.dumps(songs)


@app.route('/move_to_current', methods=['POST'])
def move_to_current():
  songs = get_songlist()
  tolearn = get_tolearn()
  tolearn.remove(request.json['name'])
  new_current = {
    'name': request.json['name'],
    'lastPracticed': time.mktime(date.today().timetuple())
  }
  songs.append(new_current)
  write_songlist(songs)
  write_tolearn(tolearn)
  data = {'songs': songs, 'tolearn': tolearn}
  return json.dumps(data)


def get_songlist():
  with open(os.path.join(os.path.dirname(__file__), 'songlist.json'), 'r') as f:
    return json.load(f)


def write_songlist(songs):
  with open(os.path.join(os.path.dirname(__file__), 'songlist.json'), 'w') as f:
    json.dump(songs, f)


def get_tolearn():
  with open(os.path.join(os.path.dirname(__file__), 'tolearn.json'), 'r') as f:
    return json.load(f)


def write_tolearn(tolearn):
  with open(os.path.join(os.path.dirname(__file__), 'tolearn.json'), 'w') as f:
    json.dump(tolearn, f)
