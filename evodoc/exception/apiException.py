class ApiException(Exception):
    """
    This exception is raised in api module
    """
    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode=errorCode
        self.message=message
        self.invalid=invalid