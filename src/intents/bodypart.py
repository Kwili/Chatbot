BP_ARRAY_FR = [
    'tête', 'dos', 'cou', 'ventre',
    'bras', 'cheveux', 'cil', 'cœur', 'doigt', 'coeur', 'front', 'genou',
    'nez', 'ongle', 'pied', 'poignet', 'sang', 'sourcil', 'visage', 'œil',
    'oeil', 'yeux', 'tete',
    'barbe', 'bouche', 'cheville', 'dent', 'épaule', 'fesses', 'fesse', 'gorge',
    'jambe', 'joue', 'langue', 'lèvre', 'main', 'moustache', 'oreille', 'peau',
    'poitrine',
]

BP_ARRAY_EN = [
    'head', 'back', 'neck', 'belly',
    'arm', 'hair', 'eyelash', 'heart', 'finger', 'forehead', 'knee',
    'nose', 'nail', 'feet', 'wrist', 'blood', 'eyebrow', 'face', 'eye', 'eyes',
    'beard', 'mouth', 'ankle', 'teeth', 'tooth', 'shoulder', 'bottom', 'buttocks', 'throat',
    'leg', 'cheek', 'tongue', 'lip', 'lips', 'head', 'mustache', 'ear', 'ears', 'skin', 'chest',
]


def detect_bodypart(lang, req):
    bp_array = BP_ARRAY_EN if lang == 'en' else BP_ARRAY_FR
    l = req.split(' ')
    for s in l:
        ss = s
        if s in bp_array:
            return s
        if s.endswith('s'):
            ss = s[:-1]
        if ss in bp_array:
            return s
    return None


def bodypart(user, req):
    ret = detect_bodypart(user.lang, req)
    if ret is not None:
        user.profile.bodypart = ret
        return True
    return False
