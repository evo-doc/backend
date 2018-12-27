class Context(object):
    """
    Context class
    """
    pass


class CreateContext(object):
    """
    Context creator (function wrapper)
    """

    def __call__(self, f):
        def wrapper(*args, **kwargs):
            g = Context()
            return f(g, *args, **kwargs)
        wrapper.__name__ = f.__name__
        return wrapper
