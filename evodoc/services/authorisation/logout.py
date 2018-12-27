def logout(g):
    """
    User logout
        :param g: context
    """
    g.token.deleteWithPrevious()
