"""
endpoints linked in this file.

"""
from flask import Flask

from app.config import app_config

from app import posts

from flask import Blueprint

from flask_restful import Api

from app.views import Query, Fetch, FetchSpecific, AnswerSpecific

posts = Blueprint("posts", __name__)


# def create_app():
#     app_ = Flask(__name__)
#     return app_

def create_app():
    app_ = Flask(__name__)
    return app_


# app = create_app()
# app.config.from_object(app_config["development"])
# app.register_blueprint(posts)


app = create_app()
app.config.from_object(app_config["development"])
app.register_blueprint(posts)
api = Api(posts)

api.add_resource(Query, '/api/v1/questions')
api.add_resource(Fetch, '/api/v1/questions')
api.add_resource(FetchSpecific, '/api/v1/questions/<questionId>')
api.add_resource(AnswerSpecific, '/api/v1/questions/<questionId>/answers')
