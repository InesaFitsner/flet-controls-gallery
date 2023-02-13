class GridItem():
    def __init__(self, id):
        self.id = id
        self.name = None
        self.image_file_name = None
        self.examples = []
        self.description = None

class ExampleItem():
    def __init__(self):
        self.name = None
        self.example = None
