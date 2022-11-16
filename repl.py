from parse import eval_expr
from sy import to_postfix, postfix_to_ast
from errors import ParseError, ExecError
from env import Env

g_frame = Env()


def read_line(line):
    global g_frame
    try:
        pf = to_postfix(line)
        ast = postfix_to_ast(pf)
        return eval_expr(ast, g_frame).sym
    except ParseError as e:
        return str(e)
    except ExecError as e:
        return str(e)


def do_loop():
    # entries = []

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
