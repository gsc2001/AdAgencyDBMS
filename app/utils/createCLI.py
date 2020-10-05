import subprocess as sp

cli_path = ["~"]

# colors
GREEN = '\033[92m'
BLUE = '\033[94m'
END = '\033[0m'
BOLD = '\033[1m'


def createCLI(
        menuName: str,
        options: dict,
        connection,
        cursor,
        wait_at_last: bool = False,
        back_keyword: str = 'Back'):
    while True:
        keys = list(options.keys())

        # print shell
        ch = input(f"{GREEN}{'/'.join(cli_path)}{BLUE}{BOLD} > {END}")

        if ch == 'ls':
            print(f"============== {BOLD}{menuName}{END} ==================")
            print(f'0. {back_keyword}\n' + '\n'.join([f'{i+1}. {key}' for (i, key) in enumerate(keys)]) + '\n')
        elif ch == '0':
            return
        elif ch in map(str, range(1, len(keys) + 1)):
            cli_path.append(keys[int(ch) - 1])
            options[keys[int(ch) - 1]](connection, cursor)
            cli_path.pop()
        elif ch[:2] == 'cd':
            opt = ' '.join(ch.split(' ')[1:])
            if opt == '..' or opt == '0':
                return
            elif opt in keys:
                cli_path.append(opt)
                options[opt](connection, cursor)
                cli_path.pop()
            elif opt in map(str, range(1, len(keys) + 1)):
                cli_path.append(keys[int(opt) - 1])
                options[keys[int(opt) - 1]](connection, cursor)
                cli_path.pop()
            elif opt == '.':
                pass
            else:
                print("Invalid Path\n")
        elif ch == 'clear':
            _ = sp.call("clear", shell=True)
        elif ch == 'help':
            printHelp()
        elif ch == 'exit':
            raise SystemExit
        else:
            print("Invalid option\n")

        connection.rollback()


def printHelp():
    print(f"{GREEN}ls{END}: View options")
    print(f"{GREEN}cd{END} {BOLD}[arg]{END}: Navigate to arg (option name or option number or {BOLD}..{END}(back))")
    print(f"{GREEN}[num]{END}: Navigate to num option number")

    print(f"{GREEN}clear{END}: Clear the output")
    print(f"{GREEN}exit{END}: Close app")
    print(f"{GREEN}help{END}: View this dialog again\n")
