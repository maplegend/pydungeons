from ..component import Component
from .transform import TransformComponent
from ..events.update import UpdateEvent
from core.collision_handler import CollisionsHandler
from core.math.line_segment import LineSegment
from core.math.vector2 import Vector2
from .renderer import RendererComponent
from core.renderers.tile_renderer import TileRenderer


class MoveComponent(Component):
    def __init__(self, acceleration, max_speed, normalize=True, flip=True):
        super().__init__()
        self.velocity = Vector2()
        self.direction = Vector2()
        self.acceleration = acceleration
        self.max_speed = max_speed
        self.entity = None
        self.normalize = normalize
        self.flip = flip

    def set_direction(self, x, y):
        self.direction = Vector2(x, y)

    def add_direction(self, x, y):
        self.direction += Vector2(x, y)

    def update(self, event):
        if self.direction.magnitude() == 0:
            return

        trans = self.entity.get_component(TransformComponent)
        if not trans:
            return

        if self.normalize and self.direction.magnitude() != 0:
            self.direction.normalize_ip()

        if self.flip:
            rend = self.entity.get_component(RendererComponent)
            if isinstance(rend.renderer, TileRenderer):
                rend.renderer.flip = self.direction.x < 0

        if (self.velocity + self.direction*self.acceleration).magnitude() > self.max_speed:
            self.velocity = self.direction*self.max_speed
        else:
            self.velocity += self.direction * self.acceleration

        line = LineSegment(trans.pos, trans.pos+self.velocity)
        col_point = self.entity.scene.game.collision_handler.check_collision(line)
        if col_point is not None:
            pass
            #trans.position = col_point
        else:
            trans.position = trans.pos + self.velocity
        self.direction *= 0

    def applied_on_entity(self, entity):
        self.entity = entity
        event_manager = entity.scene.game.event_manager
        event_manager.bind(UpdateEvent, self.update)
