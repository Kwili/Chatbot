import json

from enum import Enum

class Questions(Enum):
	START_CONVERSATION = 0 		# Bonjour et bienvenue sur Kwili etc etc
	BODYPART = 1 				# Où avez vous mal
	PAIN = 2 					# Echelle de 1 à 10
	DURATION = 3 				# Depuis quand avez vous mal
	FRENQUENCY = 4				# Souvent mal à cet endroit
	PERSONNAL = 5				# Souhaitez vous que je pose des questions personnelles pour avoir plus d'infos blabla
	HEIGHT = 6					# Quelle est votre taille
	WEIGHT = 7					# Quel est votre poids
	MEDICATION = 8				# Prenez vous actuellement des médicaments ?
	ALLERGIES = 9				# Avez-vous des allergies ?
	SMOKER = 10					# Êtes vous fumeur ?
	SEND_RECAP = 24				# Souhaitez-vous télécharger le récap
	FIND_DOCTOR = 25			# Souhaitez vous que je vous aide à trouver le doc
	END_CONVERSATION = 255		# Merci d'avoir utilisé Kwili, ciaos

questions = []

with open('src/questions.json') as json_file:
	questions = json.load(json_file)