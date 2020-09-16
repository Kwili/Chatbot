no_array_fr = [
	'non',
	'négatif',
	'no',
	'nop',
	'pas'
]

def detect(req: str):
	l = req.split(' ')
	for s in l:
		ss = s
		if s.endswith('s'):
			ss = s[:-1]
		if ss in no_array_fr:
			return True
	return False