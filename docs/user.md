# Gestion des utilisateurs

La gestion des utilisateur est réalisée dans le fichier users.py

Celui défini la Classe `User`, qui définie un utilisateur, ainsi que les méthodes `add_user` et `find_user` permettant respectivement d'ajouter et chercher un utilateur.

```python
class User:
	def __init__(self, sid):
		self.sid = sid
		self.question = Questions.START_CONVERSATION
		self.history = History()

	def update_history(self, history):
		self.history = history
```

Un utilisateur contient:

-   Un SID (id du socket depuis lequel il est connecté)
-   La dernière question qui lui a été posée
-   L'historique de ses questions et réponses
-   Une méthode `update_history` permettant de mettre à jour son historique.

Un utilisateur est automatiquement détruit lors de la déconnection de l'utilisateur, ou lorsque de la discussion est terminée.

Les informations sur l'historique de l'utilisateur peuvent être trouvées [ici](history.md).
