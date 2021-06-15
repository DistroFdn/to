#!/bin/python3

import core
import initer
import argparse

# this method run every time that the program run, this method will check that
# you have configed your username and emial or not. if yes you can continue to use
#if no, method will do this for you.
if(not initer.IsInited()):
    print(core.TColor.YELLOW + 'you shoud first config your username and email')
    username = input(core.TColor.CYAN + 'usesr name: ')
    email = input(core.TColor.CYAN + 'email: ')
    initer.UserConf(username, email)

# this is the intractive command-line interface.
command = str()
while(command != "q" or command != "quit"):
    try:
        command = input(core.TColor.NORMAL+"command (m for menu): ")
        if(command == 'm'):
            core.Menu()
        elif(command == 'a'):
            core.AddTo()
        elif(command == 'i'):
            core.InsertTask()
        elif(command == 'e'):
            core.Edit()
        elif(command == 'c'):
            core.CompletTo()
        elif(command == 'd'):
            core.DoneTask()
        elif(command == 'u'):
            core.UnDoneTask()
        elif(command == 'p'):
            core.PrintTask()
        elif(command == 's'):
            core.PrintDone()
        elif(command == 'clear'):
            core.Clear()
        elif(command == 'q'):
            quit()
        elif(command == 'prog'):
            core.Progress()
        elif(command == 'log'):
            core.log()
        else:
            print(core.TColor.RED+'command is incorrect')
    except KeyboardInterrupt:
        print(core.TColor.RED+'Quit')
