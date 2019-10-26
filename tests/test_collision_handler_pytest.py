import unittest
from core.math.line_segment import LineSegment
from core.math.vector2 import Vector2
from core.math.rect import Rect
from core.collision_handler import CollisionsHandler
from core.components.collisions.box_collider import BoxCollider
from core.entity import Entity
from core.components.transform import TransformComponent


class CollsionHanderTests(unittest.TestCase):
    def test_collision(self):
        ent = Entity()
        ent.add_component(TransformComponent(Vector2(1, 1)))
        col = BoxCollider((10, 10))
        ent.add_component(col)
        handler = CollisionsHandler()
        handler.add_collider(col)
        line = LineSegment(0, 0, 5, 5)

        self.assertEqual(Vector2(1, 1), handler.check_collision(line))


if __name__ == '__main__':
    unittest.main()
