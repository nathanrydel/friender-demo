"""SQLAlchemy models for Friender."""

import os
from dotenv import load_dotenv

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

from geocoding import find_coordinates

bcrypt = Bcrypt()
db = SQLAlchemy()

load_dotenv()

DEFAULT_IMAGE_URL = f"{os.environ['S3_BUCKET_URL']}/default-pic.png"

def connect_db(app):
    """Connect database to provided Flask app.

    Call this in Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)

class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    username = db.Column(
        db.String(16),
        primary_key=True,
    )

    first_name = db.Column(
        db.String(25),
        nullable=False,
    )

    last_name = db.Column(
        db.String(25),
        nullable=False,
    )

    bio = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

    zipcode = db.Column(
        db.String(10),
        nullable=False,
        default="94020",
    )

    email = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    phone_number = db.Column(
        db.String(10),
        nullable=False,
        unique=True,
    )

    friend_radius = db.Column(
        db.Integer(),
        nullable=False,
        default=100,
    )

    profile_photo = db.Column(
        db.Text,
        nullable=False,
        default=DEFAULT_IMAGE_URL,
    )

    password = db.Column(
        db.String(100),
        nullable=False,
    )

    latitude = db.Column(
        db.Float,
        nullable=False,
    )

    longitude = db.Column(
        db.Float,
        nullable=False,
    )

    def __repr__(self):
        return f"<User: {self.username} at {self.email}>"

    @property
    def full_name(self):
        """Return full name of user."""

        return f"{self.first_name} {self.last_name}"

    @classmethod
    def signup(
        cls,
        username,
        email,
        password,
        zipcode,
        phone_number,
        first_name,
        last_name
    ):
        """Sign up user.

        Hashes password and adds user to session.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')


        location = find_coordinates(zipcode)

        if location:
            latitude = location.latitude
            longitude = location.longitude

        else:
            latitude = None
            longitude = None

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            zipcode=zipcode,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            latitude=latitude,
            longitude=longitude,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If this can't find matching user (or if password is wrong), returns
        False.
        """

        user = cls.query.filter_by(username=username).one_or_none()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class UserInterest(db.Model):
    """Interests on a User."""

    __tablename__ = "user_interests"

    user_username = db.Column(
        db.String(16),
        db.ForeignKey('users.username'),
        primary_key=True,
    )

    interest_code = db.Column(
        db.String(20),
        db.ForeignKey('interests.code'),
        primary_key=True,
    )


class Interest(db.Model):
    """Interests that can be added to users."""

    __tablename__ = 'interests'

    code = db.Column(
        db.String(20),
        primary_key=True,
    )

    name = db.Column(
        db.String(20),
        nullable=False,
    )

    users = db.relationship(
        'User',
        secondary="user_interests",
        backref="interests",
    )

    @classmethod
    def interest_choices(cls):
        """Return [(interests.code, interests.name), ...] to use as choices in form"""

        interests = cls.query.order_by("name").all()
        return [(interest.code, interest.name) for interest in interests]


class UserHobby(db.Model):
    """Hobbies on a User."""

    __tablename__ = "user_hobbies"

    user_username = db.Column(
        db.String(16),
        db.ForeignKey('users.username'),
        primary_key=True,
    )

    hobby_code = db.Column(
        db.String(20),
        db.ForeignKey('hobbies.code'),
        primary_key=True,
    )


class Hobby(db.Model):
    """Hobbies that can be added to users."""

    __tablename__ = 'hobbies'

    code = db.Column(
        db.String(20),
        primary_key=True,
    )

    name = db.Column(
        db.String(20),
        nullable=False,
    )

    users = db.relationship(
        'User',
        secondary="user_hobbies",
        backref="hobbies",
    )

    @classmethod
    def hobby_choices(cls):
        """Return [(hobby.code, hobby.name), ...] to use as choices in form"""

        hobbies = cls.query.order_by("name").all()
        return [(hobby.code, hobby.name) for hobby in hobbies]


class UserPhoto(db.Model):
    """Photos on a User."""

    __tablename__ = "user_photos"

    # TODO: check to see how to limit to 6 photos per user
    # __table_args__ = (
    #     CheckConstraint('photos_id <= 6', name='chk_max_user_photos'),
    # )

    user_username = db.Column(
        db.String(16),
        db.ForeignKey('users.username'),
        primary_key=True,
    )

    photos_id = db.Column(
        db.Integer,
        db.ForeignKey('photos.id'),
        primary_key=True,
    )


class Photo(db.Model):
    """ User added photos """

    __tablename__ = "photos"

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    url = db.Column(
        db.String(2000),
        nullable=False,
    )


