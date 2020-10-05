import subprocess as sp
from .menus import add_menu, read_menu, delete_menu, update_menu
from ..utils.createCLI import createCLI, printHelp


def repl(connection, cursor):
    print("Commands\n")
    printHelp()
    createCLI("Menu", {
        'Add': add_menu,
        'Update': update_menu,
        'Delete': delete_menu,
        'View': read_menu
    }, connection, cursor, False, 'Exit')
