import pygame
from core.math.rect import Rect


class CollisionsHandler:
    def __init__(self):
        self.colliders = []

    def check_collision(self, line):
        for coll in self.colliders:
            r = coll.get_collider()
            if not isinstance(r, Rect):
                r = r[0].unionall(r[1:])
            return r.intersect_line(line)

    def add_collider(self, collider):
        self.colliders.append(collider)
