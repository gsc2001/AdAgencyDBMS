import subprocess as sp
import pymysql
from pymysql.cursors import DictCursor


def connect_to_database(username: str, password: str, db: str):
    try:
        connection = pymysql.connect(host='127.0.0.1', port=5005, user=username,
                                     password=password,
                                     db=db, cursorclass=DictCursor)
        _ = sp.call('clear', shell=True)

        if connection.open:
            print("Connected")
        else:
            print("Failed to connect")
        return connection

    except Exception as e:
        _ = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        print(e)
        input("Press any key to continue.")
