class ApiException(Exception):
    """
    This exception is raised in api module
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
