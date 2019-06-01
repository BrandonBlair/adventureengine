from .thing import Thing


class Door(Thing):
    def __init__(self, *args, **kwargs):
        self.locked = kwargs.get('locked', False)