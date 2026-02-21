# core/scene_manager.py

class SceneManager:

    def __init__(self):
        self.current_state = None

    def change_state(self, new_state):
        if self.current_state:
            self.current_state.exit()

        self.current_state = new_state
        self.current_state.enter()

    def update(self, dt):
        if self.current_state:
            self.current_state.update(dt)