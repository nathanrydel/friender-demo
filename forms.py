from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed  # , FileRequired
from wtforms import StringField,  PasswordField, TextAreaField, SelectField, IntegerField, TelField, BooleanField
from wtforms.validators import InputRequired, Email, Length, Optional, NumberRange, Disabled, ValidationError

# TODO: phone validators, zipcode validator


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


class DeleteForm(FlaskForm):
    """Delete form."""

    username = StringField(
        'Username',
        validators=[InputRequired(), Length(max=16)],
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )

    confirm = BooleanField(
        'Are you sure you want to delete your account?',
        validators=[InputRequired()]
    )

    def validate_confirm(self, field):
        if not field.data:
            raise ValidationError(
                'You must check the confirmation box to delete your account.')


class UserEditForm(FlaskForm):
    """Form for editing users."""

    # TODO: adding a file to send to S3, need to check how to do it
    # Currently only one hobby and interest can be selected

    username = StringField(
        'Username',
        validators=[Disabled(), Optional()]
    )
    profile_photo = FileField(
        'Profile Image (Optional)',
        validators=[
            Optional(),
            FileAllowed(["jpg", "png", "jpeg"], 'Images only (.png, .jpeg, .jpg)')]
    )

    bio = TextAreaField(
        'Tell us about yourself (Optional)',
        validators=[Optional(), Length(max=140)]
    )

    zipcode = StringField(
        'Zip Code',
        validators=[InputRequired(), Length(max=10)]
    )

    friend_radius = IntegerField(
        'Friend Radius',
        validators=[InputRequired(), NumberRange(min=1, max=100)]
    )

    interest = SelectField(
        'Interest',
        validators=[Optional()]
    )

    hobby = SelectField(
        'Hobby',
        validators=[Optional()]
    )

    password = PasswordField(
        'Password',
        validators=[InputRequired(), Length(min=6, max=50)],
    )
