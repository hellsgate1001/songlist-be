from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r'*', 'http://192.168.1.20:8080'})

# from . import songs
# app.register_blueprint(songs.bp)

from app import routes
