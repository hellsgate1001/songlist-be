import json
import time
from datetime import date

from app import app


@app.route('/update_practiced')
def update_practiced():
    songs = [
        {
          'name': 'Blondie - Call Me',
          'lastPracticed': time.mktime(date(2018,10,24).timetuple())
        },
        {
          'name': 'Alice In Chains - Man In A Box',
          'lastPracticed': time.mktime(date(2018,10,22).timetuple())
        },
        {
          'name': 'Guns N Roses - Nightrain',
          'lastPracticed': time.mktime(date(2018,10,21).timetuple())
        },
        {
          'name': 'Heart - Barracuda',
          'lastPracticed': time.mktime(date(2018,10,22).timetuple())
        },
        {
          'name': 'Alter Bridge - Blackbird',
          'lastPracticed': time.mktime(date(2018,10,21).timetuple())
        },
        {
          'name': 'Green Day - Longview',
          'lastPracticed': time.mktime(date(2018,10,20).timetuple())
        },
        {
          'name': 'Foo Fighters - The Pretender',
          'lastPracticed': time.mktime(date(2018,10,21).timetuple())
        },
        {
          'name': 'Muse - Hysteria',
          'lastPracticed': time.mktime(date(2018,10,21).timetuple())
        },
        {
          'name': 'Black Stone Cherry - Blind Man',
          'lastPracticed': time.mktime(date(2018,10,21).timetuple())
        },
        {
          'name': 'Jane\'s Addiction - Been Caught Stealing',
          'lastPracticed': time.mktime(date(2018,10,31).timetuple())
        }
      ]
    return json.dumps(sorted(songs, key=lambda x: x['lastPracticed']))
