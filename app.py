import menu
from menu.commands.CommandInfo import *

class MenuBot:
    currentMode = "commands"
    commands = {}
    def registerCommand(self, commandInstance):
        print("Command " + commandInstance.call + " is registered")
        self.commands[commandInstance.call] = commandInstance
    def executeCommand(self, name):
        if name in self.commands == False:
            print("Wrong command.")
        else:
            self.commands[name].callback()
    def progress(self, text):
        if text == "commands":
            self.outputCommands()
        elif self.currentMode == "commands":
            self.executeCommand(text)

        menu.inputLoop()
    def inputLoop(self):
        text = input("\n> Input your command: ")
        self.progress(text)
    def outputCommands(self):
        iter = 0
        for command in self.commands:
            object = self.commands[command]
            print(object.call + ": " + object.title + "\n"
                + object.description + (iter + 1 == len(self.commands) and "" or "\n"))
            iter += 1
    def launch(self):
        print("Menu started...")
        self.currentMode = "commands"

        print("Hello, that's my first python program.\n"
            + "This program can output info about me, and works with commands\n"
            + "\nHey, look at my commands:\n")

        self.outputCommands()
        self.inputLoop()
        
menu = MenuBot()
menu.registerCommand(CommandInfo())
menu.launch()