class DbException(Exception):
    """
    This exception is raised in entity module
    """
<<<<<<< HEAD

    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode = errorCode
        self.message = message
        self.invalid = invalid
=======
    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode=errorCode
        self.message=message
        self.invalid=invalid
>>>>>>> authentication working
