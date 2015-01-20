import main
import time
import requests
# represents an 8chan post


class Post():


    def __init__(self, name, number, sub, capcode, com, posttime, fsize, filename, ext, locked, sticky, extra_files, board, page):
        self.sub = sub
        self.name = name
        self.number = int(number)
        self.capcode = capcode
        self.comment = com

        self.posttime = int(posttime)
        if (fsize is not None):
            self.fsize = int(fsize)
        else:
            self.fsize = fsize
        self.filename = filename
        self.ext = ext
        self.board = board
        self.page = page
        if (locked == u'1'):
            self.locked = True
        if (locked == u'0'):
            self.locked = False
        if (sticky == u'1'):
            self.sticky = True
        if (sticky == u'0'):
            self.sticky = False
        self.extra_files = extra_files

    def getFileURLs(self):
        # https://media.8ch.net/pol/src/1418546321250.jpg
        return main.SCHEMA + 'media.' + main.DOMAIN + '/' + self.board.uri + '/src/' + self.filename + self.ext

    def getFiles(self):
        files = []
        for file in self.getFileURLs():
            files.append(requests.get(file))
        return files

    def isLocked(self):
        return self.locked

    def isAnon(self):
        return self.name == u'Anonymous'

    def getBoard(self):
        return self.board

    def getPage(self):
        return self.page

    def secondsSinceLastModified(self):
        return int(time.time()) - self.last_modified

    def isSticky(self):
        return self.sticky

    def hasFile(self):
        return self.filename is not None

    def hasMultipleFiles(self):
        return self.extra_files is not None

    def getPostAge(self):
        return int(time.time()) - self.posttime