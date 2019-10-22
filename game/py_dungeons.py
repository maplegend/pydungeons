import pygame
from core.game import Game
from core.entity import Entity
from core.components.renderer_component import RendererComponent
from core.components.transform import TransformComponent
from core.components.exit_on_escape import ExitOnEscape
from core.components.move import MoveComponent
from core.components.key_control import KeyControlComponent
from core.tilemap.tilemap import TileMap
from core.tilemap.tileset import TileSet
from core.tilemap.tilemap_renderer import TileMapRenderer
from core.renderers.tile_renderer import TileRenderer


class PyDungeons:
    @staticmethod
    def start():
        pygame.init()
        pygame.display.set_caption('PyDungeon')
        size = width, height = (640, 480)
        game = Game(size)
        scene = game.scene

        tilemap = Entity()
        scene.add_entity(tilemap)

        tilemap.add_component(TransformComponent(pygame.Rect(0, 0, 640, 480)))

        ts = TileSet()
        ts.load("assets/tileset.png", "assets/tileinfo.info")
        tm = TileMap(ts)
        mp = [[["F"] for _ in range(30)] for _ in range(15)]
        mp[1][0] = "W"
        mp[0][0] = ["F", "T"]
        tm.load_letters(mp, {"W": "wall_mid", "F": "floor_1", "T": "wall_top_mid"})
        tilemap.add_component(tm)
        tilemap.add_component(RendererComponent(TileMapRenderer()))

        player = Entity()
        scene.add_entity(player)

        key_bindings = [[pygame.K_a], [pygame.K_d], [pygame.K_w], [pygame.K_s]]

        player.add_component(MoveComponent(5, 2))
        player.add_component(KeyControlComponent(key_bindings))
        player.add_component(TransformComponent(pygame.Rect(40, 10, 16*2, 28*2)))
        player.add_component(RendererComponent(TileRenderer(ts.tiles["knight_f_idle_anim"], ts)))

        game.add_component(ExitOnEscape())

        game.run()

