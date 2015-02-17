import json
import requests
import constant
from chanboard import *


class InifinitechanAPI:
    def get_boards(self):
        boards = []
        url = requests.get(constant.MAIN_URL + 'boards.json').text
        boards_json = json.loads(url)
        for board_json in boards_json:
            new_board = Board(board_json[u'uri'],
                              board_json[u'title'],
                              board_json[u'subtitle'],
                              board_json[u'time'],
                              board_json[u'indexed'],
                              board_json[u'sfw'],
                              board_json[u'pph'],
                              board_json[u'ppd'],
                              board_json[u'max'],
                              board_json[u'uniq_ip'],
                              board_json[u'tags'],
                              board_json[u'img'],
                              board_json[u'ago'])
            boards.append(new_board)
        return boards

    def get_board(self, uri):
        uri = uri.strip('/')
        boards = self.get_boards()
        for board in boards:
            if (uri == board.uri):
                return board
        return False

    def get_boards_count(self):
        boards_count = 0
        url = requests.get(constant.MAIN_URL + 'boards.json').text
        boards_json = json.loads(url)
        for board_json in boards_json:
            boards_count += 1
        return boards_count
