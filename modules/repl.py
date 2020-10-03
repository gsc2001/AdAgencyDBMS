import subprocess as sp
from .create import *


def printMenu():
    print("==============Menu==================")
    print("1. Add\n2. Update\n3. Delete\n4. View\n5. Exit\n")


def repl(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        printMenu()
        ch = input("Enter your choice > ")
        if ch == '1':
            add_menu(connection, cursor)
        elif ch == '5':
            raise SystemExit


def add_menu(connection, cursor):
    _ = sp.call("clear", shell=True)

    print("==============ADD MENU==================")
    print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad\n")
    ch = input("Enter your choice > ")
    if ch == '0':
        return
    elif ch == '1':
        addActor(connection, cursor)
    elif ch == '2':
        addDirector(connection, cursor)
    elif ch == '3':
        addBrand(connection, cursor)
    elif ch == '4':
        addChannel(connection, cursor)
    elif ch == '5':
        addShow(connection, cursor)
    elif ch == '7':
        addProduction(connection, cursor)
    else:
        print("Invalid option\n")
