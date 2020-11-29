NO_ARRAY_EN = [
	'no',
	'negative',
	'dont',
	'don\'t',
	'disagree'
]

NO_ARRAY_FR = [
	'non',
	'négatif',
	'no',
	'nop',
	'pas'
]

def detect(lang, req: str):
	no_array = NO_ARRAY_EN if lang == 'en' else NO_ARRAY_FR
	l = req.split(' ')
	for s in l:
		if s in no_array:
			return True
	return False