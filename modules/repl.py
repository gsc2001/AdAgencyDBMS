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
        if ch == '4':
            read_menu(connection, cursor)
        elif ch == '5':
            raise SystemExit


def add_menu(connection, cursor):
    while True:
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

        _ = input("Enter a key to continue")


def read_menu(connection, cursor):
    while True:
        _ = sp.call("clear", shell=True)
        print("==============READ MENU==================")
        print("0. Back\n1. Actor\n2. Director\n3. Brand\n4. Channel\n5. Show\n6. Product\n7. Ad \
            \n8. Maximum of sum of the contract money of brand\n9. Bill for Ad\n10. Shows list by amount \
            \n11. Actors with Physical features\n12. Average ad production cost\
            \n13. Maximum preferred brands\n14. Partial text search for show\n15. Get best shows for an ad\n")
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

        _ = input("Enter a key to continue")
