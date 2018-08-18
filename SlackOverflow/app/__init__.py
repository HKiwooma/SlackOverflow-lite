from flask import Flask

from app.config import app_config

from app.api.slack_lite import posts


def create_app():
    app_ = Flask(__name__)
    return app_


app = create_app()
app.config.from_object(app_config["development"])
app.register_blueprint(posts)
