# main.py
from core.play_state import PlayState
from core.engine import GameEngine
from core.scene_manager import SceneManager
from systems.save_system import SaveSystem
from direct.task import Task

class CowboySuffer(GameEngine):

    def __init__(self):
        super().__init__()

        self.scene_manager = SceneManager()
        self.save_system = SaveSystem()
        self.scene_manager.change_state(PlayState(self))
        self.taskMgr.add(self.update, "main-update")

    def update(self, task):
        dt = globalClock.getDt()
        self.scene_manager.update(dt)
        return Task.cont


if __name__ == "__main__":
    game = CowboySuffer()
    game.run()