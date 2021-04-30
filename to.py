#!/bin/python3

import os
import sys
from json import load

def menu():
    print("""
    help:
        
        add:
            a   add a new to
            i   insert a task under a to
            e   edit a task or to

        done:
            c   completion an entire to
            d   done one task from a to
        
        print:
            p   print all todo's
            s  show task's wich you done
            clear clear the screen
            
        quit and exit:
            q  exit
        """)


def clear():
    if(sys.platform == 'linux'):
        os.system('clear')
    elif(sys.sys.platform == 'windows'):
        os.system("cls")


def printTask():
    with open('.to', 'r') as fli:
        fli = load(fli)
        lstto = list(fli['to'].keys())
        for i in range(len(lstto)):
            print(lstto[i]+":")
            to_count_done = 0
            to_count_list = len(fli['to'][lstto[i]])
            for j in fli['to'][lstto[i]]:
                if(j['done']=='False'):
                    print("\t"+j['task'])
                elif(j['done'] == 'True'):
                    to_count_done += 1
            if(to_count_done == to_count_list):
                print('\t'+'all done')



try:
    command = str()
    while(command != "q" or command != "quit"):
        command = input("command (m for menu): ")
        if(command == 'm'):
            menu()
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
            printTask()
        elif(command == 'pd'):
            pass
        elif(command == 's'):
            pass
        elif(command == 'clear'):
            clear()
        elif(command == 'w'):
            pass
        elif(command == 'q'):
            quit()
except:
    pass
