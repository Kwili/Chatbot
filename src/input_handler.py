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
            'quick_replies': user.question['quick_replies'][user.lang] if user.question['quick_replies'] is not None else None
        }
    if ret is not True:
        return {
            'question': question['error'][user.lang],
            'quick_replies': question['quick_replies'][user.lang]
        }
    user.question = question['next']
    return {
        'question': user.question[user.lang],
        'quick_replies': user.question['quick_replies'][user.lang] if user.question['quick_replies'] is not None else None
    }


def start_conversation(user):
    question = user.question
    return {
        'question': question[user.lang],
        'quick_replies': user.question['quick_replies'][user.lang] if user.question['quick_replies'] is not None else None
    }
