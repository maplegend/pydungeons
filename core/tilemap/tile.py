import pygame


class Tile:
    def __init__(self, texture, rect=pygame.Rect(0, 0, 0, 0)):
        self.rect = rect
        self.texture = texture
