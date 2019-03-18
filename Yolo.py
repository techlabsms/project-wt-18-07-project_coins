from os import popen
class Yolo:

    yoloCommand = ""

    # setup Yolo interface
    def __init__(self, command):
        print("Yolo initialized\n")
        self.yoloCommand = command

    # run yolo interface on command that was specified in setup and returp all discoverd numbers
    def start(self):
        answer =  popen(self.yoloCommand).read()
        numbers = answer.split("\n")
        numbers.remove(numbers[0])
        print (numbers)
        return numbers



