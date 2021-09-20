class AbstractConstraint:
    def __init__(self, **kwargs):
        self.error_message = None
        if 'error_message' in kwargs:
            self.error_message = kwargs['error_message']

        if self.error_message is None:
            self.error_message = 'Constraint violation.'

    def check(self, data) -> bool:
        raise NotImplementedError