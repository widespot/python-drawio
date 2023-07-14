class Content:

    def __init__(self):
        self.id = None

    def set_id(self, id):
        if self.id is not None:
            raise Exception("Id already set")
        self.id = id
