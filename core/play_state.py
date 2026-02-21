# core/play_state.py

from core.game_state import GameState
from panda3d.core import *
from config import LANES, GRAVITY, JUMP_FORCE, BASE_SPEED
from systems.obstacle_manager import ObstacleManager
from direct.task import Task
from systems.coin_manager import CoinManager
from direct.gui.OnscreenText import OnscreenText
import random
from core.obstacle import Obstacle

class PlayState(GameState):

    def enter(self):
        self.speed = BASE_SPEED
        self.lives = 2
        self.hit_cooldown = 0
        self.invincible_time = 1.0  # 1 second protection

        self.setup_scene()
        self.setup_player()
        self.setup_camera()

        self.obstacle_manager = ObstacleManager(self.engine)

        self.engine.accept("arrow_left", self.move_left)
        self.engine.accept("arrow_right", self.move_right)
        self.engine.accept("arrow_up", self.jump)

        self.engine.taskMgr.add(self.update_task, "play-update")
        self.coin_manager = CoinManager(self.engine)

        # Score and coins
        self.score = 0
        self.total_coins = 0

        # UI
        self.score_text = OnscreenText(
            text="Score: 0",
            pos=(-1.2, 0.9),
            scale=0.07,
            fg=(1,1,1,1)
        )

        self.coin_text = OnscreenText(
            text="Coins: 0",
            pos=(-1.2, 0.8),
            scale=0.07,
            fg=(1,1,0,1)
        )

        self.lives_text = OnscreenText(
            text="Lives: 2",
            pos=(-1.2, 0.7),
            scale=0.07,
            fg=(1,0.3,0.3,1)
        )
        

    def exit(self):
        self.engine.taskMgr.remove("play-update")

    # -----------------------
    # Scene
    # -----------------------
    def setup_scene(self):
        self.ground_tiles = []

        for i in range(3):
            tile = self.engine.loader.loadModel("models/box")
            tile.reparentTo(self.engine.render)
            tile.setScale(20, 100, 0.1)
            tile.setPos(0, i * 100, 0)
            tile.setColor(0.6, 0.5, 0.3, 1)
            self.ground_tiles.append(tile)

    # -----------------------
    # Player
    # -----------------------
    def setup_player(self):
        self.player = self.engine.loader.loadModel("models/box")
        self.player.reparentTo(self.engine.render)
        self.player.setScale(1, 1, 2)
        self.player.setPos(0, 5, 1)
        self.player.setColor(0.8, 0.3, 0.2, 1)

        self.current_lane = 1
        self.target_x = LANES[self.current_lane]

        self.velocity_z = 0
        self.on_ground = True

    # -----------------------
    # Camera
    # -----------------------
    def setup_camera(self):
        self.engine.camera.setPos(0, -20, 8)
        self.engine.camera.lookAt(self.player)

    # -----------------------
    # Controls
    # -----------------------
    def move_left(self):
        if self.current_lane > 0:
            self.current_lane -= 1
            self.target_x = LANES[self.current_lane]

    def move_right(self):
        if self.current_lane < 2:
            self.current_lane += 1
            self.target_x = LANES[self.current_lane]

    def jump(self):
        if self.on_ground:
            self.velocity_z = JUMP_FORCE
            self.on_ground = False

    # -----------------------
    # UPDATE LOOP
    # -----------------------
    def update_task(self, task):
        
        dt = globalClock.getDt()
        self.score += dt * 10
        # Increase speed gradually
        self.speed += dt * 0.5

        # Smooth lane movement
        current_x = self.player.getX()
        new_x = current_x + (self.target_x - current_x) * 10 * dt
        self.player.setX(new_x)

        # Gravity
        if not self.on_ground:
            self.velocity_z += GRAVITY * dt
            self.player.setZ(self.player.getZ() + self.velocity_z * dt)

            if self.player.getZ() <= 1:
                self.player.setZ(1)
                self.velocity_z = 0
                self.on_ground = True

        # Move ground tiles
        for tile in self.ground_tiles:
            tile.setY(tile.getY() - self.speed * dt)

            if tile.getY() < -100:
                tile.setY(tile.getY() + 300)

        # Update obstacles
        self.obstacle_manager.update(dt, self.speed)

        # Collision check
        # Reduce cooldown timer
        if self.hit_cooldown > 0:
            self.hit_cooldown -= dt

        # Collision check
        if self.hit_cooldown <= 0:
            if self.obstacle_manager.check_collision(self.player):
                self.lives -= 1
                self.hit_cooldown = self.invincible_time
                print("Hit! Lives:", self.lives)

                if self.lives <= 0:
                    self.game_over()

        # Update coins
        self.coin_manager.update(dt, self.speed)

        collected = self.coin_manager.check_collection(self.player)
        if collected > 0:
            self.total_coins += collected
            

        self.score_text.setText(f"Score: {int(self.score)}")
        self.coin_text.setText(f"Coins: {self.total_coins}")
        self.lives_text.setText(f"Lives: {self.lives}")
    
        return Task.cont
    def game_over(self):
        from core.game_over_state import GameOverState
        self.engine.scene_manager.change_state(GameOverState(self.engine))