import pygame
from core.renderer import Renderer
from core.tilemap.tile_texture import AnimatedTileTexture
from OpenGL.GL import *


class TileRenderer(Renderer):
    def __init__(self, tile, tileset, animate=True):
        self.tile = tile
        self.tileset = tileset
        self.frame = 0
        self.animate = animate

    def render(self, entity, rect):
        self.render_tile(self.tile, self.tileset, pygame.Vector2(rect.x, rect.y), pygame.Vector2(rect.width, rect.height), int(self.frame))
        if self.animate and isinstance(self.tile, AnimatedTileTexture):
            self.frame += 0.1
            if int(self.frame) > self.tile.frames:
                self.frame = 0

    @staticmethod
    def render_tile(tile, tileset, pos, size, frame=0):
        if frame > 0:
            x = (tile.rect.x+tile.rect.width*frame) / tileset.width
        else:
            x = tile.rect.x / tileset.width
        y = 1. - tile.rect.y / tileset.height
        w = tile.rect.width / tileset.width
        h = tile.rect.height / tileset.height
        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glBindTexture(GL_TEXTURE_2D, tileset.texture)

        # Draw the tile
        glBegin(GL_QUADS)

        # Upper left corner
        glTexCoord2f(x, y)
        glVertex2f(pos.x, pos.y)

        # Lower left corner
        glTexCoord2f(x, y - h)
        glVertex2f(pos.x, pos.y + size.y)

        # Lower right corner
        glTexCoord2f(x + w, y - h)
        glVertex2f(pos.x + size.x, pos.y + size.y)

        # Upper right corner
        glTexCoord2f(x + w, y)
        glVertex2f(pos.x + size.x, pos.y)

        glEnd()
