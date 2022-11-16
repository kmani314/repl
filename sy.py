from parse import ops, ParseError


def to_postfix(expr):
    output = []
    op_stack = []
    buf = ""

    for (idx, c) in enumerate(expr):
        if c.isdigit():
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
            while op_stack[-1] != '(':
                if not op_stack:
                    raise ParseError('Mismatched Parentheses')
                output.insert(0, op_stack.pop())
            if op_stack[-1] != '(':
                raise ParseError('Mismatched Parentheses')
            op_stack.pop()
        elif c == ' ':
            ...
        else:
            raise ParseError('Unknown token')

    while op_stack:
        c = op_stack.pop()
        if c == '(':
            raise ParseError('Mismatched Parentheses')
        output.insert(0, c)

    output.reverse()
    return output
