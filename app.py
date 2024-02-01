import os
from dotenv import load_dotenv

from flask import (
    Flask, render_template, request, flash, redirect, session, g
)
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import (
    CSRFProtection, UserAddForm, UserEditForm, LoginForm,
)
from models import (
    db, connect_db, User, Hobby, Interest, UserHobby, UserInterest)  # , UserPhoto)

from upload import upload_file, S3_BUCKET_URL

# import uuid
from werkzeug.utils import secure_filename

load_dotenv()

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
toolbar = DebugToolbarExtension(app)

connect_db(app)


##############################################################################
# User signup/login/logout

@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


@app.before_request
def add_csrf_only_form():
    """Add a CSRF-only form so that every route can use it."""

    g.csrf_form = CSRFProtection()


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.username


def do_logout():
    """Log out user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username, phone number,
    or email: flash message and re-present form.
    """
# TODO: Same username, phone#, email (all unique) + do we want to allow
    # bio + friend_radius added on signup

    if g.user:
        return redirect('/users/{g.user.username}')

    do_logout()

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
                first_name=form.first_name.data,
                last_name=form.last_name.data,
                zipcode=form.zipcode.data,
                phone_number=form.phone_number.data,
            )
            db.session.commit()
# FIXME: outdated
        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login and redirect to homepage on success."""

    form = LoginForm()

    if g.user:
        return redirect('/')

# TODO: further-study add login by phone number and email
    if form.validate_on_submit():
        user = User.authenticate(
            form.username.data,
            form.password.data,
        )

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.post('/logout')
def logout():
    """Handle logout of user and redirect to homepage."""

    form = g.csrf_form

    if not form.validate_on_submit() or not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/")


##############################################################################
# General user routes:

@app.get('/users')
def list_users():
    """Page with listing of users.

    Can take a 'q' param in querystring to search by that username.
    """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    search = request.args.get('q')

# FIXME: looking at username vs first/last name
    if not search:
        users = User.query.all()
    else:
        users = User.query.filter(User.username.like(f"%{search}%")).all()

    return render_template('users/index.html', users=users)


@app.get('/users/<username>')
def show_user(username):
    """Show user profile."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = User.query.get_or_404(username)

    return render_template('users/profile.html', user=user)


@app.route('/users/<username>/edit', methods=["GET", "POST"])
def edit_profile(username):
    """Update profile for current user.

    Redirect to user page on success.
    """

    if not g.user.username == username:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    user = g.user
    form = UserEditForm(obj=user)
    form.hobby.choices = Hobby.hobby_choices()
    form.interest.choices = Interest.interest_choices()

    if form.validate_on_submit():
        if User.authenticate(user.username, form.password.data):
            user.bio = form.bio.data
            user.friend_radius = form.friend_radius.data
            user.zipcode = form.zipcode.data

            if form.profile_photo.data:

                file = form.profile_photo.data
                # FIXME: potential name collision if file name is globally unique
                # Potentially use uuid to fix?
                file_name = secure_filename(file.filename)

                file_path = os.path.join(
                    app.root_path, 'temp_photos', file_name)
                file.save(file_path)

                if upload_file(file_path):
                    user.profile_photo = S3_BUCKET_URL + "/" + file_name
                    os.remove(file_path)

                else:
                    flash("Failed to upload profile photo", "danger")

            if form.interest.data:
                print("############## form.interest.data")
                print(user.username, form.interest.data)
                if not UserInterest.query.filter_by(user_username=user.username, interest_code=form.interest.data).first():

                    new_interest = UserInterest(
                        user_username=user.username,
                        interest_code=form.interest.data
                    )
                    db.session.add(new_interest)

            if form.hobby.data:
                if not UserHobby.query.filter_by(user_username=user.username, hobby_code=form.hobby.data).first():
                    new_hobby = UserHobby(
                        user_username=user.username,
                        hobby_code=form.hobby.data
                    )
                    db.session.add(new_hobby)

            db.session.commit()
            return redirect(f"/users/{user.username}")

        flash("Wrong password, please try again.", 'danger')

    return render_template('users/edit.html',
                           form=form,
                           username=user.username)


@app.post('/users/delete')
def delete_user():
    """Delete user.

    Redirect to signup page.
    """

    form = g.csrf_form

    if not form.validate_on_submit() or not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    do_logout()

    # Message.query.filter_by(username=g.user.username).delete()
    db.session.delete(g.user)
    db.session.commit()

    return redirect("/signup")


##############################################################################
# Homepage and error pages


@app.get('/')
def homepage():
    """Show homepage"""

    if g.user:
        return render_template('home.html')

    else:
        return render_template('home-anon.html')


@app.errorhandler(404)
def page_not_found(e):
    """404 NOT FOUND page."""

    return render_template('404.html'), 404


@app.after_request
def add_header(response):
    """Add non-caching headers on every request."""

    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control
    response.cache_control.no_store = True
    return response
