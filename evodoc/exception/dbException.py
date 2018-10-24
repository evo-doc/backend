class DbException(Exception):
    """
    This exception is raised in entity module
    """

    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode = errorCode
        self.message = message
        self.invalid = invalid
