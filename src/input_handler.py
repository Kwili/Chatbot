from src.questions import Questions


def parse_input(req):
    message = req.lower()


def handle_input(user: object, req: str):
    question = user.question
    ret = question['fun'](user, req.lower())
    if type(ret) is str:
        user.question = question['next']
        return {
            'question': ret,
            'quick_replies': user.question['quick_replies'] if 'quick_replies' in user.question else None
        }
    if ret is not True:
        return {
            'question': 'Désolé mais je nai pas compris',
            'quick_replies': None
        }
    user.question = question['next']
    return {
        'question': user.question['fr'],
        'quick_replies': user.question['quick_replies'] if 'quick_replies' in user.question else None
    }


def start_conversation(user):
    question = user.question
    return {
        'question': question['fr'],
        'quick_replies': user.question['quick_replies'] if 'quick_replies' in user.question else None
    }
