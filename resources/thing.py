from .container import Container


class Thing(Container):
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name', 'Generic Thing')
        self.short_desc = kwargs.get('short_desc', 'thing')
        self.desc = kwargs.get('desc', 'generic thing')
        self.contains = kwargs.get('contains', self.contains)
        self.gettable = kwargs.get('gettable', False)