""""
    display module
"""

from flask_restful import Resource

from flask import request

from app.slack_lite.models import Blog

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
        

class Fetch(Resource,Blog, Supporter):
    """ Display all questions"""

    def get(self):
        content = self.container
        return self.response(content)


class FetchSpecific(Resource, Blog, Supporter):
    """ Display specific questions"""

    def get(self, questionId):
        try:
            spec=int(questionId)
        except ValueError:
            return('Non-numeric data found in the file.')
        else:
            for string in self.container:
                if string["id"] == spec:
                    return self.response(string)
            return("Sorry Id provide does not exist")


class AnswerSpecific(Resource, Blog, Supporter):
    """Post answer to specific question"""

    def post(self, questionId):

        try:
            spec = int(questionId)
        except ValueError:
            return('Non-numeric data found in the file.')
        else:
            for string in self.container:
                if string["id"] == spec:
                    # "comment" = self.response(string)
                    if request.content_type == 'application/json':
                        comment = request.get_json()
                        post = comment["Note"]
                        string["comment"] = post
                        return self.response("success")
                    return self.response("not success")

        return("Sorry Id provide does not exist")
