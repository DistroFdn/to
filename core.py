#!/bin/python3

import json
import os
import sys
from json import load
from datetime import datetime, date
import initer

'''
This is the main file and the center of important tasks of the program.
In this file, the definition of various methods for
running the program is set.
'''

#In this method, it displays the config data in the created file
#Such as E-mail and username
def Uconf():
    conf_path = None
    if os.name == "nt":
        conf_path = str(initer.Whoami()) + '\\to.conf'
    else:
        conf_path = str(initer.Whoami()) + '/.local/share/to.conf'
    with open(conf_path, 'r') as fli:
        fli = json.load(fli)
        return (str(fli['username']), fli['email'])

# This method will get the deadline from user, if user inpute be incorrect. the method will try again.
def GetDate():
    ''' This part is responsible for receiving the target year '''
    check_y =True
    while check_y:
        deadline_y = (input(TColor.GREEN+f'Deadline Years: '))
        if deadline_y.isdigit() and int(deadline_y) < 5 and int(deadline_y) >= 0:
            deadline_y = int(deadline_y)
            break
        elif(deadline_y == ''):
            deadline_y = 0
            break
        else:
            print(TColor.RED+f'{deadline_y} years is too far,'
                            'should be less than 5 years and greater'
                            'than or equal to 0')

    ''' This section is responsible for receiving the target month '''
    check_m =True
    while check_m:
        deadline_m = (input(TColor.GREEN+f'Deadline Months: '))
        if deadline_m.isdigit() and (int(deadline_m) < 12) and (int(deadline_m) >= 0):
            deadline_m = int(deadline_m)
            break
        elif(deadline_m == ''):
            deadline_m = 0
            break
        else:
            print(TColor.RED+f'Months should be less than 12 and greater than or equal to 0')

    ''' This section is the task of receiving the target week '''
    check_w =True
    while check_w:
        deadline_w = (input(TColor.GREEN+f'Deadline Weeks: '))
        if deadline_w.isdigit() and (int(deadline_w) <= 4) and (int(deadline_w) >= 0):
            deadline_w = int(deadline_w) * 7
            break
        elif(deadline_w == ''):
            deadline_w = 0
            break
        else:
            print(TColor.RED+f'Weeks should be less than 5 and greater than or equal to 0')
            deadline_m = int(deadline_m)


    '''
    This section is the task of receiving the target day
    and the conversion and time intervals of day,
    week, year and month
    '''
    check_d =True
    while check_d:
        deadline_d = (input(TColor.GREEN+f'Deadline Days: '))
        if deadline_d.isdigit() and (int(deadline_d) < 7) and (int(deadline_d) >= 0):
            deadline_m = int(deadline_m)
            deadline_w = int(deadline_w)
            deadline_y = int(deadline_y)
            deadline_d = int(deadline_d)
            tmp = deadline_w + deadline_d

            if(tmp <= 30):
                tmp += datetime.now().day
                if(tmp <= 30):
                    deadline_d = (deadline_w + deadline_d + datetime.now().day)
                    break
                else:
                    deadline_m += int((deadline_d + deadline_w + datetime.now().day) / 30)
                    deadline_d = int((deadline_d + deadline_w + datetime.now().day) % 30)
                    break
            else:
                print(TColor.RED+'Sum of days and weeks is greater than 30')
        elif(deadline_d == ''):
            deadline_d = datetime.now().day
            break
        else:
            print(TColor.RED+f'Days should be less than 7 and '
                            'greater than or equal to 1')

    # Calculate target deadlines
    Deadline = {
            "y":datetime.now().year + deadline_y,
            "m":datetime.now().month + deadline_m,
            "d":deadline_d
        }

    return Deadline

# will tell us how much time do we have to done our task, this function is use in PrintTask
def TimeLeft(task):
    NOW = datetime.now()
    nowline = date(NOW.year, NOW.month, NOW.day)
    deadline = date(task['deadline']['y'], task['deadline']['m'], task['deadline']['d'])
    # an object will return which have some property like: day
    return deadline - nowline

# every time you call this functin, function will send a dictionary of the towday date
def SetDate():
    time = {
    'y' : datetime.now().year,
    'm' : datetime.now().month,
    'd' : datetime.now().day
    }
    return time

def CheckFile(init):
        '''
        this function will check .to file exist or not.
        if it wasn't it will exist and init == false the program with exit
        code 2 if init == true program will make the file.
        '''
        if(not os.path.isfile('.to')):
            if(init == True):
                struct = {'to':{}}
                with open('.to', 'w') as fli:
                    fli.write(json.dumps(struct, indent=4))
            else:
                print(TColor.RED+'Error: first add a to')
                sys.exit(2)

# this function will get max and min and then print a progress bar in the screen.
def bar(min, max):
    bar = (min / max) * 100
    tmp = int(bar)
    spacebar = 100 - bar
    spacebar = int(spacebar) * '_'
    bar = int(bar) * '|'
    print(TColor.GREEN+'[' + bar + spacebar + ']',str(tmp)+'%')
    print('\n')

# theas color is for the linux terminal. every time that program need color. its enough to call one variable of this class
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

# this functin is for the intractive menu.
def MenuIntractive():
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
            cr      Create README.md in your github repo
            ur      update README.md for change .to tile


        quit and exit:
            q  exit

        change config:
            cf  change to.conf file
        """)

# this function is for non-intractive menu
def MenuNonIntractive():
    print("""
        help:

            add:
                add         add a new to
                insert      insert a task under a to
                edit        edit a task or to

            done:
                fill        completion an entire to
                done        done one task from a to
                undone      undone one task

            print:
                list        print all todo's
                show        show task's wich you done

            progress:
                prog        show a percentage and a progress of what you done
                log         show a log of what you done.

            """)

# this function will clear the intractive-command-line
def Clear():
    if(sys.platform == 'linux'):
        os.system('clear')
    elif(sys.platform == 'win32' or sys.platform == 'win64'):
        os.system('cls')

# this function will list all task and thair dead line on the screen
def PrintTask():
    CheckFile(False)
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
                        print('\n'+TColor.GREEN+"\t"+'|'+'['+str(todo_count)+"]. "+j['task'])
                        if(TimeLeft(j).days >= 0):
                            print('\t'+'|'+str(TimeLeft(j).days)+' days left')
                        elif(TimeLeft(j).days < 0):
                            print('\t'+'|'+'expiered '+str(TimeLeft(j).days) + ' days ago')
                    elif(j['priority'] == 2):
                        print('\n'+TColor.YELLOW+"\t"+'|'+'['+str(todo_count)+"]. "+j['task'])
                        if(TimeLeft(j).days >= 0):
                            print('\t'+'|'+str(TimeLeft(j).days)+' days left')
                        elif(TimeLeft(j).days < 0):
                            print('\t'+'|'+'expiered '+str(TimeLeft(j).days) + ' days ago')
                    elif(j['priority'] == 3):
                        print('\n'+TColor.RED+"\t"+'|'+'['+str(todo_count)+"]. "+j['task'])
                        if(TimeLeft(j).days >= 0):
                            print('\t'+'|'+str(TimeLeft(j).days)+' days left')
                        elif(TimeLeft(j).days < 0):
                            print('\t'+'|'+'expiered '+str(TimeLeft(j).days) + ' days ago')
                elif(j['done'] == 'True'):
                    to_count_done += 1
            if(to_count_done == to_count_list):
                print(TColor.BLUE+'\t'+'all done')

# this function will print all doned task
def PrintDone():
    CheckFile(False)
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

# this functin will done a task fron a list of to
def DoneTask():
    __tmp__ = False
    try:
        CheckFile(False)
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
                            fli['to'][tag][task_num-1]['by'] = {
                                'username':Uconf()[0],
                                'email':Uconf()[1],
                                'doneat': SetDate()
                                }
                            with open('.to', 'w') as fliw:
                                fliw.write(json.dumps(fli,indent=4))
                                print(TColor.BLUE+'done')
                                __tmp__ = 'done:\n' + '\t' + tag + ': ' + fli['to'][tag][task_num-1]['task']
                                return __tmp__
                        else:
                            return __tmp__
                    else:
                        print(TColor.BLUE+"you did all the task's")
                else:
                    print(TColor.RED+'there is no task in this to')
            else:
                return __tmp__
    except Exception as e:
        print(TColor.RED+str(e))
        return __tmp__

# this function will full complete a list of to
def CompletTo():
    __tmp__ = []
    try:
        CheckFile(False)
        with open('.to', 'r') as fli:
            tag_count = 1
            fli = json.load(fli)
            for i in list(fli['to'].keys()):
                print(TColor.GREEN+str(tag_count)+". "+i)
                tag_count += 1
            which_to = int(input(TColor.NORMAL+'select to[0 to quit]: '))
            if(which_to != 0):
                tag = list(fli['to'].keys())[which_to-1]
                __tmp__.append(tag)
                for k in fli['to'][tag]:
                    k['done'] = 'True'
                    __tmp__.append(k['task'])
                tmp_fli = (json.dumps(fli, indent=4))
                with open('.to', 'w') as fliw:
                    fliw.write(tmp_fli)
                    print(TColor.BLUE+"done")
                    return __tmp__
    except Exception as e:
        print(TColor.RED+str(e))
        __tmp__ = False
        return __tmp__

# this function will insert a task in a list of to
def InsertTask():
    try:
        CheckFile(False)
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
                if(priority == ''):
                    priority = 2
                newtask = {
                    "done":"False","task":task,"priority":int(priority),
                    "deadline":GetDate(),
                    'begintime':SetDate()
                    }
                fli['to'][tag].append(newtask)
                fli = (json.dumps(fli, indent=4))
                with open('.to', 'w') as fliw:
                    fliw.write(fli)
    except Exception as e:
        print(TColor.RED+str(e))

# this function is for add a to
def AddTo():
    try:
        CheckFile(True)
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
    except Exception as e:
        print(TColor.RED+str(e))

# this function is to edit a task
def Edit():
    try:
        CheckFile(False)
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
                        newpriority = int(input(TColor.NORMAL+'select new priority: '))
                        newdone = fli['to'][tag][task_num-1]['done']
                        newtask = {'done' : newdone,'task' : newtask, 'priority' : newpriority}
                        fli['to'][tag][task_num-1] = newtask
                        fli['to'][tag][task_num-1]['deadline'] = GetDate()
                        with open('.to', 'w') as fliw:
                            fliw.write(json.dumps(fli, indent=4))
                            print('done')
    except Exception as e:
        print(TColor.RED+str(e))

# this function will use bar and .to file to print a progress. it will print a progress of all thing.
def Progress():
    CheckFile(False)
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
        if(all_task_count != 0):
            print(TColor.YELLOW + 'At All:', end=' ')
            bar(all_done_count, all_task_count)

# this function will undone a doned task
def UnDoneTask():
    try:
        CheckFile(False)
        with open('.to', 'r') as fli:
            to_count = 1
            fli = json.load(fli)
            for i in fli['to'].keys():
                print(TColor.CYAN+str(to_count)+". "+i)
                to_count += 1
            which_to = int(input(TColor.NORMAL+'select a to[0 to quit]: '))
            if(which_to != 0):
                task_count = 0
                undone_count = 0
                tag = list(fli['to'].keys())[which_to-1]
                if(len(fli['to'][tag]) != 0):
                    for i in fli['to'][tag]:
                        task_count += 1
                        if(i['done'] == "True"):
                            print(TColor.YELLOW+str(task_count)+". "+i['task'])
                            undone_count += 1
                    if(undone_count != 0):
                        task_num = int(input(TColor.NORMAL+'which task[0 to quit]: '))
                        if(task_num != 0):
                            fli['to'][tag][task_num-1]['done'] = 'False'
                            with open('.to', 'w') as fliw:
                                fliw.write(json.dumps(fli,indent=4))
                                print(TColor.BLUE+'undoned')
                    else:
                        print(TColor.BLUE+"you didn't do anything")
                else:
                    print(TColor.RED+'there is no task in this to')
    except Exception as e:
        print(TColor.RED+str(e))

# this function is to show who done what and whene done what and whene added what
def log():
    CheckFile(init=False)
    try:
        with open(".to", 'r') as fli:
            fli = load(fli)
            tag = fli['to'].keys()
            for i in tag:
                for j in (fli['to'][i]):
                    if(j['done'] == 'True'):
                        tmp_begin_date = str(j['begintime']['y']) + "-" + str(j['begintime']['m']) + "-" + str(j['begintime']['d'])
                        tmp_end_date = str(j['by']['doneat']['y']) + "-" + str(j['by']['doneat']['m']) + "-" + str(j['by']['doneat']['d'])
                        print(TColor.YELLOW + '\n' + '* {username} <{email}>'.format(username=j['by']['username'], email=j['by']['email']))
                        print(TColor.CYAN + '|' + '\t' + j['task'])
                        print(TColor.GREEN + '|' + '\t' + "added at: " + tmp_begin_date, end=(''))
                        print('\n|\t' +"done at: " + tmp_end_date)
    except Exception as e:
        print('error: '+str(e))

# this function will get a function and will save what that function return in tag named 'latest' in .to file.
def Done(f):
    __tmp__ = f()
    if(__tmp__ != False):
        with open('.to', 'r') as fli:
            fli = json.load(fli)
            fli['latest'] = __tmp__
            with open('.to', 'w') as fliw:
                fli = json.dumps(fli, indent=4)
                fliw.write(fli)

# this functin is to use the text of last doned
#task for git commit message. every time that this function called.
#this command will run: git commit -m
def Commit():
    with open('.to', 'r') as fli:
        fli = json.load(fli)
        text_to_be_commited = fli['latest']
        os.system(f'git commit -m "{text_to_be_commited}"')

path_file=None
def createReadme():
    text=('Hello ;)'
          'please Create repo in github and clone your repo also path '
          'clone repo in this input :)'
    )
    print(TColor.BLUE+text)
    print(TColor.RED+"**Enter complex path such as /home/user/file**")
    path_file = input(TColor.NORMAL+"path your clone file (end .md): ")
    conf_path = None
    if os.name == "nt":
        conf_path = str(initer.Whoami()) + '\\PathReadme.conf'
    else:
        conf_path = str(initer.Whoami()) + '/.local/share/PathReadme.conf'
    with open(conf_path, 'w') as fli:
        conf_fli = {'PathFileRepo':path_file}
        conf_fli = json.dumps(conf_fli, indent=4)
        fli.write(conf_fli)

    if os.path.exists(path_file):
        os.system('python Create.py')
        print(TColor.GREEN+'sucsses')
    else:
        print(TColor.RED+'file not exists :(')
        return

def updateREADME():
    os.system('python Create.py')
    output=('finish your README file update\n'
            'you just go to folder repo , add and commit change also push\n'
            'and Enjoy:)\n'
    )
    print(TColor.GREEN+output)


def changeConf():
    print(TColor.YELLOW + 'change username and email :)')
    username = input(TColor.CYAN + 'new usesrname: ')
    email = input(TColor.CYAN + 'new email: ')
    initer.UserConf(username, email)
