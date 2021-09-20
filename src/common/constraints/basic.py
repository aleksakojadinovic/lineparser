from src.abstractions.abstractconstraint import AbstractConstraint

class MultiCondition(AbstractConstraint):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.conditions = kwargs['conditions']

    def check(self, data) -> bool:
        if len(data) != len(self.conditions):
            raise ValueError(f'Data is of length {len(data)} while there are {len(self.conditions)} conditions.')
        return all(p(d) for p, d in zip(self.conditions, data))

class SingleCondition(AbstractConstraint):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.condition = kwargs['condition']

    def check(self, data) -> bool:
        return all(self.condition(d) for d in data)


def AllPositive(**kwargs):
    kwargs['condition'] = lambda x: x > 0
    return SingleCondition(**kwargs)

def AllNegative(**kwargs):
    kwargs['condition'] = lambda x: x < 0
    return SingleCondition(**kwargs)

def AllNonNegative(**kwargs):
    kwargs['condition'] = lambda x: x >= 0
    return SingleCondition(**kwargs)

def AllNonPositive(**kwargs):
    kwargs['condition'] = lambda x: x <= 0
    return SingleCondition(**kwargs)


