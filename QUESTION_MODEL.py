class QuestionFetch:

    def __init__(self, text, answer):
        self.response = None
        self.question = text
        self.solution = answer

    def take_response(self, question_number):
        self.response = input(f"Q.{question_number}: {self.question} (True/False) : ")
