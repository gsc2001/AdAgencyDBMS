import subprocess as sp


def createMenu(menuName: str, options: dict, connection, cursor, wait_at_last: bool = False):
    while True:
        _ = sp.call('clear', shell=True)

        keys = list(options.keys())
        print(f"=============={menuName}==================")
        print('0. Back\n' + '\n'.join([f'{i+1}. {key}' for (i, key) in enumerate(keys)]) + '\n')
        ch = input("Enter your choice > ")
        if ch == '0':
            return
        elif ch in map(str, range(1, len(keys) + 1)):
            options[keys[int(ch) - 1]](connection, cursor)
        else:
            print("Invalid option\n")
        connection.rollback()
        if wait_at_last:
            _ = input('Press any key to continue')
