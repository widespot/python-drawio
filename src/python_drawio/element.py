class Element:

    def __init__(self):
        self.id = None

    def set_id(self, id: str):
        if self.id is not None:
            raise Exception("Id already set")
        self.id = str(id)
