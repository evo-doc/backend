from evodoc.exception.evoDocException import EvoDocException


class ApiException(EvoDocException):
    """
    This exception is raised in api module
    """

    # def __init__(self, errorCode, message, invalid=[]):
    #     self.errorCode = errorCode
    #     self.message = message
    #     self.invalid = invalid
