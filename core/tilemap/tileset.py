import pygame
from core.gl.gl_texture import GLTexture
from .tile_texture import TileTexture, AnimatedTileTexture


class TileSet:
    def __init__(self):
        self.tiles = {}
        self.texture, self.width, self.height = None, 0, 0

    def load(self, tex_name, tiles_info_file):
        self.texture, self.width, self.height = GLTexture.load_image(tex_name)
        f = open(tiles_info_file, "r")
        for line in f.readlines():
            if line == '':
                continue

            tile = line.split(' ')
            nums = [int(n) for n in tile[1:] if n != '']
            if len(nums) == 4:
                self.tiles[tile[0]] = TileTexture(pygame.Rect(*nums))
            elif len(nums) == 5:
                self.tiles[tile[0]] = AnimatedTileTexture(pygame.Rect(*nums[:4]), nums[4])
