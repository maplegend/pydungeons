import pygame
from ..component import Component


class RendererComponent(Component):
    def __init__(self, renderer):
        super().__init__()
        self.renderer = renderer

    def render(self, rect, ent):
        self.renderer.render(ent, rect)
