from errors import ExecError


class Env:
    def __init__(self, parent=None):
        self.bindings = {}

    def bind(self, sym, val):
        # if sym in self.bindings:
        #     raise ExecError(f'Duplicate bindings on symbol \'{sym}\'')

        self.bindings[sym] = val

    def lookup(self, sym):
        if sym not in self.bindings:
            raise ExecError(f'Symbol \'{sym}\' referenced without declaration')

        return self.bindings[sym]
