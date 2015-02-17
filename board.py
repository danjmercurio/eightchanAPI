import time
import requests
import json
import constant
from boardthread import *

class Board:

    def __init__(self, board_json):
        self.uri = board_json[u'uri']
        self.title = board_json[u'title']
        self.subtitle = board_json[u'subtitle']
        self.time = board_json[u'time']
        if (board_json[u'indexed'] == u'0'):
            self.indexed = False
        if (board_json[u'indexed'] == u'1'):
            self.indexed = True
        if (board_json[u'sfw'] == u'0'):
            self.sfw = False
        if (board_json[u'sfw'] == u'1'):
            self.sfw = True
        self.pph = board_json[u'pph']
        self.ppd = board_json[u'ppd']
        self.max = board_json[u'max']
        self.uniq_ip = board_json[u'uniq_ip']
        self.tags = board_json[u'tags']
        self.img = board_json[u'img']
        self.ago = board_json[u'ago']
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
                thread = BoardThread(thread_json[u'no'], currentPage, thread_json[u'last_modified'], self)
                self.threads.append(thread)
        return self.threads

    def get_thread(self, thread_id):
        for thread in self.get_threads():
            if thread.number == int(thread_id):
                return thread
        return False