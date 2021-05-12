#!/bin/python3

import json
import os
import sys
from json import load

def bar(min, max):
    bar = (min / max) * 100
    tmp = int(bar)
    spacebar = 100 - bar
    spacebar = int(spacebar) * '_'
    bar = int(bar) * '|'
    print(TColor.GREEN+'[' + bar + spacebar + ']',str(tmp)+'%')

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
            d   done one task from a to
            u   undone one task

        print:
            p   print all todo's
            s  show task's wich you done
            clear clear the screen
        
        progress:
            prog    show a percentage and a progress of what you done
            log     show a log of what you done.


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
                    if(task_num != 0):
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
        tag = input(TColor.NORMAL+'to[0 to quit]: ').strip()
        if(not tag in ['', '0']):
            fli = json.load(fli)
            tag_list = list(fli['to'].keys())
            if(tag in tag_list):
                print(TColor.RED+'this to is early declared')
            else:
                fli['to'][tag] = []
                fli = json.dumps(fli, indent=4)
                with open('.to', 'w') as fliw:
                    fliw.write(fli)
                    print(TColor.GREEN+tag,'added')

def Edit():
    with open('.to', 'r') as fli:
        task_count = 1
        pri = ('low', 'normal', 'high')
        fli = json.load(fli)
        for i in range(len(fli['to'].keys())):
            print(TColor.CYAN+str(i+1)+ '. ' + list(fli['to'].keys())[i])
        tag = int(input(TColor.NORMAL+'select a to[0 to quit]: '))
        if(tag != 0):
            tag = list(fli['to'].keys())[tag-1]
            for i in fli['to'][tag]:
                if(i['done'] == "True"):
                    print(TColor.BLUE+str(task_count)+ '. ' +i['task'])
                else:
                    print(TColor.YELLOW+str(task_count)+ '. ' +i['task'])
                task_count += 1
            task_num = int(input(TColor.NORMAL+'select a task[0 to quit]: '))
            if(task_num != 0):
                print(TColor.PURPPLE+fli['to'][tag][task_num-1]['task'])
                newtask = input(TColor.NORMAL+'type new task[0 to quit]: ')
                if(newtask != '0'):
                    for i in range(len(pri)):
                        print(TColor.PURPPLE+str(i+1) + '. ' + pri[i])
                    newpriority = int(input(TColor.NORMAL+'select new priority: '))-1
                    newdone = fli['to'][tag][task_num-1]['done']
                    newtask = {'done' : newdone,'task' : newtask, 'priority' : newpriority}
                    fli['to'][tag][task_num-1] = newtask
                    with open('.to', 'w') as fliw:
                        fliw.write(json.dumps(fli, indent=4))
                        print('done')

def Progress():
    with open('.to', 'r') as fli:
        all_done_count = 0
        all_task_count = 0
        fli = json.load(fli)
        for i in fli['to'].keys():
            done_count = 0
            for j in fli['to'][i]:
                all_task_count += 1
                if(j['done'] == 'True'):
                    done_count += 1
                    all_done_count += 1
            if(len(fli['to'][i]) != 0):
                print(TColor.GREEN + i, end=' ')
                bar(done_count, len(fli['to'][i]))
            if(len(fli['to'][i]) == 0):
                print(TColor.RED + i + '. ' + 'there is no task under this to')
        print(TColor.YELLOW + 'All:', end=' ')
        bar(all_done_count, all_task_count)

