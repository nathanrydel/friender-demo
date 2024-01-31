from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, FileField, IntegerField, TelField
from wtforms.validators import InputRequired, Email, Length, Optional, NumberRange


class CSRFProtection(FlaskForm):
    """CSRFProtection form, intentionally has no fields."""


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=16)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )

    email = StringField(
        'E-mail',
        validators=[InputRequired(), Email(), Length(max=50)],
    )

    first_name = StringField(
        'First Name',
        validators=[InputRequired(), Length(max=25)]
    )

    last_name = StringField(
        'Last Name',
        validators=[InputRequired(), Length(max=25)]
    )

    # TODO: Check geo-coding libraries to see what form is required
    zipcode = StringField(
        'Zip Code',
        validators=[InputRequired(), Length(max=10)]
    )

    # TODO: check if there is a Phone Number WTF validator
    phone_number = TelField(
        'Phone Number',
        validators=[
            InputRequired()
        ]
    )

# TODO: FS-A add option for phone number and email login
class LoginForm(FlaskForm):
    """Login form."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=16)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )

class UserEditForm(FlaskForm):
    """Form for editing users."""

    # TODO: adding a file to send to S3, need to check how to do it
    # Currently only one hobby and interest can be selected
    profile_photo = FileField(
        '(Optional) Profile Image',
        validators=[Optional()]
    )

    bio = TextAreaField(
        '(Optional) Tell us about yourself',
        validators=[Optional(), Length(max=255)]
    )

    zipcode = StringField(
        'Zip Code',
        validators=[InputRequired(), Length(max=10)]
    )

    hobby = SelectField(
        'Hobby',
        validator=[InputRequired()]
    )

    interest = SelectField(
        'Interest',
        validator=[InputRequired()]
    )

    friend_radius=IntegerField(
        'Friend Radius',
        validator=[InputRequired(), NumberRange(min=1, max=100)]
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )