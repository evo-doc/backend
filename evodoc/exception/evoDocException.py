class EvoDocException(Exception):
    """
    This is parent exceptio to other exceptions in this project.
    """

    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode = errorCode
        self.message = message
        self.invalid = invalid
