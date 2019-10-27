from core.math.rect import Rect
from .collider import Collider
from ..transform import TransformComponent


class BoxCollider(Collider):
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.entity = None

    def applied_on_entity(self, entity):
        self.entity = entity
        super().applied_on_entity(entity)

    def get_collider(self):
        trans = self.entity.get_component(TransformComponent)
        return Rect(trans.x, trans.y, self.size[0], self.size[1])
