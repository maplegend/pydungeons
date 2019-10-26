class CollisionsHandler:
    def __init__(self):
        self.colliders = []

    def check_collision(self, line):
        for coll in self.colliders:
            if coll.collidepoint(line.end):
                pass

    def get_collide_edges(self, rect, line):
        edges = rect.edges()
        for ed in edges:
            pass


    def add_static_collider(self):
        pass

    def add_collider(self):
        pass