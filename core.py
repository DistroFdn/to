#!/bin/python3

import json
import os
import sys
from json import load

class TColor:
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
               done one task from a to
        
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
            print(TColor.NORMAL+lstto[i]+":")
            to_count_done = 0
            todo_count = 0
            to_count_list = len(fli['to'][lstto[i]])
            for j in fli['to'][lstto[i]]:
                if(j['done']=='False'):
                    todo_count += 1
                    if(j['priority'] == 1):
                        print(TColor.GREEN+"\t"+str(todo_count)+"."+j['task'])
                    elif(j['priority'] == 2):
                        print(TColor.YELLOW+"\t"+str(todo_count)+"."+j['task'])
                    elif(j['priority'] == 3):
                        print(TColor.RED+"\t"+str(todo_count)+"."+j['task'])
                elif(j['done'] == 'True'):
                    to_count_done += 1
            if(to_count_done == to_count_list):
                print(TColor.BLUE+'\t'+'all done')

def PrintDone():
    done_count = 0
    print("you done:")
    with open(".to", 'r') as fli:
        fli = load(fli)
        lstto = fli['to'].keys()
        for i in lstto:
            print(TColor.NORMAL+"\n\t"+i+":")
            for j in (fli['to'][i]):
                if(j['done'] == 'True'):
                    print(TColor.CYAN+"\t\t"+j['task'])
                    done_count += 1
    print(TColor.BLUE+"\n"+str(done_count) + " task done")

def DoneTask():
    with open('.to', 'r') as fli:
        to_count = 1
        fli = json.load(fli)
        for i in fli['to'].keys():
            print(TColor.CYAN+str(to_count)+". "+i)
            to_count += 1
        which_to = int(input(TColor.NORMAL+'select a to[0 to quit]: '))
        if(which_to != 0):
            task_count = 0
            done_count = 0
            tag = list(fli['to'].keys())[which_to-1]
            if(len(fli['to'][tag]) != 0):
                for i in fli['to'][tag]:
                    task_count += 1
                    if(i['done'] == "False"):
                        print(TColor.YELLOW+str(task_count)+". "+i['task'])
                        done_count += 1
                if(done_count != 0):
                    task_num = int(input(TColor.NORMAL+'which task[0 to quit]: '))
                    fli['to'][tag][task_num-1]['done'] = 'True'
                    with open('.to', 'w') as fliw:
                        fliw.write(json.dumps(fli,indent=4))
                        print(TColor.BLUE+'done')
                else:
                    print(TColor.BLUE+"you did all the task's")
            else:
                print(TColor.RED+'there is no task in this to')

def CompletTo():
    with open('.to', 'r') as fli:
        tag_count = 1
        fli = json.load(fli)
        for i in list(fli['to'].keys()):
            print(TColor.GREEN+str(tag_count)+". "+i)
            tag_count += 1
        which_to = int(input(TColor.NORMAL+'select to[0 to quit]: '))
        if(which_to != 0):
            tag = list(fli['to'].keys())[which_to-1]
            for k in fli['to'][tag]:
                k['done'] = 'True'
            tmp_fli = (json.dumps(fli, indent=4))
            with open('.to', 'w') as fliw:
                fliw.write(tmp_fli)
                print(TColor.BLUE+"done")

def InsertTask():
    with open('.to', 'r') as fli:
        tag_count = 1
        pri = ('low','normal','high')
        fli = json.loads(fli.read())
        for i in fli['to'].keys():
            print(TColor.CYAN+str(tag_count)+". "+i)
            tag_count += 1
        tag = int(input(TColor.NORMAL+"select a to[0 to quit]: "))
        if(tag != 0):
            tag = list(fli['to'].keys())[tag-1]
            task = input(TColor.GREEN+'task: ')
            for i in range(3):
                print(TColor.BLUE+str(i+1) + ". " +pri[i])
            priority = input(TColor.GREEN+'priority: ')
            newtask = {"done":"False","task":task,"priority":int(priority)}
            fli['to'][tag].append(newtask)
            fli = (json.dumps(fli, indent=4))
            with open('.to', 'w') as fliw:
                fliw.write(fli)

def AddTo():
    with open('.to', 'r') as fli:
        tag = input(TColor.GREEN+'to[0 to quit]: ')
        if(tag != '0'):
            fli = json.load(fli)
            fli['to'][tag] = []
            fli = json.dumps(fli, indent=4)
            with open('.to', 'w') as fliw:
                fliw.write(fli)
                print(TColor.BLUE+tag,'added')
                # bug is if we have a tag, we can override it. it should fix