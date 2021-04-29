#!/bin/python3

import os
import sys


def menu():
    print("""
    help:
        
        add:
            a   add a new tag
            i   insert a task under a tag

        done:
            c   completion an entire tag
            d   done one task from a tag
        
        save and print:
            p   print all todo's
            s   save
            clear clear the screen
            
        quit and exit:
            w   write to disk and exit
            q  to quit
        """)


def clear():
    if(sys.platform == 'linux'):
        os.system('clear')
    elif(sys.sys.platform == 'windows'):
        os.system("cls")





command = str()
while(command != "q" or command != "quit"):
    command = input("command (m for menu): ")
    if(command == 'm'):
        menu()
    elif(command == 'a'):
        pass
    elif(command == 'i'):
        pass
    elif(command == 'c'):
        pass
    elif(command == 'd'):
        pass
    elif(command == 'p'):
        pass
    elif(command == 's'):
        pass
    elif(command == 'w'):
        pass
    elif(command == 'q'):
        quit()
    elif(command == 'clear'):
        clear()
