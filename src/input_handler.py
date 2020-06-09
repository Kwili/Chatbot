from src.history import History
from src.questions import Questions, questions

history = History()

def parse_input(req):
	message = req.lower()

def send_question(next_question):
	print('I should send in the next question')

def handle_input(user, req):
	question = user.next_question
	next_question_idx = int(question.value) + 1
	user.next_question = Questions(next_question_idx)
	return questions[question.name]['text']