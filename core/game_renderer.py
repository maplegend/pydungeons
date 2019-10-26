import pygame
from OpenGL.GL import *
from .components.renderer_component import RendererComponent
from .components.transform import TransformComponent


class GameRender:
    def __init__(self, game):
        self.game = game

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        for ent in self.game.scene.get_entities_with_component(RendererComponent):
            rend = ent.get_component(RendererComponent)
            trans = ent.get_component(TransformComponent)
            if not rend or not trans:
                continue
            rend.render(trans.rect, ent)

        pygame.display.flip()
