from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email, Length, URL, Optional, Regexp


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
    phone_number = StringField(
        'Phone Number',
        validators=[
            InputRequired(),
            Length(min=10, max=10),
            Regexp(regex='^[+-]?[0-9]$')
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
    profile_photo = StringField(
        '(Optional) Profile Image',
        validators=[Optional(), Length(max=255), URL()]
    )

    bio = TextAreaField(
        '(Optional) Tell us about yourself',
    )

    zipcode = StringField(
        'Zip Code',
        validators=[InputRequired(), Length(max=10)]
    )

    hobby = SelectField(
        'Hobby',
        validator=[InputRequired()]
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )