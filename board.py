class Board():
	def __init__(self,uri,subtitle,img,sfw,pph,ppd,time,maxposts,ago,uniq_ip,tags,title,indexed):
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
		self.max = int(maxposts)
		self.ago = ago
		self.uniq_ip = uniq_ip
		self.tags = tags

	def __repr__(self):
		return 'Board Object of '.join(self.uri)

	def isSFW(self):
		return self.sfw

	def isIndexed(self):
		return self.indexed

	def getThreads(self):
		return True

#, u'uniq_ip': u'3118', u'tags': [u'politics', u'news', u'activism']}
