import pygame


class Tile:
    def __init__(self, texture, name, rect=pygame.Rect(0, 0, 0, 0)):
        self.rect = rect
        self.name = name
        self.texture = texture
