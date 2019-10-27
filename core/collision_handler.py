import pygame
from core.math.rect import Rect


class CollisionsHandler:
    def __init__(self):
        self.colliders = []

    def check_collision(self, line):
        for coll in self.colliders:
            r = coll.get_collider()
            if isinstance(r, Rect):
                return r.intersect_line(line)

            for rect in r:
                intr = r.intersect_line(line)
                if intr is not None:
                    return intr
            return None

    def add_collider(self, collider):
        self.colliders.append(collider)
