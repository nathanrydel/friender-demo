"""SQLAlchemy models for Friender."""

import os
from dotenv import load_dotenv

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy  # , CheckConstraint

bcrypt = Bcrypt()
db = SQLAlchemy()

load_dotenv()

DEFAULT_IMAGE_URL = f"{os.environ['S3_BUCKET_URL']}/default-pic.png"


class User(db.Model):
    """Site user."""

    __tablename__ = "users"

    username = db.Column(
        db.String(16),
        primary_key=True)

    first_name = db.Column(
        db.String(25),
        nullable=False)

    last_name = db.Column(
        db.String(35),
        nullable=False)

    bio = db.Column(
        db.Text,
        nullable=False,
        default="",
    )

    zipcode = db.Column(
        db.String(10),
        nullable=False,
        default="",
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
        default=DEFAULT_IMAGE_URL
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

        user = User(
            username=username,
            email=email,
            password=hashed_pwd,
            zipcode=zipcode,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name
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


# class UserInterest(db.Model):
#     """Interests on a User."""

#     __tablename__ = "user_interests"

#     user_username = db.Column(
#         db.String(16),
#         db.ForeignKey('users.username'),
#         primary_key=True)

#     interest_name = db.Column(
#         db.String(20),
#         db.ForeignKey('interest.name'),
#         primary_key=True)


# class Interest(db.Model):
#     """Interests that can be added to users."""

#     __tablename__ = 'interests'

#     name = db.Column(
#         db.Str(20),
#         primary_key=True)

#     users = db.relationship(
#         'User',
#         secondary="users_interests",
#         backref="interests",
#     )


# class UserHobbies(db.Model):
#     """Hobbies on a User."""

#     __tablename__ = "user_hobbies"

#     user_username = db.Column(
#         db.String(16),
#         db.ForeignKey('users.username'),
#         primary_key=True)

#     hobbies_name = db.Column(
#         db.String(20),
#         db.ForeignKey('hobbies.name'),
#         primary_key=True)


# class Hobbies(db.Model):
#     """Hobbies that can be added to users."""

#     __tablename__ = 'hobbies'

#     name = db.Column(
#         db.Str(20),
#         primary_key=True)

#     users = db.relationship(
#         'User',
#         secondary="users_hobbies",
#         backref="hobbies",
#     )


# class UserPhotos(db.Model):
#     """Photos on a User."""

#     __tablename__ = "user_photos"

#     # TODO: check to see how to limit to 6 photos per user
#     # __table_args__ = (
#     #     CheckConstraint('photos_id <= 6', name='chk_max_user_photos'),
#     # )

#     user_username = db.Column(
#         db.String(16),
#         db.ForeignKey('users.username'),
#         primary_key=True)

#     photos_id = db.Column(
#         db.Integer,
#         db.ForeignKey('photos.name'),
#         primary_key=True)


# class Photos(db.Model):
#     """ User added photos """

#     __tablename__ = "photos"

#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#         auto_increment=True)

#     url = db.Column(
#         db.String(2000),
#         nullable=False,
#     )


def connect_db(app):
    """Connect database to provided Flask app.

    Call this in Flask app.
    """

    app.app_context().push()
    db.app = app
    db.init_app(app)
