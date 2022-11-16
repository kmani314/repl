class Expr:
    def __init__(self, sym, children=None, t=None):
        self.sym = sym
        self.children = children
        self.t = t

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


def exp(a, b):
    return Expr(a.sym ** b.sym)


def neg(a):
    return Expr(-a.sym)

# pyfunc, precedence (lower is first), 0 for left-associative and 1 for right
ops = {
    '*': (mul, 2, 0, 2),
    '/': (div, 2, 0, 2),
    '+': (add, 3, 0, 2),
    '-': (sub, 3, 0, 2),
    '^': (exp, 1, 1, 2),
    'u': (neg, 3, 0, 1),
    '=': (None, -1, 0, 2)
    # ')': (None, 0),
    # '(': (None, 0),
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
    # if it's a literal
    if not p_expr.t == 'op':
        return p_expr

    t_op = ops[p_expr.sym][0]
    return t_op(*[eval_expr(c) for c in p_expr.children])
