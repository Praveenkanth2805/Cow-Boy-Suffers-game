from core.game_state import GameState
from direct.gui.OnscreenText import OnscreenText

class GameOverState(GameState):

    def enter(self):
        self.text = OnscreenText(
            text="GAME OVER\nPress R to Restart",
            pos=(0, 0),
            scale=0.1,
            fg=(1,0,0,1),
            align=1
        )

        self.engine.accept("r", self.restart)

    def restart(self):
        from core.play_state import PlayState
        self.engine.scene_manager.change_state(PlayState(self.engine))

    def exit(self):
        self.text.destroy()