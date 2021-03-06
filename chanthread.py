import time
import requests
import json
import constant
from chanpost import *
from chanboard import *


class Thread:
    def __init__(self, number, page, last_modified, board):
        self.number = int(number)
        self.page = int(page)
        self.board = board
        self.last_modified = int(last_modified)
        self.posts = []

    def is_front_page(self):
        return self.page == 0

    def seconds_since_last_modified(self):
        return int(time.time()) - self.last_modified

    def get_posts(self):
        url = constant.MAIN_URL + self.board.uri
        url += u'/res/' + str(self.number) + u'.json'
        url = requests.get(url).text
        postsJson = json.loads(url)
        for p in postsJson[u'posts']:
            try:
                name = p[u'name']
            except KeyError:
                name = None
            number = p[u'no']
            try:
                capcode = p[u'capcode']
            except KeyError:
                capcode = None
            try:
                com = p[u'com']
            except KeyError:
                com = None
            posttime = p[u'time']
            try:
                fsize = p[u'fsize']
            except KeyError:
                fsize = None
            try:
                filename = p[u'filename']
            except KeyError:
                filename = None
            try:
                ext = p[u'ext']
            except KeyError:
                ext = None
            locked = p[u'locked']
            sticky = p[u'sticky']
            try:
                extra_files = p['extra_files']
            except KeyError:
                extra_files = None
            try:
                sub = p[u'sub']
            except KeyError:
                sub = None
            try:
                tim = p[u'tim']
            except KeyError:
                tim = None

            post = Post(name=name,
                        number=number,
                        sub=sub,
                        capcode=capcode,
                        com=com,
                        posttime=posttime,
                        fsize=fsize,
                        filename=filename,
                        ext=ext,
                        locked=locked,
                        sticky=sticky,
                        extra_files=extra_files,
                        tim=tim,
                        board=self.board,
                        page=self.page)
            self.posts.append(post)
        return self.posts

    def number_of_posts(self):
        return len(self.posts)

    def first_post(self):
        if (len(self.posts) == 0):
            return self.get_posts()[0]
        else:
            return self.posts[0]

    def get_all_file_urls(self):
        urls = list()
        if len(self.posts) == 0:
            self.getPosts()

        for post in self.get_posts():
            urls.append(post.get_file_urls())
        return urls
