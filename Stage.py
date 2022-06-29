""" Is this the right spot for module docstring?"""
import logging
import sys

class Stage:
    """ This is the base class for a pipeline Stage"""

    STATE_ERROR = "Error"
    STATE_SUCCESS = "Success"
    STATE_FAILURE = "Failure"
    STATE_IN_PROGRESS = "In Progress"

    def __init__(*args, **kwargs):
        """ constructor """
        logging.info(f'__init__({args}, {kwargs}')
        first = args[0]
        print(f'{result}')

    def initalize(self, *args, **kwargs):
        """ initialize method """


    def execute(self, *args, **kwargs):
        """ execute method """

    def finalize(self, *args, **kwargs):
        """ finalize method """

    def update_state(self):
        """ updates the state for the given stage"""

def main(stuff):
    """ test method """
    print('Hello')
    i = int(stuff)
    s = Stage(i)

if __name__ == '__main__':
    main(4)
