class ApiException(Exception):
    """
    This exception is raised in api module
    """
    def __init__(self, errorCode, message, missing=[]):
        self.errorCode=errorCode
        self.message="{\n\t\"message\": " + "\"" + message + "\",\n\t\"invalid\": [\n"
        for i in missing:
            self.message+="\t\t\"" + i + "\",\n"
        self.message+="\t]\n}"