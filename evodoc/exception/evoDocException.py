class EvoDocException(Exception):
    """
<<<<<<< HEAD
    This is parent exceptio to other exceptions in this project.
=======
    This exception is raised in entity module
>>>>>>> Master exception created issue #4
    """

    def __init__(self, errorCode, message, invalid=[]):
        self.errorCode = errorCode
        self.message = message
        self.invalid = invalid
