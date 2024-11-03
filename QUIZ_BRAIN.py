class PointCalculatingJudge:
    def __init__(self, response_tkn, answer, question_num, point):
        self.response = response_tkn
        self.solution = answer
        self.points = point
        self.question_number = question_num

    def check_answer(self):
        if self.response == self.solution:
            print('you got it right!')
            self.points += 1
        else:
            print("That's Wrong")
        print(f"The correct answer was: {self.solution}")
        print(f"Your current score is: {self.points}/{self.question_number}")
