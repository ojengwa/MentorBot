from flask import (
    render_template,
    current_app as app,
    jsonify
)
from flask.ext.classy import FlaskView
# import mentorapp

# from flask_oauth2_login import GoogleLogin


class UserView(FlaskView):

    """docstring for UserView"""

    def index(self):
        return render_template('users/index.html')
