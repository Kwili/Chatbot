YES_ARRAY_EN = [
	'yes',
	'please',
	'positive',
	'ye',
	'do it',
	'do'
]

YES_ARRAY_FR = [
	'oui',
	'positif',
	'stp',
	'ok',
	'yes',
	'fais-le'
]

def detect(lang, req: str):
	yes_array = YES_ARRAY_EN if lang == 'en' else YES_ARRAY_FR
	l = req.split(' ')
	for s in l:
		if s in yes_array:
			return True
	return False