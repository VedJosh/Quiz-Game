from DATA import question_data
from QUESTION_MODEL import QuestionFetch
from QUIZ_BRAIN import PointCalculatingJudge

#intializing the score to 0
score = 0
# iterating through each question
for question in question_data:
    # quizzer object created for each_question
    quizzer = QuestionFetch(question['text'], question['answer'])
    question_number = (question_data.index(question))+1
    # taking response from the user
    quizzer.take_response(question_number)
    # creating judge object who scores the user
    judge = PointCalculatingJudge(quizzer.response, quizzer.solution, question_number, score)
    judge.check_answer()
    score = judge.points
    # exiting the quiz with the score printed
    if question_number == 12:
        print("You have completed the quiz")
        print(f"Your final score was: {judge.points}/{question_number}")

