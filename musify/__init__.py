
import os
from flask import Flask, render_template
from dotenv import load_dotenv
from musify.spotify import Spotify


# The application
app = Flask(__name__)


#The secret key of the application
load_dotenv()
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
print("The config secret : ", app.config["SECRET_KEY"])

#The musify class linked to the webapp
spotify_client = Spotify(app)


# Import different routes of the application
from musify import views

# The app templates configurations

@app.template_filter("music_time")
def music_time(ms_time):
    milliseconds = ms_time / 1000
    minutes = str(milliseconds / 60)
    time_track = []

    seconds = int(minutes.split('.')[1][:2])
    minutes = int(minutes.split('.')[0])

    if seconds > 60:
        minutes += 1
        seconds -= 60

    time_track.append(str(minutes))
    time_track.append(str(seconds))
    track_time = ':'.join(time_track)
    return track_time
