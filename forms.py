from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,IntegerField,BooleanField

from wtforms.validators import InputRequired, Optional, Email,URL,NumberRange


class AddPetForm(FlaskForm):
    """Add Pet Form"""

    name=StringField("Pet Name",validators=[InputRequired(message="Name cannot be blank")])
    species=SelectField("Species",choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porc', 'Porcupine')],validators=[InputRequired(message="Species cannot be blank")])
    photo_url=StringField("Photo URL",validators=[URL(),Optional()])
    age=IntegerField("Age",validators=[Optional(),NumberRange(min=0,max=30)])
    notes=StringField("Notes")


class EditPetForm(FlaskForm):
    """Edit Pet Form"""

    photo_url=StringField("Photo URL",validators=[URL(),Optional()])
    notes=StringField("Notes")
    available=BooleanField("Available")