from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, Length, URL

class PetForm(FlaskForm):
    name = StringField("Pet Name", InputRequired())
    species = SelectField( "Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField('Photo URL', Optional())
    age = FloatField('Age of Pet', NumberRange(min=0, max=30))
    notes = StringField('Notes', Length(min=10))
    available = BooleanField('Available?')

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL",validators=[Optional(), URL()])

    notes = StringField("Notes", validators=[Optional(), Length(min=10)])

    available = BooleanField("Available?")