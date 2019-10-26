from abc import abstractmethod
from core.component import Component


class Collider(Component):

    @abstractmethod
    def get_collider(self):
        pass
