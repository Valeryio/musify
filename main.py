
import os
import json
import base64
from requests import *
from dotenv import load_dotenv



load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")


def get_token():
    """
        This function requests the access token to allow communication
        between the application and the spotify API
    """
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    print(auth_base64)


    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {"grant_type": "client_credentials"}
    result = post(url=url, headers=headers, data=data)

    json_result = json.loads(result.content)
    token = json_result["access_token"]

    print("The result : ", result.content)


    return token




def get_auth_header(token):
        """
            Get the authorized header to communicate with the API
        """
        return {"Authorization": "Bearer " + token}



get_token()

print("We have : ", client_id, " and : ", client_secret)