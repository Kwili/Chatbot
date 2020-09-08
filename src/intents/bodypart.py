bp_array_fr = [
    'bras', 'cheveu', 'cil', 'cœur', 'coeur', 'doigt', 'dos', 'front', 'genou',
    'nez', 'ongle', 'pied', 'poignet', 'sang', 'sourcil', 'visage', 'œil',
    'oeil', 'yeux'
    'barbe', 'bouche', 'cheville', 'dent', 'épaule', 'fesses', 'fesse', 'gorge',
    'jambe', 'joue', 'langue', 'lèvre', 'main', 'moustache', 'oreille', 'peau',
    'poitrine', 'tête'
]

bp_array_en = []


def detect_bodypart(req):
    l = req.split(' ')
    for s in l:
        ss = s
        if s in bp_array_fr:
            return s
        if s.endswith('s'):
            ss = s[:-1]
        if ss in bp_array_fr:
            return s
    return None


def bodypart(user, req):
    ret = detect_bodypart(req)
    if ret is not None:
		user.profile.bodypart = ret
        return True
    return False
