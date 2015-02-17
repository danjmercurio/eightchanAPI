import json
import requests
import constant
from board import *

class InifinitechanAPI:
    
    def __init__(self):
        pass
    
    def get_boards(self):
        boards = []
        boards_json = json.loads(requests.get(constant.MAIN_URL + 'boards.json').text)
        for board_json in boards_json:
            new_board = Board(board_json)
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
        boardsNum = 0
        boardsJson = json.loads(requests.get(constant.MAIN_URL + 'boards.json').text)
        for item in boardsJson:
            boardsNum += 1
        return boardsNum

