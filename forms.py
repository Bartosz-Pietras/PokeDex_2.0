from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

allowed_extensions = ['jpg', 'jpeg', 'png']


class PokemonImageForm(FlaskForm):
    pokemon = FileField('image', validators=[
        FileRequired(),
        FileAllowed(allowed_extensions,
                    f'You can only upload files with the following extensions: {allowed_extensions}')])
    submit = SubmitField('Upload Photo')
