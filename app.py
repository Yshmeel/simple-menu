import menu
import os
from menu.commands.CommandInfo import *
from menu.tests.SimpleTest import *

current_mode = ""
command_in_process = ""
commands = {}
tests = {}

def register_test(testInstance):
    tests[testInstance.key] = testInstance

def get_test(text):
    if text in tests:
        return tests[text]
    else:
        return False

def start_test(testInstance):
    testInstance.start()

def register_command(commandInstance):
    commands[commandInstance.call] = commandInstance

def execute_command(name):
    if name in commands:
        commands[name].callback()
    else:
        print("Wrong command")
        input_loop()

def change_mode(mode):
    global current_mode
    current_mode = mode

def progress(text):
    global current_mode
    if text == "commands":
        output_commands()
    elif text == "return":
        change_mode("commands")
        output_commands()
    elif text == "exit":
        if input("Are you sure?(y, n)") == "y":
            os._exit(1)
    elif text == "tests":
        change_mode("tests")
        output_tests()
    elif current_mode == "commands":
        execute_command(text)
    elif current_mode == "tests":
        test = get_test(text)
        if test != False:
            start_test(test)
        else:
            print("Wrong test!")

    input_loop()

def input_loop():
    global current_mode
    input_label = ""
    if current_mode == "commands":
        input_label = "\n> Input your command: "
    elif current_mode == "tests":
        input_label = "\n> Select test: "

    text = input(input_label)
    progress(text)

def output_tests():
    iter = 0
    for test in tests:
        object = tests[test]
        print(object.key + ": " + object.name + "\n"
            + object.description + (iter + 1 == len(tests) and "" or "\n"))
        iter += 1

def output_commands():
    iter = 0
    for command in commands:
        object = commands[command]
        print(object.call + ": " + object.title + "\n"
            + object.description + (iter + 1 == len(commands) and "" or "\n"))
        iter += 1
def launch():
    global current_mode
    current_mode = "commands"
    print("Hello, that's my first python program.\n"
        + "This program can output info about me, and works with commands\n"
        + "\nHey, look at my commands:\n")

    output_commands()
    input_loop()


register_command(CommandInfo())
register_test(SimpleTest())
launch()