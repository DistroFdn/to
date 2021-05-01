#!/bin/python3

import json
import os
import sys
from json import load

class tcolor:
    PURPPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
            print(tcolor.NORMAL+lstto[i]+":")
            to_count_done = 0
            todo_count = 0
            to_count_list = len(fli['to'][lstto[i]])
            for j in fli['to'][lstto[i]]:
                if(j['done']=='False'):
                    todo_count += 1
                    if(j['priority'] == 1):
                        print(tcolor.GREEN+"\t"+str(todo_count)+"."+j['task'])
                    elif(j['priority'] == 2):
                        print(tcolor.YELLOW+"\t"+str(todo_count)+"."+j['task'])
                    elif(j['priority'] == 3):
                        print(tcolor.RED+"\t"+str(todo_count)+"."+j['task'])
                elif(j['done'] == 'True'):
                    to_count_done += 1
            if(to_count_done == to_count_list):
                print(tcolor.BLUE+'\t'+'all done')

def printDone():
    done_count = 0
    print("you done:")
    with open(".to", 'r') as fli:
        fli = load(fli)
        lstto = fli['to'].keys()
        for i in lstto:
            print(tcolor.NORMAL+"\n\t"+i+":")
            for j in (fli['to'][i]):
                if(j['done'] == 'True'):
                    print(tcolor.CYAN+"\t\t"+j['task'])
                    done_count += 1
    print(tcolor.BLUE+"\n"+str(done_count) + " task done")