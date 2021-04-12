from sys import exit
from sdl2 import ext
from src.material.window import create_window
from src.material.gameloop import _gameloop

ext.init()
create_window()


if __name__ == '__main__':
    ext.quit(_gameloop())
    pass