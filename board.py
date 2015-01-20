import requests
import main
import thread
import json
# a python class that represents a board on 8chan


class Board():

    def __init__(self, uri, title, subtitle, time, indexed, sfw, pph, ppd, max, uniq_ip, tags, img, ago):
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
        self.threads = []

    def __repr__(self):
        return "<8chan /" + self.uri + "/ board " + str(object.__repr__(self))[1:]

    def isSFW(self):
        return self.sfw

    def isIndexed(self):
        return self.indexed

    def firstThread(self):
        if (len(self.threads) == 0):
            return self.getThreads()[0]
        else:
            return self.threads[0]

    def getThreads(self):
        threadsJson = json.loads(requests.get(main.MAINURL + self.uri + '/threads.json').text)
        for page in threadsJson:
            currentPage = page[u'page']
            for threadNum in page[u'threads']:
                self.threads.append(thread.Thread(threadNum[u'no'], currentPage, threadNum[u'last_modified'], self))
        return self.threads

    def getThread(self, threadid):
        for thread in self.getThreads():
            if thread.number == int(threadid):
                return thread
        return False

