#!/bin/python3


def menu():
    print("""
    help:
        
        a   add a new to
        i   insert a task
        c   completion an entire to
        d   done one task from a to
        p   print all todo's
        w   write to disk and exit
        q  to quit
        """)

command = str()
while(command != "q" or command != "quit"):
    command = input("command (m for menu): ")
    if(command == 'm'):
        menu()
