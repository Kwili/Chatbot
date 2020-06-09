from src.questions import Questions

class User:
	def __init__(self, sid):
		self.sid = sid
		self.next_question = Questions.START_CONVERSATION
		self.history = []
	
	def update_history(self, history):
		self.history = history

users = []

def add_user(sid):
	users.append(User(sid))

def find_user(sid):
	return next((x for x in users if x.sid == sid), None)