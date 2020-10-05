import subprocess as sp

import os

from .utils.connect import connect_to_database
from .cli import repl


def main():
    _ = sp.call('clear', shell=True)
    username = os.getenv('MYSQL_USERNAME', None)
    password = os.getenv('MYSQL_PASS', None)
    if not username:
        username = input("Enter Username: ")
    if not password:
        password = input("Enter Password: ")

    connection = connect_to_database(username, password, 'AdAgency')
    if not connection:
        return

    with connection.cursor() as cursor:
        repl(connection, cursor)
