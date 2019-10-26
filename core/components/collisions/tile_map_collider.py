from .collider import Collider


class TileMapCollider(Collider):
    def __init__(self, tile_map, collisions_tiles):
        super().__init__()
        self.col_tiles = collisions_tiles
        self.tile_map = tile_map
        self.entity = None

    def applied_on_entity(self, entity):
        self.entity = entity

    def get_collider(self):
        tiles = self.tile_map.tile_map
        if tiles is None:
            return False

        rects = []
        for tiles in tiles:
            for tile in tiles:
                if tile.name in self.col_tiles:
                    rects.append(tile.rect)
        return rects
