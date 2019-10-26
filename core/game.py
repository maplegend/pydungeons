import pygame
import sys
from .entity import Entity
from .event_manager import EventManager
from .game_screen import GameScreen
from .game_renderer import GameRender
from .scene import Scene
from .events.key_press import KeyPressEvent
from .events.key_pressed import KeyPressedEvent
from .events.update import UpdateEvent


class Game(Entity):
    def __init__(self, screen_size, pipeline=None):
        super().__init__()
        self.event_manager = EventManager()
        self.game_screen = GameScreen(screen_size)
        self.renderer = GameRender(self)
        self.scene = Scene(self)
        self.pipeline = pipeline if pipeline is None else self.default_pipeline

    @property
    @staticmethod
    def default_pipeline():
        return [
            Game.handle_event,
            Game.handle_event,
            Game.trigger_game_tick,
            Game.render
        ]

    @staticmethod
    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.event_manager.trigger_event(KeyPressEvent(event.key))

    @staticmethod
    def handle_key_press(self):
        for i, k in enumerate(pygame.key.get_pressed()):
            if k != 0:
                self.event_manager.trigger_event(KeyPressedEvent(i))

    @staticmethod
    def trigger_game_tick(self):
        self.event_manager.trigger_event(UpdateEvent())

    @staticmethod
    def render(self):
        self.renderer.draw()

    def game_tick(self):
        for handler in self.pipeline:
            handler(self)

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.game_tick()
            clock.tick(60)
