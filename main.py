# main file for 8chan api

# imports
import json

import requests

from board import Board


# 8chan url: make this a variable because unfortunately it changes
MAINURL = 'http://8ch.net/'

# force all connections to be made securely
def forceSSL():
    global MAINURL
    MAINURL = 'https://8ch.net'


# returns a list of Boards
def getBoards():
    boards = []
    boardsJson = json.loads(requests.get(MAINURL + 'boards.json').text)
    for item in boardsJson:
        boards.append(
            Board(item[u'uri'], item[u'title'], item[u'subtitle'], item[u'time'], item[u'indexed'], item[u'sfw'],
                  item[u'pph'], item[u'ppd'], item[u'max'], item[u'uniq_ip'], item[u'tags'], item[u'img'],
                  item[u'ago']))
    return boards


# returns a Board object if board exists, or False otherwise.
# don't include slashes in uri argument. for example: 'b', NOT '/b/'
def getBoard(uri):
    boards = getBoards()
    for board in boards:
        if (board.uri == uri):
            return board
    return False


# returns an integer value of the total number of boards on 8chan
def getNumBoards():
    boardsNum = 0
    boardsJson = json.loads(requests.get(MAINURL + 'boards.json').text)
    for item in boardsJson:
        boardsNum += 1
    return boardsNum



