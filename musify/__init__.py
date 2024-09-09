
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