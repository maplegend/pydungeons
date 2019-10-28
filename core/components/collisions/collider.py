from abc import abstractmethod
from core.component import Component


class Collider(Component):

    def applied_on_entity(self, entity):
        entity.scene.game.collision_handler.add_collider(self.get_collider())

    @abstractmethod
    def get_collider(self):
        pass
