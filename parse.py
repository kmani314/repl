from errors import ParseError, ExecError
from env import Env


class Expr:
    def __init__(self, sym, children=None, t=None):
        self.sym = sym
        self.children = children
        self.t = t

    def __repr__(self):
        return f'Expr({self.sym}, [{", ".join([c.__repr__() for c in self.children]) if self.children else ""}])'


def add(a, b, env):
    return Expr(a.sym + b.sym)


def sub(a, b, env):
    return Expr(a.sym - b.sym)


def mul(a, b, env):
    return Expr(a.sym * b.sym)


def div(a, b, env):
    return Expr(a.sym / b.sym)


def exp(a, b, env):
    return Expr(a.sym ** b.sym)


def neg(a, env):
    return Expr(-a.sym)


def bind(sym, val, env):
    if sym.t != 'name':
        raise ExecError(f'Invalid LHS \'{sym.sym}\' for assignment')
    env.bind(sym.sym, val)
    return sym


# pyfunc, precedence (lower is first), 0 for left-associative and 1 for right, number of operands
ops = {
    '*': (mul, 2, 0, 2),
    '/': (div, 2, 0, 2),
    '+': (add, 3, 0, 2),
    '-': (sub, 3, 0, 2),
    '^': (exp, 1, 1, 2),
    '_': (neg, 3, 1, 1),
    '=': (bind, 10, 1, 2)
}


def eval_expr(p_expr, env):
    # if it's a literal
    if p_expr.t == 'op':
        # needs to handled differently since the LHS isn't defined yet
        t_op = ops[p_expr.sym][0]
        if p_expr.sym == '=':
            return t_op(p_expr.children[0], eval_expr(p_expr.children[1], env), env)

        return t_op(*[eval_expr(c, env) for c in p_expr.children], env)
    elif p_expr.t == 'name':
        return env.lookup(p_expr.sym)
    else:
        return p_expr
