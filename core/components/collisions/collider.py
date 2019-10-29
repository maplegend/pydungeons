from abc import abstractmethod
from core.component import Component
from ..game.collision_handler import GameCollisionsHandlerComponent


class Collider(Component):

    def applied_on_entity(self, entity):
        ch = entity.scene.game.get_component(GameCollisionsHandlerComponent)
        if ch is None:
            return
        ch.add_collider(self)

    @abstractmethod
    def get_collider(self):
        pass
