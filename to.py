#!/bin/python3


def menu():
    print("""
    help:
        
        a   make a new to
        e   edit a to
        c   completion an entire to
        d   done one task from a to
        p   print all todo's
        w   write to disk and exit
        crtl+c  to cancel
        """)

command = str()
while(command != "q" or command != "quit"):
    command = input("command (m for menu): ")
    if(command == 'm'):
        menu()
    