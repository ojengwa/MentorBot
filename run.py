from flask.ext.script import Manager
from mentorapp import app


manager = Manager(app)


@manager.command
def test_hello():
    print('Hello')


if __name__ == '__main__':
    manager.run()
