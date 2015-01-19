#a python class that represents a board on 8chan
class Board():
	def __init__(self,uri,title,subtitle,time,indexed,sfw,pph,ppd,max,uniq_ip,tags,img,ago):
		self.uri = uri
		self.subtitle = subtitle
		self.img = img
		self.title = title
		if (sfw == u'0'):
			self.sfw = False
		if (sfw == u'1'):
			self.sfw = True
		self.pph = int(pph)
		self.ppd = int(ppd)
		self.time = time
		if (indexed == u'0'):
			self.indexed = False
		if (indexed == u'1'):
			self.indexed = True
		self.max = max
		self.ago = ago
		self.uniq_ip = uniq_ip
		self.tags = tags

	def __repr__(self):
		return "<8chan /" + self.uri + "/ board " + str(object.__repr__(self))[1:]

	def isSFW(self):
		return self.sfw

	def isIndexed(self):
		return self.indexed

	def getThreads(self):
		return True
