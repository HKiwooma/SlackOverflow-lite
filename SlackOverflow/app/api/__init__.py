"""
endpoints linked in this file.

"""
from flask import Blueprint

from flask_restful import Api

from app.api.views import Query, Fetch, FetchSpecific, AnswerSpecific


posts = Blueprint("posts", __name__)

api = Api(posts)

api.add_resource(Query, '/api/v1/questions')
api.add_resource(Fetch, '/api/v1/questions')
api.add_resource(FetchSpecific, '/api/v1/questions/<questionId>')
api.add_resource(AnswerSpecific, '/api/v1/questions/<questionId>/answers')


