from src.questions import Questions
from src.history import History


class Profile:
    def __init__(self):
        self.pain_level: int
        self.bodypart: str
        self.duration: int
        self.frequency: int
        self.height: int
        self.weight: int
        self.medication: str
        self.allergies: str
        self.smoker: str



class User:
    def __init__(self, sid):
        self.sid = sid
        self.question = Questions.START_CONVERSATION
        self.history = History()
        self.profile = Profile()

    def update_history(self, history):
        self.history = history


users = []


def add_user(sid):
    users.append(User(sid))


def find_user(sid):
    return next((x for x in users if x.sid == sid), None)


def pop_user(sid):
    pass
