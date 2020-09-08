from src.questions import Questions


def parse_input(req):
    message = req.lower()


def send_question(question):
    print('I should send in the next question')


def handle_input(user: object, req: str):
    question = user.question
    ret = question['fun'](user, req.lower())
    if ret is not True:
        return 'Désolé mais je nai pas compris'
    user.question = question['next']
    return user.question['fr']


def start_conversation(user):
    question = user.question
    return question['fr']
