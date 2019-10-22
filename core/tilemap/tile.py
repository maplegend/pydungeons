class Tile:
    def __init__(self, rect):
        self.rect = rect


class AnimatedTile(Tile):
    def __init__(self, rect, frames):
        super().__init__(rect)
        self.frames = frames
