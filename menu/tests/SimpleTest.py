from menu.Test import *

class SimpleTest(Test):
    def __init__(self):
        self.key = "simple"
        self.name = "Simple"
        self.description = "Test yourself"
        self.add_question("What programmers writes first?", [
            "Hello world",
            "hello, python",
            "print",
            "red"
        ], 0)