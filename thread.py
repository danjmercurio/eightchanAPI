import time
import main
import requests
import json
import post
# represents an 8chan thread


class Thread():

	# thread.Thread(threadNum[u'no'], currentPage, self.uri)
    def __init__(self, number, page, last_modified, board):
        self.number = int(number)
        self.page = int(page)
        self.board = board
        self.last_modified = int(last_modified)
        self.posts = []

    def isFrontPage(self):
        return self.page == 0

    def secondsSinceLastModified(self):
        return int(time.time()) - self.last_modified

    def getPosts(self):
        postsJson = json.loads(requests.get(main.MAINURL + self.board.uri + u'/res/' + str(self.number) + u'.json').text)
        for p in postsJson[u'posts']:
            name = p[u'name']
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

            self.posts.append(post.Post(name=name,
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
                                        board=self.board,
                                        page=self.page))
        return self.posts

    def numberOfPosts(self):
        return len(self.posts)

    def firstPost(self):
        if (len(self.posts) == 0):
            return self.getPosts()[0]
        else:
            return self.posts[0]
