class GridItem():
    def __init__(self, id):
        self.id = id
        self.name = None
        self.image_file_name = None
        self.examples = []
        self.description = None

class ExampleItem():
    def __init__(self):
        #super().__init__()
        self.name = None
        #self.file_name = file_name
        self.example = None
