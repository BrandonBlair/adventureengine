class Character(object):
    MAX_HEALTH = 100
    def __init__(self, *args, **kwargs):
        self.first_name = kwargs.get('first_name', 'John')
        self.last_name = kwargs.get('last_name', 'Smith')
        self.health = kwargs.get('health', self.MAX_HEALTH)
        self.inventory = kwargs.get('inventory', dict())