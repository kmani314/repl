from parse import ParseError, eval_expr
from sy import to_postfix, postfix_to_ast


def read_line(line):
    try:
        pf = to_postfix(line)
        ast = postfix_to_ast(pf)
        return eval_expr(ast).sym
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
