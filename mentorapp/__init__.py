import os

from flask import (
    render_template,
    # redirect,
    # url_for,
    # session,
    jsonify,
    # current_app as appp
)
from flask.ext.admin import Admin
from flask.ext.bcrypt import Bcrypt
from flask_oauth2_login import GoogleLogin
from flask_login import (
    LoginManager,
)

# from models.user import User
from factories import create_app
from mentorapp.views import (
    admin as admin_views,
    user as user_views
)


dev_env = os.getenv('ENV', default='dev')
app = create_app(__name__, dev_env)
login_manager = LoginManager(app)


# Initialise extensions for the app
admin = Admin(app)
bcrypt = Bcrypt(app)
google = GoogleLogin(app)
app.google = google
db = app.db

# Register the routes for the admin views
admin.add_view(admin_views.Dashboard())

# Register views for the User page
user_views.UserView.register(app)


@app.route('/')
def index():
    google = app.google
    return render_template('index.html', **locals())


@google.login_success
def login_success(token, profile):
    print(token)
    return jsonify(token=token, profile=profile)


@google.login_failure
def login_failure(e):
    print(e)
    return jsonify(error=str(e))
