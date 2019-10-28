import pygame
from core.math.rect import Rect


class CollisionsHandler:
    def __init__(self):
        self.colliders = []

    def check_collision(self, line):
        for coll in self.colliders:
            #r = coll.get_collider()
            if isinstance(coll, Rect):
                return coll.intersect_line(line)

            for rect in coll:
                intr = rect.intersect_line(line)
                if intr is not None:
                    return intr
            return None

    def add_collider(self, collider):
        self.colliders.append(collider)
