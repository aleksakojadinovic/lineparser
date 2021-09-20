from src.common.parsers.basic import NOfParser, OfParser


class NIntsParser(NOfParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data['fcast'] = int

class NFloatsParser(NOfParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data['fcast'] = float

class SingleIntParser(OfParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data['fcast'] = int

class SingleFloatParser(OfParser):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.data['fcast'] = float