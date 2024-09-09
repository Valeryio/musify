
from musify import app
from wtforms.validators import Length, DataRequired
from flask_wtf import FlaskForm
from wtforms import SearchField, SubmitField, TextAreaField, StringField


class SearchForm(FlaskForm):
    """
        This is the search form used to search
    """

    search_field = SearchField(validators=[Length(min=2, max=30), DataRequired()])
    submit = SubmitField()


class AlbumForm(FlaskForm):
    """This is the submit form for any album
        of an artist
    """

    album_id = StringField()
    submit = SubmitField()
