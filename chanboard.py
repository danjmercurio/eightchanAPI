import time
import requests
import json
import constant
from chanthread import *

class Board:

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

    def first_thread(self):
        if (len(self.threads) == 0):
            return self.get_threads()[0]
        else:
            return self.threads[0]
                
    def get_threads(self):
        threadsJson = json.loads(requests.get(constant.MAIN_URL + self.uri + '/threads.json').text)
        for page in threadsJson:
            currentPage = page[u'page']
            for thread_json in page[u'threads']:
                thread = Thread(thread_json[u'no'], currentPage, thread_json[u'last_modified'], self)
                self.threads.append(thread)
        return self.threads

    def get_thread(self, thread_id):
        for thread in self.get_threads():
            if thread.number == int(thread_id):
                return thread
        return False