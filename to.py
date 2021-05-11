#!/bin/python3

import core
import sys

command = str()

while(command != "q" or command != "quit"):
    command = input(core.TColor.NORMAL+"command (m for menu): ")
    if(command == 'm'):
        core.Menu()
    elif(command == 'a'):
        core.AddTo()
    elif(command == 'i'):
        core.InsertTask()
    elif(command == 'e'):
        pass
    elif(command == 'c'):
        core.CompletTo()
    elif(command == 'd'):
        core.DoneTask()
    elif(command == 'p'):
        core.PrintTask()
    elif(command == 's'):
        core.PrintDone()
    elif(command == 'clear'):
        core.Clear()
    elif(command == 'q'):
        quit()
    else:
        pass