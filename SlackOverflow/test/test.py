import unittest

import json

from app import app


class ApiTest(unittest.TestCase):

    def setUp(self):
        self.info = {"Note": "How can i install pylint"}
        self.client = app.test_client(self)

    def test_add_answer(self):
        questionId = 4
        result = self.client.get('/api/v1/questions/{}'.format(questionId), content_type='application/json')
        self.assertEqual(result.status_code, 200)
    
    def test_add_questions(self):
        result = self.client.post('/api/v1/questions', data=json.dumps(self.info), content_type='application/json')
        self.assertEqual(result.status_code, 200)

    def test_a_question_validity(self):
        result = self.client.post('/api/v1/questions', data="", content_type='application/json')
        self.assertEqual(result.status_code, 400)

    def test_add_a_question(self):
        qtnId = "what is pysec"
        result = self.client.get('/api/v1/questions/{}'.format(qtnId), content_type = 'application/json')
        self.assertEqual(result.status_code, 200)





