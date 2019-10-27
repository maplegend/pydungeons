import pygame
from core.renderer import Renderer
from core.renderers.tile_renderer import TileRenderer
from .tilemap import TileMap
from OpenGL.GL import *


class TileMapRenderer(Renderer):
    def __init__(self, size=None):
        self.size = size

    def render(self, entity, rect):
        tmap = entity.get_component(TileMap)
        if map is None:
            return
        tm = tmap.tile_map
        for row in tm:
            for tiles in row:
                for tile in tiles:
                    if not tile.texture.is_baked:
                        tile.texture.bake(tmap.tileset, (tile.rect.width, tile.rect.height))
                    TileRenderer.render_tile(tile.texture, pygame.Vector2(tile.rect.x, tile.rect.y))



