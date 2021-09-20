from src.abstractions.abstractparser import AbstractParser


class NOfParser(AbstractParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, line, meta):
        n, fcast = meta['n'], meta['fcast']
        vals = line.split(" ")
        if n is not None and len(vals) != n:
            raise ValueError(f'Expected {n} values, got {len(vals)}')

        return [fcast(v) for v in vals]

class OfParser(NOfParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'n' in kwargs:
            raise ValueError(f'Unexpected argument `n` for OfParser (maybe use NOfParser?)')

class SingleOfParser(AbstractParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, line, meta):
        fcast = self.data['fcast']
        return fcast(line)

class MNOfMatrixParser(AbstractParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def parse(self, in_data, meta):
        n, fcast = meta['n'], meta['fcast']
        return [[fcast(entry) for entry in line.split(" ")] for line in in_data]

