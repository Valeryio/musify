
from test.unit.musifyapp import client

def test_landing_page(client):
    landing_page = client.get("/")
    html_result = landing_page.data.decode()

    # checks that the important links to the landing page section exists
    assert '<a href="#" class="header__nav-item">Intro</a>' in html_result
    assert '<a href="#about" class="header__nav-item">About</a>' in html_result
    assert '<a href="#feature" class="header__nav-item">Features</a>' in html_result

    # checks that the page responds to with the right code
    assert landing_page.status_code == 200

def test_index_page(client):
    index_page = client.get("/home")

    # checks that the page responds to with the right code
    assert index_page.status_code == 200

def test_songs_page(client):
    songs_page = client.get("/songs/GIMS/55DUcp4pTvwD4VzUnWaXfw")

    # checks that the page responds to with the right code
    songs_page.status_code == 200

def test_artist_page(client):
    artist_page = client.get("artist/Johny%20haliday")

    # checks that the page responds to with the right code
    artist_page.status_code == 200