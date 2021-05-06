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

def Menu():
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

def Clear():
    if(sys.platform == 'linux'):
        os.system('clear')

def PrintTask():
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

def PrintDone():
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

def DoneTask():
    with open('.to', 'r') as fli:
        to_count = 1
        fli = json.load(fli)
        for i in fli['to'].keys():
            print(tcolor.CYAN+str(to_count)+". "+i)
            to_count += 1
        which_to = int(input(tcolor.NORMAL+'select a to[0 to quit]: '))
        if(which_to != 0):
            task_count = 0
            tag = list(fli['to'].keys())[which_to-1]
            if(len(fli['to'][tag]) != 0):
                for i in fli['to'][tag]:
                    if(i['done'] == "False"):
                        print(tcolor.YELLOW+str(task_count+1)+". "+i['task'])
                        task_count += 1
                if(task_count != 0):
                    task_num = int(input(tcolor.NORMAL+'which task[0 to quit]: '))
                    # tmp_fli = list(fli['to'][tag])[task_num-1]
                    fli['to'][tag][task_num-1]['done'] = 'True'
                    with open('.to', 'w') as fliw:
                        fliw.write(json.dumps(fli,indent=4))
                else:
                    print(tcolor.BLUE+"you did all the task's")
            else:
                print(tcolor.RED+'there is no task in this to')














