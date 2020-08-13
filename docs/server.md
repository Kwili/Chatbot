# Serveur

La mise en place du serveur est effectuée dans le fichier `server.py`.

```python
PORT = 8080 if 'PORT' not in os.environ else os.environ['PORT']
```

Le port sur lequel est déployé est, par défaut, le port 8080. S'il est défini dans l'environnement, il sera récupéré, et peut donc être changé.

L'application est ensuite crée en utilisant les frameworks Flask et SocketIO.

```python
@app.route("/")
def index():
    return app.send_static_file('index.html')
```

Une route index est définie, permettant d'avoir un affichage graphique du chatbot.

```python
@socketio.on('message')
def handle_message(message):
	user = find_user(request.sid)
    response = handle_input(user, message)
    emit('message', response)
```

La route `message` permet de gérer l'arrivée d'un message de l'utilisateur (la réponse à une question). Elle récupère donc l'utilisateur, analyse son message, et émet une réponse à l'utilisateur.

```python
@socketio.on('connect')
def handle_connect():
    add_user(request.sid)
    user = find_user(request.sid)
    response = start_conversation(user)
    emit('message', response)
```

La route `connect` permet de gérer la première connection de l'utilisateur, en créant une nouvelle instance de la classe `User`, et en émettant un message de bienvenue.

La route `disconnect` détruit un utilisateur et son historique associés.

Les informations concernant la gestion des utilisateurs peuvent être trouvées [ici](user.md).

Les informations sur les questions peuvent être trouvées [ici](questions.md).
