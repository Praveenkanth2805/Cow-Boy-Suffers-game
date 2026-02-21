# systems/obstacle_manager.py

from panda3d.core import *
import random
from config import LANES, BASE_SPEED

class ObstacleManager:

    def __init__(self, engine):
        self.engine = engine
        self.obstacles = []
        self.spawn_distance = 40

        self.create_pool(10)

    def create_pool(self, count):
        for _ in range(count):
            obstacle = self.engine.loader.loadModel("models/box")
            obstacle.reparentTo(self.engine.render)
            obstacle.setScale(1.5)
            obstacle.setColor(1, 0, 0, 1)
            obstacle.hide()
            self.obstacles.append(obstacle)

    def spawn_obstacle(self):
        for obstacle in self.obstacles:
            if obstacle.isHidden():
                lane = random.choice(LANES)
                y_pos = random.randint(40, 80)
                obstacle.setPos(lane, y_pos, 1)
                obstacle.show()
                break

    def update(self, dt, speed):
        for obstacle in self.obstacles:
            if not obstacle.isHidden():
                obstacle.setY(obstacle.getY() - speed * dt)

                if obstacle.getY() < -10:
                    obstacle.hide()

        # Random spawn chance
        if random.random() < 0.02:
            self.spawn_obstacle()

    def check_collision(self, player):
        for obstacle in self.obstacles:
            if not obstacle.isHidden():
                if obstacle.getDistance(player) < 1.5:
                    obstacle.hide()
                    return True
        return False