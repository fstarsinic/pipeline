import inspect
import logging


class Stage:
    """ This is the base class for a pipeline Stage"""

    STATE_ERROR = "Error"
    STATE_SUCCESS = "Success"
    STATE_FAILURE = "Failure"
    STATE_IN_PROGRESS = "In Progress"

    def __init__(*args, **kwargs):
        """ constructor """
        logging.info('__init__()')
        
    def initalize(self, *args, **kwargs):
        """ initialize method """
        
    def execute(self, *args, **kwargs):
        """ execute method """
        
    def finalize(self, *args, **kwargs):
        """ finalize method """
        
    def update_state(self):
        """ updates the state for the given stage"""

def main():
    """ test method """
    print('Hello')

if __name__ == '__main__':
    main()
