# systems/save_system.py

import os
import json
from config import SAVE_PATH

class SaveSystem:

    def __init__(self):
        self.data = {
            "high_score": 0,
            "coins": 0,
            "unlocked_skins": [],
            "settings": {},
            "level_progress": 1
        }
        self.load()

    def load(self):
        if os.path.exists(SAVE_PATH):
            try:
                with open(SAVE_PATH, "r") as f:
                    self.data = json.load(f)
            except:
                self.save()
        else:
            self.save()

    def save(self):
        os.makedirs(os.path.dirname(SAVE_PATH), exist_ok=True)
        with open(SAVE_PATH, "w") as f:
            json.dump(self.data, f, indent=4)