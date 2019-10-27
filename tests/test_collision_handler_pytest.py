import pytest
import pygame
from core.math.line_segment import LineSegment
from core.math.vector2 import Vector2
from core.math.rect import Rect
from core.collision_handler import CollisionsHandler
from core.components.collisions.box_collider import BoxCollider
from core.entity import Entity
from core.components.transform import TransformComponent
from core.game import Game


def test_collision():
    pygame.init()
    g = Game((640, 480))
    ent = Entity()
    g.scene.add_entity(ent)
    ent.add_component(TransformComponent(Vector2(1, 1)))
    col = BoxCollider((10, 10))
    ent.add_component(col)
    line = LineSegment(0, 0, 5, 5)

    assert g.collision_handler.check_collision(line) == Vector2(1, 1)

