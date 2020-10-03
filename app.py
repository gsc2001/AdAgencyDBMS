#!/usr/bin/env python
"""
    :author: Three of a Kind
    :brief: Database CLI for AdAgency
"""

import subprocess as sp
from utils.connect import connect_to_database
from modules.repl import repl


def main():

    _ = sp.call('clear', shell=True)
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    connection = connect_to_database(username, password, 'AdAgency')
    if not connection:
        return

    with connection.cursor() as cursor:
        repl(connection, cursor)


if __name__ == "__main__":
    main()
