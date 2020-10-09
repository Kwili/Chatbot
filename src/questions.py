from src.intents import start_conversation, bodypart, pain, personnal
from src.pdf import recap


class Questions:

    END_CONVERSATION = {
        'next': None,
        'fun': None,
        'fr': 'Merci davoir utilisé Kwili, bonne journée!',
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
        'fr': 'Souhaitez-vous que ces informations soient rédigées dans un document présentable \
                aux urgences ? Une fois le document téléchargé, vos informations seront supprimées.',
        'en': 'not yet'
    }

    SMOKER = {
        'next': SEND_RECAP,
        'fun': personnal.ask_smoker,
        'fr': 'Est-ce que vous fumez ? Si oui, combien de fois par semaine ? Si non, indiquez 0.',
        'en': 'not yet'
    }

    ALLERGIES = {
        'next': SMOKER,
        'fun': personnal.ask_allergies,
        'fr': 'Avez-vous des allergies ? Si oui, lesquelles ?',
        'en': 'not yet'
    }

    HAS_ALLERGIES = {
        'next': ALLERGIES,
        'fun': personnal.ask_allergies,
        'fr': 'Avez-vous des allergies ? Si oui, lesquelles ?',
        'en': 'not yet'
    }

    MEDICATION = {
        'next': HAS_ALLERGIES,
        'fun': personnal.ask_medication,
        'fr': 'Prenez vous actuellement des médicaments ? Si oui, lesquels ?',
        'en': 'not yet'
    }

    HAS_MEDICATION = {
        'next': ALLERGIES,
        'fun': personnal.ask_medication,
        'fr': 'Prenez vous actuellement des médicaments ? Si oui, lesquels ?',
        'en': 'not yet'
    }

    WEIGHT = {
        'next': HAS_MEDICATION,
        'fun': personnal.ask_weight,
        'fr': 'Quel est votre poids ?',
        'en': 'not yet'
    }

    HEIGHT = {
        'next': WEIGHT,
        'fun': personnal.ask_height,
        'fr': 'Quelle taille faites-vous ?',
        'en': 'not yet'
    }

    PERSONNAL = {
        'next': HEIGHT,
        'fun': personnal.ask_consent,
        'fr': 'Souhaitez vous que je pose des questions personnelles pour écrire un compte-rendu plus précis ?',
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
        'fr': 'Sur une échelle de 1 à 10, à combien évaluriez-vous votre douleur ?',
        'en': 'not yet'
    }

    BODYPART = {
        'next': PAIN_LEVEL,
        'fun': bodypart.bodypart,
        'fr': 'Où avez-vous mal?',
        'en': 'Where are you hurt ?'
    }

    START_CONVERSATION = {
        'next': BODYPART,
        'fun': start_conversation.detect_intent,
        'fr': 'Comment puis-je vous aider ?',
        'en': 'Hello and welcome on Kwili'
    }
