class DbException(Exception):
    """
    This exception is raised in entity module
    """
<<<<<<< HEAD
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
=======
    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode=errorCode
        self.message=message
        self.invalid=invalid
>>>>>>> 3a87d36124975b2e832402d1629f26741887965d
