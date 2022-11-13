class Expr:
    def __init__(self, sym, children=None):
        self.sym = sym
        self.children = children

    def __repr__(self):
        return f'Expr({self.sym}, [{", ".join([c.__repr__() for c in self.children]) if self.children else ""}])'

def add(a, b):
    return Expr(a.sym + b.sym)

def sub(a, b):
    return Expr(a.sym - b.sym)

def mul(a, b):
    return Expr(a.sym * b.sym)

def div(a, b):
    return Expr(a.sym / b.sym)


ops = {
    '*': mul,
    '/': div,
    '+': add,
    '-': sub,
}


class ParseError(Exception):
    pass

def parse_expr(expr):
    tok = ""
    idx = 0

    for c in expr:
        if c in ops:
            rest = parse_expr(expr[idx + 1:])

            if not rest:
                raise ParseError

            return Expr(c, children=[Expr(int(tok)), rest])

        elif c.isdigit():
            tok += c

        elif c == "(":
            ...

        elif c == ")":
            ...
        elif c == " ":
            ...

        else:
            raise ParseError("Invalid token")
        idx += 1

    if tok:
        return Expr(int(tok))

def eval_expr(p_expr):

    # no children, so for now must be self-evaluating
    if not p_expr.children:
        return p_expr

    t_op = ops[p_expr.sym]
    return t_op(*[eval_expr(c) for c in p_expr.children])

def eval_line(s):
    # return eval_expr(parse_expr(s))
    return parse_expr(s)
