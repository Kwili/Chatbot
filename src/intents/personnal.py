from src.keywords import yes, no

def ask_smoker(req):
	print('asking smoker')
	return True

def ask_allergies(req):
	print('asking allergies')
	return True

def ask_medication(req):
	print('asking medication')
	return True

def ask_weight(req):
	print('asking weight')
	return True

def ask_height(req):
	print('askin height')
	return True

def ask_consent(req: str):
	if yes.detect(req) is True:
		return True
	return False