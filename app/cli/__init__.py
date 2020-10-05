import subprocess as sp
from .menus import add_menu, read_menu, delete_menu, update_menu


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
        elif ch == '2':
            update_menu(connection, cursor)
        elif ch == '3':
            delete_menu(connection, cursor)
        elif ch == '4':
            read_menu(connection, cursor)
        elif ch == '5':
            raise SystemExit
