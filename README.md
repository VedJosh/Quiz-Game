# True/False Quiz
Overview
This Python application is a command-line True/False quiz designed to test your knowledge on various interesting facts. Users will answer a series of questions and receive immediate feedback, along with a final score at the end of the quiz.

# Features
True/False Questions: Answer questions that require a simple true or false response.
Score Tracking: Track your score and get feedback after each question.
User-Friendly Interface: Simple prompts guide you through the quiz.

# Requirements
Python 3.6 or higher

# Usage
Run the quiz application:
Respond to each question by typing True or False.
At the end of the quiz, your total score will be displayed.

# Code Structure
DATA.py: Contains the list of questions and answers.
QUESTION_MODEL.py: Includes the QuestionFetch class for handling question text and user responses.
QUIZ_BRAIN.py: Houses the PointCalculatingJudge class for scoring user answers.
main.py: The entry point of the application, orchestrating the quiz flow.
