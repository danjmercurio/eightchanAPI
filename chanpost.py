import time
import requests
import constant
# represents an 8chan post

class Post():
    
    def __init__(self, name, number, sub, capcode, com, posttime, fsize, filename, ext, locked, sticky, extra_files, tim, board, page):
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
        self.tim = tim
    
    def get_file_urls(self):
        if self.hasFile():
            urls = list()
            urls.append(constant.SCHEMA + 'media.' + constant.DOMAIN + self.board.uri + '/src/' + self.tim + self.ext)
            if self.extra_files is not None:
                for i in self.extra_files:
                    urls.append(constant.SCHEMA + 'media.' + constant.DOMAIN + self.board.uri + '/src/' + i[u'tim'] + i[u'ext'])
            return urls
        else:
            return False

def is_locked(self):
    return self.locked
    
    def is_anon(self):
        return self.name == u'Anonymous'
    
    def get_board(self):
        return self.board
    
    def get_page(self):
        return self.page
    
    def seconds_since_last_modified(self):
        return int(time.time()) - self.last_modified
    
    def is_sticky(self):
        return self.sticky
    
    def has_file(self):
        return self.filename is not None
    
    def has_multiple_files(self):
        return self.extra_files is not None
    
    def get_post_age(self):
        return int(time.time()) - self.posttime
    
    def check_dubs(self):
        return str(self.number)[-2:-1] == str(self.number)[-1:]
    
    def check_trips(self):
        return str(self.number)[-3:-2] == str(self.number)[-2:-1] == str(self.number)[-1:]
