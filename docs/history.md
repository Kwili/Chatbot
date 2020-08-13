# Historique

La gestion de l'historique est effectuée dans le fichier `history.md`.

Son utilisation permet d'accéder à l'historique de la conversation, et d'effectuer des retours en arrière dans la discussion.
Ce fichier défini la classe `History`, contenant la date de discussion, et une liste de logs.:

```python
class History:
	conversation_date = ''
	logs = []

	def __init__(self):
		self.conversation_date = ''

	class Log:
		def __init__(self, req, res):
			self.date = ''
			self.req = req
			self.res = res

	def push(self, req, res):
		self.logs.push(Log(req, res))

	def pop_last(self):
		self.logs.pop()
```

La classe `Log` est une structure contenant la date, ainsi que la requête et la réponse envoyée (la requête étant la question posée, et la réponse étant la réponse de l'utilisateur) à une question.

Un historique appartient à un utilisateur, et est détruit lors de la déconnection d'un utilisateur.
