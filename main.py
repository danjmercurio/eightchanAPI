import os
import sys
from .infinitechanapi import *
'''
    This is an example of how to use the API in your main function for your
    projects.
'''

if __name__ == "__main__":
    api = InifinitechanAPI()
    
    # Fetch all the boards
    #boards = api.get_boards();

    # Fetch a single board, the 'tech' board
    tech = api.get_board('/tech/')
    #print(tech)
    
    # Get the fist thread in the board.
    first_thread = tech.first_thread()
    #print(first_thread)

    # Get first post comment for the first thread in the board.
    comment = first_thread.firstPost().comment
    print(comment)

  