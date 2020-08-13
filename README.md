# Chatbot Kwili

Ceci est la documentation du chatbot de Kwili.

Il a été construit en `Python`, en utilisant le framework `Flask` et `SocketIO`.

Il est déployé sur Heroku via le `Procfile` à l'url [suivant](https://kwili-bot.herokuapp.com/ui).

## Développement

Pour commencer le développement, créez un nouvel environnement virtuel et utilisez pip pour installer les packets listés dans requirements.txt

```sh
pip install -r requirements.txt
```

Lancez ensuite le serveur en utilisant

```sh
python wsgy.py
```

## Déploiement

Le déploiement est effectué automatiquement par Heroku lors d'un merge sur la branche `production`.

Des informations supplémentaires sur la mise en place du serveur sont disponibles [ici](docs/server.md)

## Documentation technique

Le chatbot contient ces différentes catégories:

-   [Gestion de l'utilisateur](docs/user.md)
-   [Questions à poser](docs/questions.md)
-   [Gestion des réponses utilisateur](docs/intents.md)

Le chatbot fonctionne de cette manière:

-   Un utilisateur se connecte
-   Un message d'introduction est envoyé
-   L'utilisateur envoie un message
-   Le message est analysé par le chatbot
-   La réponse est envoyée à l'utilisateur
