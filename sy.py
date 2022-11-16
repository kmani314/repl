from parse import ops, Expr
from types_ext import return_typed
from errors import ParseError


def to_postfix(expr):
    output = []
    op_stack = []
    buf = ""

    for (idx, c) in enumerate(expr):
        if c.isalnum() or c == '.':
            buf += str(c)
            if idx == len(expr) - 1:
                output.insert(0, buf)
            continue

        if buf:
            output.insert(0, buf)
            buf = ""

        if c in ops:
            while op_stack \
                    and op_stack[-1] != '(' \
                    and (ops[op_stack[-1]][1] < ops[c][1]
                         or (ops[op_stack[-1]][1] == ops[c][1] and ops[c][2] == 0)):
                output.insert(0, op_stack.pop())

            op_stack.append(c)
        elif c == '(':
            op_stack.append(c)
        elif c == ')':
            if not op_stack:
                raise ParseError(f'Mismatched \'{c}\'')

            while op_stack[-1] != '(':
                output.insert(0, op_stack.pop())
                if not op_stack:
                    raise ParseError(f'Mismatched \'{c}\'')

            if op_stack[-1] != '(':
                raise ParseError(f'Mismatched \'{c}\'')
            op_stack.pop()
        elif c == ' ':
            ...
        else:
            raise ParseError(f'Unknown token \'{c}\'')

    while op_stack:
        c = op_stack.pop()
        if c == '(':
            raise ParseError(f'Mismatched \'{c}\'')
        output.insert(0, c)

    output.reverse()
    return output


def postfix_to_ast(expr):
    tree = []
    for tok in expr:
        if tok in ops:
            op = ops[tok]
            arg = op[3]

            if len(tree) < arg:
                raise ParseError(f'Invalid use of \'{tok}\'')
            args = tree[-arg:]
            tree = tree[:-arg]
            tree.append(Expr(tok, args, t='op'))
        else:
            tree.append(return_typed(tok))
    return tree[0]
