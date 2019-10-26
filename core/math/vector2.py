import pygame


class Vector2(pygame.Vector2):
    def __int__(self, x, y):
        if isinstance(x, tuple):
            super().__init__(x)
        else:
            super().__init__(x, y)

    def xy(self):
        return self.x, self.y
