from parse import ParseError, eval_line
from sy import to_postfix


def read_line(line):
    try:
        return to_postfix(line)
    except ParseError as e:
        return str(e)


def do_loop():
    try:
        while ...:
            print("repl> ", end="")
            line = input()
            print(read_line(line))
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    do_loop()
