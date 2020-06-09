class History:
	conversation_date = ''
	logs = []

	def __init__(self):
		self.conversation_date = ''
		''' TODO: Add exact date '''

	class Log:
		def __init__(self, req, res):
			self.date = ''
			''' TODO: Add date '''
			self.req = req
			self.res = res

	def add_log(self, req, res):
		self.logs.push(Log(req, res))

	def remove_last_log(self):
		self.logs.pop()