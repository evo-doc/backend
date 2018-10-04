from flask import Flask

def create_app():
    """
    Application factory, just something that creates your new favorite API
    """

    app = Flask(__name__)

    return app