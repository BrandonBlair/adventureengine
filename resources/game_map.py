class GameMap(object):

    def __init__(self, *args, **kwargs):
        self.tiles = kwargs.get('tiles', {})

    def loc_desc(self, loc):
        desc = ""
        desc += loc.desc
        desc += "\n\n"
        desc += "Exits:\n"
        for ex in loc.exits:
            desc += ex.item.short_desc
            if ex.known:
                dest_name = self.tiles[ex.tile].name
                desc += f" ({dest_name})"
            desc += "\n"
        return desc

