class Comment():
    """Comment Class"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every METHOD on a CLASS
    # needs as the first parameter.
    def __init__(self, id, post_id, author_id, content="", created_on=""):
        self.id = id
        self.post_id = post_id
        self.author_id = author_id
        self.content = content
        self.created_on = created_on