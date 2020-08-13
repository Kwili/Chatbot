# Questions

La liste des questions est définie dans le fichier `questions.py`.

Ce fichier définie la classe `Questions` contenant la liste des questions posées à l'utilisateur.

Chaque question comprend 4 élements:

-   `fun`: la fonction d'analyse qui est associée à la question
-   `next`: la question suivante
-   `fr`: la question (en français)
-   `en`: la question (en anglais)

Exemple:

```python
START_CONVERSATION = {
        'next': BODYPART,
        'fun': start_conversation.detect_intent,
        'fr': 'Bonjour et bienvenue sur Kwili, comment puis-je vous aider ?',
        'en': 'Hi! Welcome on Kwili! How can I help you ?'
    }
```

Ces questions sont utilisées dans le fichier `input_handler.py`.

Ce fichier définie notamment la méthode

```python
def handle_input(user: object, req: str):
    question = user.question
    ret = question['fun'](req.lower())
    if ret is not True:
        return 'Désolé mais je nai pas compris'
    user.question = question['next']
    return user.question['fr']
```

Cette méthode récupère toute d'abord la dernière question posée à l'utilisateur, et fait appelle à la méthode `fun` de celle-ci, permettant de faire l'analyse de la réponse.
Ensuite, si la réponse n'a pas été comprise, un message d'erreur est retourné. Sinon, la propriété `next` est utilisée pour trouver directement la prochaine question à poser, et la version française de la question est envoyée (le chatbot n'est disponible qu'en français pour l'instant).

Plus d'informations sur les fonctions d'analyses sont disponibles [ici](intents.md).
