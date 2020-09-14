from src.questions import Questions
from src.history import History


class Profile:
    def __init__(self):
        self.pain_level: int = 0
        self.bodypart: str = ''
        self.duration: int = 0
        self.frequency: bool = False
        self.height: str = ''
        self.weight: str = ''
        self.medication: str = ''
        self.allergies: str = ''
        self.smoke: int = 0

    def __repr__(self):
        return 'Bodypart: ' + self.bodypart + '\nPain Level: ' + str(self.pain_level) \
            + '\nDuration: ' + str(self.duration) + '\nFrequency: ' + str(self.frequency) \
            + '\nHeight: ' + self.height + '\nWeight: ' + self.weight + '\nMedication: ' + self.medication \
            + '\nAllergies: ' + self.allergies + '\nSmoker: ' + str(self.smoke)


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
