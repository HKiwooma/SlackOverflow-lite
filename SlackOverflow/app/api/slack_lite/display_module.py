""""
    display module
"""

from flask_restful import Resource

from flask import request

from app.api.slack_lite.data_models import Blog

from flask import jsonify, make_response


class Supporter:
    """supports display module"""

    def response(self, status):
        json_conv = jsonify({"status": status})
        return make_response(json_conv)


class Query(Resource, Blog, Supporter):

    def post(self):
        """post question"""

        if request.content_type == 'application/json':
            message = request.get_json()
            post = message["Note"]
            if self.capture_question(post):
                return self.response("Bravo! Your question is posted.")
            return self.response("Enble to display question sorry!")
        
