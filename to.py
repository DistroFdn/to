#!/bin/python3

import core

command = str()

while(command != "q" or command != "quit"):
    command = input("command (m for menu): ")
    if(command == 'm'):
        core.menu()
    elif(command == 'a'):
        pass
    elif(command == 'i'):
        pass
    elif(command == 'e'):
        pass
    elif(command == 'c'):
        pass
    elif(command == 'd'):
        pass
    elif(command == 'p'):
        core.printTask()
    elif(command == 's'):
        core.printDone()
    elif(command == 'clear'):
        core.clear()
    elif(command == 'q'):
        quit()
    else:
        pass