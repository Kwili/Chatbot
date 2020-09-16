from src.keywords import yes, no


def frequency(user, req: str):
    if yes.detect(req) is True:
        user.profile.frequency = True
        return True
    if no.detect(req) is True:
        user.profile.frequency = False
        return True
    return False


def duration(user, req: str):
    nbs = [int(s) for s in req.split() if s.isdigit()]
    if len(nbs) > 0:
        n = nbs[0]
        pos = req.find(str(n))
        user.profile.duration = (req[pos:])
        return True
    return True


def level(user, req: str):
    nbs = [int(s) for s in req.split() if s.isdigit()]
    if len(nbs) > 0:
        user.profile.pain_level = nbs[0]
        return True
    return False
