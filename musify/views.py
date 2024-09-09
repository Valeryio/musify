
from musify import app
from musify import spotify_client
from flask import render_template, redirect, url_for, request
from musify.forms import SearchForm, AlbumForm


@app.route("/", strict_slashes=False, methods=["GET", "POST"])
@app.route("/home", strict_slashes=False, methods=["GET", "POST"])
def index():
    """ This is the index route endpoint

    Methods:
        GET:/login
        POST:/login

    Returns:
        It renders the home.html template if no input is submitted
        It renders the artist.html template if an input is submitted
    """

    # Code to treat the search form
    form = SearchForm()
    result = form_redirect(form)
    if result is not None:
        return redirect(url_for("artist_page", search_data=result))

    """
    if form.validate_on_submit():
        search_data = form.search_field.data
        print(search_data)
        return redirect(url_for("get_artist", search_data=search_data))
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            print("Error : ", err_msg)
    """

    headers = spotify_client.get_header()
    albums = spotify_client.get_recommanded_albums(6)
    return render_template("index.html", headers=headers, albums=albums, form=form)


@app.route("/artist/<string:search_data>", strict_slashes=False, methods=["GET", "POST"])
def artist_page(search_data):
    """ This is the artist route endpoint

    Methods:
        GET:/login
        POST:/login

    Returns:
        It renders the artist.html template if an input is submitted
    """
    
    # Code to treat the search form
    form = SearchForm()
    result = form_redirect(form)
    if result is not None:
        return redirect(url_for("artist_page", search_data=result))

    # Get the object about the searched artist
    artist = spotify_client.get_artist(search_data)['artists']
    
    # Get the object about the albums of this artist
    albums = spotify_client.get_artist_albums(artist["items"][0]["id"])

    # Get the object about the top-track of this artist
    top_tracks = spotify_client.get_artist_top_track(artist["items"][0]["id"])

    # Code to manage the album forms
    album_form = AlbumForm()
    if album_form.validate_on_submit():
        print("Submitted")
        return redirect(url_for("songs_page", artist_name=artist["items"][0]["name"],
                                album_id=album_form.album_id.data))

    return render_template("artist.html", search_data=search_data, form=form,
                        artist=artist, albums=albums, top_tracks=top_tracks, album_form=album_form)


#app.route("/songs/<string:artist_name>/<string:album_id>", strict_slashes=False, methods=["GET", "POST"])
@app.route("/songs/<artist_name>/<album_id>", strict_slashes=False, methods=["GET", "POST"])
def songs_page(artist_name, album_id):
    """Get the songs of a specified album

    Return:
        (object)
    """

    # Code to manage the search form
    form = SearchForm()
    result = form_redirect(form)
    if result is not None:
        return redirect(url_for("artist_page", search_data=result))

    album = spotify_client.get_album(album_id)
    return render_template("songs.html", form=form, album=album)


def form_redirect(form):
    """Analyse the form if submit

    Args:
        form (object): analyse the form if submitted
    Return:
        (string): if the right input is entered
        None: if there's error in the process
    """
    if form.validate_on_submit():
        search_data = form.search_field.data
        print(search_data)
        return search_data
    
    if form.errors != {}:
        for err_msg in form.errors.values():
            print("Error : ", err_msg)
            return None







# curl "https://api.spotify.com/v1/recommendations?seed_genres=Acoustic%20Blues%2Ccountry&limit=2" -H "Authorization: Bearer BQBpCq6wUfFFWg4_tQrZEhNbH0sHvWDWu6Qd9qz0CggKXevdeDCq3Nic_1sqGopWQ9QE1wYcsI5wkpBCwMCjeg6hSjr99evv7djhw-lMZLNOeUcjzb8"

# curl "https://api.spotify.com/v1/search?seed_genres=Acoustic%20Blues%2Ccountry&limit=2" -H "Content-type: application/json" -H "Authorization: Bearer BQD4UE88G3QwVgR9BWibtO2PZ1FZq9iKq51m_XmA-JDVL6AqLw57ManaTbHjPisW-U7FKVgmdlwN_NOka_JG40z-Z86sK-nom77Ow34y38aUKIx_JHY"

# https://api.spotify.com/v1/artists/{artist_id}/albums

# curl "https://api.spotify.com/v1/albums/{70puiNnXbXIRjGTwj1D83e}" -H "Authorization: Bearer BQBhfPbuqgsAh25LeOyvmlcFcbQAe1aQOfmVD8UKKVoW_n0ZPtTLifmgq0gxtmLMqWEApJfj5X61QUaFhhqAiAfoaW9YSf_fyuUDIWPdt_iM2enuJ2w"