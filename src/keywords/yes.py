yes_array_en = [
	'yes',
	'please',
	'positive'
]

yes_array_fr = [
	'oui',
	'positif',
	'stp',
	'ok',
	'yes',
	'fais-le'
]

def detect(req: str):
	l = req.split(' ')
	for s in l:
		ss = s
		if s.endswith('s'):
			ss = s[:-1]
		if ss in yes_array_fr:
			return True
	return False