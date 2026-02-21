# systems/coin_manager.py

from panda3d.core import *
import random
from config import LANES

class CoinManager:

    def __init__(self, engine):
        self.engine = engine
        self.coins = []
        self.create_pool(15)

    def create_pool(self, count):
        for _ in range(count):
            coin = self.engine.loader.loadModel("models/box")
            coin.reparentTo(self.engine.render)
            coin.setScale(0.5)
            coin.setColor(1, 1, 0, 1)
            coin.hide()
            self.coins.append(coin)

    def spawn_coin(self):
        for coin in self.coins:
            if coin.isHidden():
                lane = random.choice(LANES)
                y_pos = random.randint(40, 100)
                coin.setPos(lane, y_pos, 2)
                coin.show()
                break

    def update(self, dt, speed):
        for coin in self.coins:
            if not coin.isHidden():
                coin.setY(coin.getY() - speed * dt)

                if coin.getY() < -10:
                    coin.hide()

        if random.random() < 0.04:
            self.spawn_coin()

    def check_collection(self, player):
        collected = 0
        for coin in self.coins:
            if not coin.isHidden():
                if coin.getDistance(player) < 1.5:
                    coin.hide()
                    collected += 1
        return collected