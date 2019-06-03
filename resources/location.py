from .container import Container


class Location(Container):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', 'Generic Location')
        self.short_desc = kwargs.get('short_desc', 'location')
        self.desc = kwargs.get('desc', 'location')

        self.attributes = kwargs.get('attributes', [])

        self.exits = kwargs.get('exits', [])

    def __str__(self):
        return f"{self.name} - {self.short_desc}"
