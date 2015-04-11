from factories import init_app
from flask.ext.admin import Admin
from app.views import admin as admin_views
import os


dev_env = os.getenv('ENV', default='dev')
app = init_app(__name__, dev_env)
admin = Admin(app)

# Register the routes for the admin views
admin.add_view(admin_views.Dashboard())
