class book(object):
	"""docstring ids, name, author, edition Book"""
	def __init__(self, ids, name, author, edition):
		self.ids = ids
		self.name = name
		self.author = author
		self.edition = edition
	def getName(self):
		return self.name
	def getAuthor(self):
		return self.author
	def getEdition(self):
		return self.edition
	def getIds(self):
		return self.ids
	def showAuthorName(self):
		print(self.author)
	def _str_(self):
		return self.name + "," + self.ids + "," +  self.author + "," +self.edition
		