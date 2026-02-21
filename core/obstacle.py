from panda3d.core import Vec3

class Obstacle:
    def __init__(self, engine, position):
        self.engine = engine
        self.model = engine.loader.loadModel("models/box")
        self.model.reparentTo(engine.render)
        self.model.setScale(1)
        self.model.setPos(position)

    def update(self, dt):
        # Move obstacle towards player
        self.model.setY(self.model, -10 * dt)

        # Remove if passed player
        if self.model.getY() < -10:
            self.model.removeNode()
            return False

        return True