from flask.ext.admin import BaseView, expose


class Dashboard(BaseView):
    """docstring for StaffDash"""

    @expose('/')
    def index(self):
        return self.render('index.html')
