class Exit(object):

    def __init__(self, *args, **kwargs):
        self.item = kwargs.get('item', None)
        self.tile = kwargs.get('tile', None)
        self.known = kwargs.get('known', False)