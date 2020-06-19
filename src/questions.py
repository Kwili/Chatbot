from src.intents import start_conversation, bodypart, pain, personnal, recap

class Questions:

	END_CONVERSATION = {
		'next': None,
		'fun': None,
		'fr': 'Merci davoir utilisé Kwili, bye bye',
		'en': 'not yet'
	}

	FIND_DOCTOR = {
		'next': END_CONVERSATION,
		'fun': None,
		'fr': 'Souhaitez-vous que je vous aide à trouver un docteur ?',
		'en': 'not yet'
	}

	SEND_RECAP = {
		'next': END_CONVERSATION,
		'fun': recap.send_recap,
		'fr': 'Souhaitez-vous télécharger le document ?',
		'en': 'not yet'
	}

	SMOKER = {
		'next': SEND_RECAP,
		'fun': personnal.ask_smoker,
		'fr': 'Etes vous fumeur ?',
		'en': 'not yet'
	}

	ALLERGIES = {
		'next': SMOKER,
		'fun': personnal.ask_allergies,
		'fr': 'Avez-vous des allergies ?',
		'en': 'not yet'
	}

	MEDICATION = {
		'next': ALLERGIES,
		'fun': personnal.ask_medication,
		'fr': 'Prenez vous actuellement des médicaments ?',
		'en': 'not yet'
	}

	WEIGHT = {
		'next': MEDICATION,
		'fun': personnal.ask_weight,
		'fr': 't gros ?',
		'en': 'not yet'
	}

	HEIGHT = {
		'next': WEIGHT,
		'fun': personnal.ask_height,
		'fr': 'Quelle tailles fais-tu',
		'en': 'not yet'
	}

	PERSONNAL = {
		'next': HEIGHT,
		'fun': personnal.ask_consent,
		'fr': 'Souhaitez vous que je pose des questions personnelles pour avoir plus dinfos blabla',
		'en': 'not yet'
	}

	FREQUENCY = {
		'next': PERSONNAL,
		'fun': pain.frequency,
		'fr': 'Avez-vous souvent mal à cet endroit ?',
		'en': 'not yet'
	}

	DURATION = {
		'next': FREQUENCY,
		'fun': pain.duration,
		'fr': 'Depuis quand avez-vous mal ?',
		'en': 'not yet'
	}

	PAIN_LEVEL = {
		'next': DURATION,
		'fun': pain.level,
		'fr': 'Sur une échelle de 1 à 10',
		'en': 'not yet'
	}

	BODYPART = {
		'next': PAIN_LEVEL,
		'fun': bodypart.bodypart,
		'fr': 'Où avez-vous mal?',
		'en': 'proutlol'
	}
 
	START_CONVERSATION = {
		'next': BODYPART, #Utilise un objet de next pour la question précédente en fonction de douleur/brulure/maladie etc
		'fun': start_conversation.detect_intent,
		'fr': 'Bonjour et bienvenue sur Kwili, comment puis-je vous aider ?',
		'en': 'Hello and welcome on Kwili'
	}

	""" {
		hurt: BODYPART,
		sick: BODYPART,
		burned: BODYPART
	}
	"""