import pygame
from core.game import Game
from core.entity import Entity
from core.components.renderer import RendererComponent
from core.components.transform import TransformComponent
from core.components.exit_on_escape import ExitOnEscape
from core.components.move import MoveComponent
from core.components.key_control import KeyControlComponent
from core.components.collisions.tile_map_collider import TileMapCollider
from core.components.collisions.screen_bounds_collsion import ScreenBoundsCollisionHandler
from core.components.name import NameComponent
from core.tilemap.tilemap import TileMap
from core.tilemap.tileset import TileSet
from core.tilemap.tilemap_renderer import TileMapRenderer
from core.renderers.tile_renderer import TileRenderer
from core.math.vector2 import Vector2
from core.renderers.image_renderer import ImageRenderer


class PyDungeons:

    @staticmethod
    def build_wall_rect(map, rect):
        for y in range(rect.height):
            if y == 0 or y == rect.height-1:
                for x in range(1, rect.width-1):
                    map[rect.y + y][rect.x + x] = "W"
            map[rect.y + y][rect.x] = "W"
            map[rect.y + y][rect.right-1] = "W"

    @staticmethod
    def start():
        pygame.init()
        pygame.display.set_caption('PyDungeon')
        size = width, height = (640, 480)
        game = Game(size)
        scene = game.scene

        tilemap = Entity()
        scene.add_entity(tilemap)
        tilemap.add_component(NameComponent("tilemap"))

        tilemap.add_component(TransformComponent(Vector2(0, 0)))

        ts = TileSet()
        ts.load("assets/tileset.png", "assets/tileinfo.info")
        tm = TileMap(ts, size)
        mp = [[["F"] for _ in range(30)] for _ in range(20)]
        mp[1][0] = "W"
        mp[0][0] = ["F", "T"]
        PyDungeons.build_wall_rect(mp, pygame.Rect(2, 2, 10, 10))
        tm.load_letters(mp, {"W": "wall_mid", "F": "floor_1", "T": "wall_top_mid"})
        tilemap.add_component(tm)
        tilemap.add_component(RendererComponent(TileMapRenderer(), size))

        player = Entity()
        scene.add_entity(player)
        player.add_component(NameComponent("player"))

        key_bindings = [[pygame.K_a], [pygame.K_d], [pygame.K_w], [pygame.K_s]]

        player.add_component(MoveComponent(5, 2))
        player.add_component(KeyControlComponent(key_bindings))
        #player.add_component(ScreenBoundsCollisionHandler(pygame.Rect(0, 0, width, height)))
        player.add_component(TileMapCollider(tm, ["wall_mid"]))
        player.add_component(TransformComponent(Vector2(100, 100)))
        player.add_component(RendererComponent(TileRenderer(ts.tiles["knight_f_idle_anim"], ts), (16*2, 28*2)))
        #player.add_component(RendererComponent(ImageRenderer("assets/tileset.png"), (1000, 1000)))

        game.add_component(ExitOnEscape())

        game.run()

