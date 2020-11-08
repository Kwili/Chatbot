# Intentions

Ce fichier décrit les différents fonctions d'analyse utilisées lors d'une question.

Ces fonctions sont disponibles dans le module `intents`, et dans leur fichiers associés.

Elles permettent d'obtenir l'information recherchée dans la réponse utilisateur.

Par exemple, lors de la question `BODYPART`, la fonction associée est `bodypart`, disponible dans le fichier `bodypart.py`.

```python
def detect_bodypart(req):
	l = req.split(' ')
	for s in l:
		ss = s
		if s in BP_ARRAY_FR:
			return s
		if s.endswith('s'):
			ss = s[:-1]
		if ss in BP_ARRAY_FR:
			return s
	return None


def bodypart(req):
	ret = detect_bodypart(req)
	if ret is not None:
		return True
	return False
```

Cette fonction compare chaque mot de la réponse de l'utilisateur à un array défini, afin de trouver la partie du corps concernée. Si la partie du corps est identifiée, la valeur `True` est renvoyée, et l'information est enregistrée sur le profil utilisateur.
Sinon, la valeur `False` est renvoyée, et un message d'erreur sera donc produit.
