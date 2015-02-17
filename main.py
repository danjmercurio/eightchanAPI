import os
import sys
from infinitechanapi import *
'''
    This is an example of how to use the API in your main function for your
    projects.
'''

if __name__ == "__main__":
    api = InifinitechanAPI()
    tech = api.get_board('/tech/')
    first_thread = tech.first_thread()
    comment = first_thread.first_post().comment
    print(comment)
