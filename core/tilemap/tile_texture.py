class TileTexture:
    def __init__(self, rect):
        self.rect = rect


class AnimatedTileTexture(TileTexture):
    def __init__(self, rect, frames):
        super().__init__(rect)
        self.frames = frames