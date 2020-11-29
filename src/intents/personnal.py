from src.keywords import yes, no
from src.lib import detect_numbers


def ask_smoker(user, req):
    user.profile.smoke = req
    return True


def ask_allergies(user, req):
    user.profile.allergies = req
    return True


def has_allergies(user, req):
    return True


def ask_medication(user, req):
    user.profile.medication = req
    return True


def has_medication(user, req):
    return True


def ask_weight(user, req):
    weight = detect_numbers(req)
    if weight is not None:
        user.profile.weight = weight
        return True
    return False


def ask_height(user, req):
    height = detect_numbers(req)
    if height is not None:
        user.profile.height = height
        return True
    return False


def ask_consent(user, req: str):
    if yes.detect(user.lang, req) is True:
        return True
    if no.detect(user.lang, req) is True:
        return True, False
    return False
