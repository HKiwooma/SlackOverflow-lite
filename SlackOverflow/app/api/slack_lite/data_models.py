"""
    Data module or user flow

"""

class Blog():

    counter = [0]
    container = []
    questions = dict()
    answer = dict()
    incrementer = 1


    def data_post(self,question):
        """store post data"""
        self.container.append(question)
        return(self.container)

    def id_generator(self):
        """Question id generation"""

        self.counter[0] += 3
        return self.counter

    def post_answer(self): 
        """capturing posted answer"""
        pass

    def capture_question(self,question):
        """capturing question """
        if question != "":
            self.questions = {"id": self.id_generator(), "question": question}
            #question post
            self.data_post(self.questions)
            return True
        return False
    




