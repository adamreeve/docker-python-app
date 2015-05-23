from   flask import Flask
import logging

from hello.database import ScopedSession
from hello.data import auth


def create_app(config):
    app = Flask("hello")
    app.config.from_object(config)

    @app.route("/")
    def hello():
        users = auth.User.query.all()
        user_list = ",".join(u.email for u in users)
        output = "Hello World! Got {0} users:{1}".format(len(users), user_list)
        return output

    @app.before_first_request
    def setup_logging():
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
            ScopedSession.remove()

    return app
