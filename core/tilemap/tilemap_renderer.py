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
        start = pygame.Vector2(rect.x, rect.y)
        if self.size is None:
            scale = pygame.Vector2(rect.width/len(tm[0]), rect.height/len(tm))
        else:
            scale = pygame.Vector2(rect.width / self.size[0], self.size[1])
        for y, row in enumerate(tm):
            for x, tiles in enumerate(row):
                for tile in tiles:
                    TileRenderer.render_tile(tile, tmap.tileset, start + pygame.Vector2(x*scale.x, y*scale.y), scale)



