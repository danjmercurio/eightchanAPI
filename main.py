#main file for 8chan api

#8chan url: make this a variable because unfortunately it changes
MAINURL = 'http://8ch.net/'

#imports
import requests
import json
from board import Board

def getBoards():
	boards = []
	boardsJson = json.loads(requests.get(MAINURL + 'boards.json').text)
	for item in boardsJson:
		boards.append(Board(item[u'uri'],item[u'subtitle'],item[u'img'],item[u'sfw'],item[u'pph'],item[u'ppd'],item[u'time'],item[u'max'],item[u'ago'],item[u'uniq_ip'],item[u'tags'],item[u'title'],item[u'indexed']))
	return boards

def getBoard(uri):
	boards = getBoards()
	for board in boards:
		if (board.uri == uri):
			return board


	
