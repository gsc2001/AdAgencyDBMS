import subprocess as sp
from .menus import add_menu, read_menu, delete_menu, update_menu
from ..utils.createMenu import createMenu


def repl(connection, cursor):
    createMenu("Menu", {
        'Add': add_menu,
        'Update': update_menu,
        'Delete': delete_menu,
        'View': read_menu
    }, connection, cursor, False, 'Exit')
