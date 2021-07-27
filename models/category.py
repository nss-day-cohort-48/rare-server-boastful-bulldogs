class Category():
    """Category Class"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every METHOD on a CLASS
    # needs as the first parameter.
    def __init__(self, id, label):
        self.id = id
        self.label = label