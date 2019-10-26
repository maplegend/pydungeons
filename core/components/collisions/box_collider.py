import pygame
from .collider import Collider
from ..transform import TransformComponent


class BoxCollider(Collider):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.entity = None

    def applied_on_entity(self, entity):
        self.entity = entity

    def get_collider(self):
        trans = self.entity.get_component(TransformComponent)
        return pygame.Rect(trans.rect.x, trans.rect.y, self.size[0], self.size[1])
