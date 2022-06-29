import inspect
import logging


class Stage:

    STATE_ERROR = "Error"
    STATE_SUCCESS = "Success"
    STATE_FAILURE = "Failure"
    STATE_IN_PROGRESS = "In Progress"

    def __init__(*args, **kwargs):
        pass

    def initalize(self, *args, **kwargs):
        pass

    def execute(self, *args, **kwargs):
        pass

    def finalize(self, *args, **kwargs):
        pass

    def update_state(self):
        pass

def main():
    print('Hello')

if __name__ == '__main__':
    main()
