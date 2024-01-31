import os
from dotenv import load_dotenv

from flask import (
    Flask, render_template, request, flash, redirect, session, g, abort,
)
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import (
    UserAddForm, UserEditForm, LoginForm, MessageForm, CSRFProtection,
)
from models import (
    db, connect_db, User, Message, DEFAULT_IMAGE_URL, DEFAULT_HEADER_IMAGE_URL)

load_dotenv()

CURR_USER_KEY = "curr_user"