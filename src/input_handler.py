from src.questions import Questions

FRENCH_NOT_UNDERSTOOD = "Désolé mais je n'ai pas compris"
ENGLISH_NOT_UNDERSTOOD = "Sorry but I didn't understand"


def parse_input(req):
    message = req.lower()


def handle_input(user: object, req: str):
    question = user.question
    ret = question['fun'](user, req.lower())
    if type(ret) is str:
        user.question = question['next']
        return {
            'question': ret,
            'quick_replies': user.question['quick_replies'][user.lang] if 'quick_replies' in user.question else None
        }
    if ret is not True:
        return {
            'question': question['error'][user.lang],
            'quick_replies': question['quick_replies'][user.lang]
        }
    user.question = question['next']
    return {
        'question': user.question[user.lang],
        'quick_replies': user.question['quick_replies'][user.lang] if 'quick_replies' in user.question else None
    }


def start_conversation(user):
    question = user.question
    return {
        'question': question[user.lang],
        'quick_replies': user.question['quick_replies'][user.lang] if 'quick_replies' in user.question else None
    }
