class DbException(Exception):
    """
    This exception is raised in entity module
    """
    def __init__(self, errorCode, message):
        self.errorCode=errorCode
        self.message=message