import re
from parse import Expr, ParseError


def return_typed(tok):
    # float, int

    # floats = '[0-9]+\.[0-9]+'
    floats = '([0-9]*\.[0-9]+|[0-9]+)'

    ints = '[0-9]+'

    if re.search(ints, tok) and tok.isnumeric():
        return Expr(int(tok), t='int')
    elif re.search(floats, tok):
        return Expr(float(tok), t='float')
    else:
        raise ParseError('Uninterpretable sequence')
