#!/bin/python3

import core
import initer
import argparse
import sys

# this method run every time that the program run, this method will check that
# you have configed your username and emial or not. if yes you can continue to use
#if no, method will do this for you.
if(not initer.IsInited()):
    print(core.TColor.YELLOW + 'you shoud first config your username and email')
    username = input(core.TColor.CYAN + 'usesrname: ')
    email = input(core.TColor.CYAN + 'email: ')
    initer.UserConf(username, email)

# this is the intractive command-line interface.
def intractive():
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

# this is the non-intractive command-line interface
if(len(sys.argv) > 1):
    cli = sys.argv[1]
    if(cli == 'add'):
        core.AddTo()
    elif(cli == 'help' or cli == 'menu' or cli == '--help'):
        core.Menu()
    elif(cli == 'insert'):
        core.InsertTask()
    elif(cli == 'edit'):
        core.Edit()
    elif(cli == 'fill' or cli == 'complete'):
        core.Done(core.CompletTo)
    elif(cli == 'done'):
        core.Done(core.DoneTask)
    elif(cli == 'undone'):
        core.UnDoneTask()
    elif(cli == 'print' or cli == 'list'):
        core.PrintTask()
    elif(cli == 'show'):
        core.PrintDone()
    elif(cli == 'prog' or cli == 'progress'):
        core.Progress()
    elif(cli == 'log'):
        core.log()
    elif(cli == 'commit'):
        pass
    else:
        print(core.TColor.RED+'option is invalid')
elif(len(sys.argv) == 1):
    intractive()
