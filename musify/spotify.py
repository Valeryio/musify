
import os
import json
import base64
from requests import *
from dotenv import load_dotenv


class Spotify():
    """This class contains the different methods and
    attributes to interact with the spotify Web API"""

    __authorization_details = {}
    __token = ""

    def __init__(self, app):
        load_dotenv()
        self.__client_id = os.getenv("CLIENT_ID")
        self.__client_secret = os.getenv("CLIENT_SECRET")

    @property
    def client_id(self):
        return self.__client_id

    @property
    def client_secret(self):
        return self.__client_secret

    @property
    def token(self):
        return self.__token

    @property
    def authorisation_details(self):
        return self.__authorization_details
    
    @token.setter
    def token(self, value):
        if value is not None and type(value) is str:
            self.__token = value
        else:
            raise ValueError("Invalid type for the WEB_API_token")

    @authorisation_details.setter
    def authorization_details(self, params):
        """
            set the value of the authorization_detail attribute
        """
        if type(params) is not dict:
            raise ValueError("Authorization parameters should be\
                             an dictionnary")
        else:
            self.__authorization_details = params

    def get_token(self):

        url = "https://accounts.spotify.com/api/token"
        auth_string = self.client_id + ":" + self.client_secret
        auth_string = auth_string.encode("utf-8")
        
        #print(auth_string)
        auth_base64 = str(base64.b64encode(auth_string), "utf-8")

        data = {"grant_type" : "client_credentials"}
        headers = {
             "Authorization": "Basic " + auth_base64,
             "Content-Type": "application/x-www-form-urlencoded"
             }


        response = post(url=url, data=data, headers=headers)
        self.authorization_details = json.loads(response.content)
        self.token = self.authorization_details["access_token"]
        
        #print("The response : \nContent :", response.content)
        #print("The token : ", self.token)
    
    def get_header(self):
        """
            returns the right header to request data to the WEB api
        """
        self.get_token()
        return {"Authorization": "Bearer " + self.token}

    def get_recommanded_albums(self, genre="pop", number=1):
        """Gets a customised global recommandation from the SPOTIFY
        WEB API

        Args:
            number (int): number of albums to get
        
        Returns:
            (list): a list of tracks (as objects)
        """

        url = "https://api.spotify.com/v1/recommendations"
        query = f"?seed_genres={genre}%2Ccountry&limit={number}"

        url_query = url + query
        response = get(url_query, headers=self.get_header())
        track_list = json.loads(response.content)

        # Only get the tracks objects and not the seeds
        track_list = track_list["tracks"]

        # Deletes some useless keys
        track_list = self.format_album_track(track_list)

        return track_list

    def format_album_track(self, track_list):
        """Deletes some useless keys from the track object
        in the track_list

        Returns a track_list with no useless keys!

        Args:
            (list) : a list of objects (tracks)
        """

        keys = ["disc_number", "duration_ms", "explicit",
                 "external_ids", "external_urls", "href",
                 "is_local", "type", "uri", "track_number",
                 "popularity", "name", "restrictions", "linked_from",
                 "is_playable"]

        for track in track_list:
            for key in keys:
                try:
                    track.pop(key, None)
                except KeyError:
                    pass
        
        return track_list
            
    def get_artist(self, artist_name):
        """Gets an artist id based on its name

        Args:
            artist_name (str): the name of the artist
        
        Return:
            (str): the id of the artist
        """

        url = "https://api.spotify.com/v1/search"
        query = f"?q={artist_name}&type=artist&limit=1"

        url_query = url + query
        response = get(url_query, headers=self.get_header())
        json_result = json.loads(response.content)
        return json_result
    
    def get_artist_albums(self, artist_id):
        """Gets albums of an artist based on its id

        Args:
            artist_name (str): the name of the artist
        
        Return:
            (str): the id of the artist
        """

        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"

        response = get(url, headers=self.get_header())
        return response.json()
    
    def get_artist_top_track(self, artist_id):
        """Gets top tracks of an artist based on its id

        Args:
            artist_name (str): the name of the artist
        
        Return:
            (object): the id of the artist
        """
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"

        response = get(url, headers=self.get_header())
        return response.json()["tracks"]

    def get_album(self, album_id):
        """Gets an album based on its id

        Args:
            album_id (str): the name of the artist

        Return:
            (object): the id of the artist
        """
        url = f"https://api.spotify.com/v1/albums/{album_id}"

        response = get(url, headers=self.get_header())
        # return response.json()["tracks"]
        return response.json()