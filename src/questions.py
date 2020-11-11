from src.intents import start_conversation, bodypart, pain, personnal
from src.intents.bodypart import BP_ARRAY_FR, BP_ARRAY_EN
from src.pdf import recap


def single_reply(title, value = None):
    return {
        'title': title,
        'value': value if value != None else title
    }

class Questions:

    END_CONVERSATION = {
        'next': None,
        'fun': None,
        'fr': 'Merci davoir utilisé Kwili, bonne journée!',
        'en': 'Thanks for using Kwili! Have a good day.',
        'error': None,
        'quick_replies': None
    }

    FIND_DOCTOR = {
        'next': END_CONVERSATION,
        'fun': None,
        'fr': 'Souhaitez-vous que je vous aide à trouver un docteur ?',
        'en': 'Do you need help finding a doctor ?',
        'error': {
            'fr': "Désolé je n'ai pas compris. Vous pouvez me répondre par un simple 'oui' ou 'non'",
            'en': "Sorry I did not understand. You can answer by a simple 'yes' or 'no'"
        },
        'quick_replies': {
            'fr': [
                single_reply('oui'),
                single_reply('non')
            ],
            'en': [
                single_reply('yes'),
                single_reply('no'),
            ]
        }
    }

    SEND_RECAP = {
        'next': END_CONVERSATION,
        'fun': recap.send_recap,
        'fr': 'Souhaitez-vous que ces informations soient rédigées dans un document présentable \
                aux urgences ? Une fois le document téléchargé, vos informations seront supprimées.',
        'en': 'Do you want these informations to be written in a recap ? Once downloaded, your informations will be deleted.',
        'error': {
            'fr': "Désolé je n'ai pas compris. Vous pouvez me répondre par un simple 'oui' ou 'non'",
            'en': "Sorry I did not understand. You can answer by a simple 'yes' or 'no'"
        },
        'quick_replies': {
            'fr': [
                single_reply('oui'),
                single_reply('non')
            ],
            'en': [
                single_reply('yes'),
                single_reply('no'),
            ]
        }
    }

    SMOKER = {
        'next': SEND_RECAP,
        'fun': personnal.ask_smoker,
        'fr': 'Est-ce que vous fumez ? Si oui, combien de fois par semaine ? Si non, indiquez 0.',
        'en': "Are you a smoker ? If so, how many times do you smoke per week ? If you don't, answer 0",
        'error': {
            'fr': "Désolé mais je n'ai pas compris. Combien de fois fumez-vous par semaine ?",
            'en': "Sorry I did not understand that. How many times do you smoke per week ?"
        },
        'quick_replies': {
            'fr': [
                single_reply('0'),
                single_reply('5'),
                single_reply('16'),
            ],
            'en': [
                single_reply('0'),
                single_reply('5'),
                single_reply('16'),
            ]
        }
    }

    ALLERGIES = {
        'next': SMOKER,
        'fun': personnal.ask_allergies,
        'fr': 'Avez-vous des allergies ? Si oui, lesquelles ?',
        'en': 'Do you have any allergies ? If so, which ones ?',
        'error': {
            'fr': "Désolé mais je n'ai pas quelles étaient vos allergies.",
            'en': "Sorry but I didn't understand your reply."
        },
        'quick_replies': {
            'fr': [
                single_reply('non'),
                single_reply('arachides'),
                single_reply('blé'),
                single_reply('pollen'),
            ],
            'en': [
                single_reply('no'),
                single_reply('peanuts'),
                single_reply('wheat'),
                single_reply('pollen'),
            ]
        }
    }

    HAS_ALLERGIES = {
        'next': ALLERGIES,
        'fun': personnal.ask_allergies,
        'fr': 'Avez-vous des allergies ? Si oui, lesquelles ?',
        'en': 'Do you have any allergies ? If so, which ones ',
        'error': {
            'fr': "Désolé mais je n'ai pas quelles étaient vos allergies.",
            'en': "Sorry but I didn't understand your reply."
        },
        'quick_replies': {
            'fr': [
                single_reply('non'),
                single_reply('arachides'),
                single_reply('blé'),
                single_reply('pollen'),
            ],
            'en': [
                single_reply('no'),
                single_reply('peanuts'),
                single_reply('wheat'),
                single_reply('pollen'),
            ]
        }
    }

    MEDICATION = {
        'next': HAS_ALLERGIES,
        'fun': personnal.ask_medication,
        'fr': 'Prenez vous actuellement des médicaments ? Si oui, lesquels ?',
        'en': 'Are you currently taking a medication ?',
        'error': {
            'fr': "Désolé mais je n'ai pas compris quels médicaments vous preniez.",
            'en': "Sorry but I didn't understand your reply."
        },
        'quick_replies': {
            'fr': [
                single_reply('non'),
                single_reply('morphine'),
                single_reply('imodium'),
                single_reply('levothyrox'),
            ],
            'en': [
                single_reply('no'),
                single_reply('morphine'),
                single_reply('imodium'),
                single_reply('levothyrox'),
            ]
        }
    }

    HAS_MEDICATION = {
        'next': ALLERGIES,
        'fun': personnal.ask_medication,
        'fr': 'Prenez vous actuellement des médicaments ? Si oui, lesquels ?',
        'en': 'Are you currently taking a medication ?',
        'error': {
            'fr': "Désolé mais je n'ai pas compris quels médicaments vous preniez.",
            'en': "Sorry but I didn't understand your reply."
        },
        'quick_replies': {
            'fr': [
                single_reply('non'),
                single_reply('morphine'),
                single_reply('imodium'),
                single_reply('levothyrox'),
            ],
            'en': [
                single_reply('no'),
                single_reply('morphine'),
                single_reply('imodium'),
                single_reply('levothyrox'),
            ]
        }
    }

    WEIGHT = {
        'next': HAS_MEDICATION,
        'fun': personnal.ask_weight,
        'fr': 'Quel est votre poids ?',
        'en': 'How much do you weight ?',
        'error': {
            'fr': "Désolé mais je n'ai pas compris votre poids. Pouvez-vous me l'indiquer en kilogrammes ?",
            'en': "Sorry but I didn't get your weight. Can you tell me in kilograms ?"
        },
        'quick_replies': None
    }

    HEIGHT = {
        'next': WEIGHT,
        'fun': personnal.ask_height,
        'fr': 'Quelle taille faites-vous ?',
        'en': 'How tall are you ?',
        'error': {
            'fr': "Désolé mais je n'ai pas compris votre taille. Pouvez-vous me l'indiquer en centimètres ?",
            'en': "Sorry but I didn't get your height. Can you tell me in centimeters ?"
        },
        'quick_replies': None
    }

    PERSONNAL = {
        'next': HEIGHT,
        'fun': personnal.ask_consent,
        'fr': 'Souhaitez vous que je pose des questions personnelles pour écrire un compte-rendu plus précis ?',
        'en': 'Do you want me to ask you some personnal questions in order to write a more precise recap ?',
        'error': {
            'fr': "Désolé je n'ai pas compris. Vous pouvez me répondre par un simple 'oui' ou 'non'",
            'en': "Sorry I did not understand. You can answer by a simple 'yes' or 'no'"
        },
        'quick_replies': {
            'fr': [
                single_reply('oui'),
                single_reply('non')
            ],
            'en': [
                single_reply('yes'),
                single_reply('no'),
            ]
        }
    }

    FREQUENCY = {
        'next': PERSONNAL,
        'fun': pain.frequency,
        'fr': 'Avez-vous souvent mal à cet endroit ?',
        'en': 'Does this area hurt often ?',
        'error': {
            'fr': "Désolé mais je n'ai pas compris la fréquence de votre douleur.",
            'en': "Sorry but I didn't understand your reply."
        },
        'quick_replies': {
            'fr': [
                single_reply('oui'),
                single_reply('non')
            ],
            'en': [
                single_reply('yes'),
                single_reply('no'),
            ]
        }
    }

    DURATION = {
        'next': FREQUENCY,
        'fun': pain.duration,
        'fr': 'Depuis quand avez-vous mal ?',
        'en': 'How long have you been in pain ?',
        'error': {
            'fr': "Je n'ai pas compris depuis combien de temps vous avez mal. Pouvez-vous recommencer ?",
            'en': "Sorry but I didn't understand. Can you start again ?"
        },
        'quick_replies': {
            'fr': [
                single_reply('quelques jours'),
                single_reply('plus d\'une semaine'),
                single_reply('un mois')
            ],
            'en': [
                single_reply('few days'),
                single_reply('more than a week'),
                single_reply('a month')
            ]
        }
    }

    PAIN_LEVEL = {
        'next': DURATION,
        'fun': pain.level,
        'fr': 'Sur une échelle de 1 à 10, à combien évaluriez-vous votre douleur ?',
        'en': 'On a scale of 1 to 10, how would you rate your pain ?',
        'error': {
            'fr': "Désole mais je n'ai pas compris. Pouvez vous m'indiquer un chiffre ?",
            'en': "Sorry but I didn't understand. Can you give me a number ?"
        },
        'quick_replies': {
            'fr': [single_reply(f'{i}') for i in range(1, 11)],
            'en': [single_reply(f'{i}') for i in range(1, 11)]
        }
    }

    BODYPART = {
        'next': PAIN_LEVEL,
        'fun': bodypart.bodypart,
        'fr': 'Où avez-vous mal?',
        'en': 'Where are you hurt ?',
        'error': {
            'fr': "Désole mais je n'ai pas compris où vous aviez mal. Pourriez-vous m'indique plus précisément ?",
            'en': "Sorry but I didn't understand where you were hurt. Can you be more specific ?"
        },
        'quick_replies': {
            'fr': [single_reply(i) for i in BP_ARRAY_FR[:5]],
            'en': [single_reply(i) for i in BP_ARRAY_EN[:5]],
        }
    }

    START_CONVERSATION = {
        'next': BODYPART,
        'fun': start_conversation.detect_intent,
        'fr': 'Comment puis-je vous aider ?',
        'en': 'Hello and welcome on Kwili',
        'error': None,
        'quick_replies': {
            'fr': [
                single_reply('J\'ai mal'),
                single_reply('Bonjour'),
            ],
            'en': [
                single_reply('I am in pain'),
                single_reply('Hi'),
            ]
        }
    }
