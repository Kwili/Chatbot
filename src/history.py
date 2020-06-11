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

	def push(self, req, res):
		self.logs.push(Log(req, res))

	def pop_last(self):
		self.logs.pop()