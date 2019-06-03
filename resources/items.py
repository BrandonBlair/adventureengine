from .thing import Thing


class Door(Thing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.locked = kwargs.get('locked', False)


class Window(Thing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.locked = kwargs.get('locked', False)
        
        
class Clue(Thing):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.locked = kwargs.get('locked', False)