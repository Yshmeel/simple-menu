from menu.Command import * 

class CommandInfo (Command):
    def __init__(self):
        self.call = "info"
        self.title = "Information"
        self.description = "Hello. I will introduce myself."
    def callback(self):
        print(self.description)