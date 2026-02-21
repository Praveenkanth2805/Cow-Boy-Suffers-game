# core/engine.py

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from config import *

class GameEngine(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()
        self.setup_window()
        self.setBackgroundColor(0.7, 0.8, 1)

        self.clock.setMode(self.clock.MLimited)
        self.clock.setFrameRate(TARGET_FPS)

    def setup_window(self):
        props = WindowProperties()
        props.setTitle(WINDOW_TITLE)
        props.setSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.win.requestProperties(props)