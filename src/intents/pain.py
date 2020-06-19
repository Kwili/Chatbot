from src.keywords import yes, no

def frequency(req: str):
	return True

def duration(req: str):
	nbs = [int(s) for s in req.split() if s.isdigit()]
	if len(nbs) > 0:
		n = nbs[0]
		pos = req.find(str(n))
		print(req[pos:]) # J'ai mal depuis 4 semaines -> 4 semaines
		return True
	return True


def level(req: str):
	nbs = [int(s) for s in req.split() if s.isdigit()]
	if len(nbs) > 0:
		print('pain level: ', nbs[0])
		return True
	return False