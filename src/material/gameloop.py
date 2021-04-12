from sdl2 import ext, SDL_Delay, SDL_QUIT, SDL_KEYUP, SDL_KEYDOWN, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
from src.persons.player import Player
from src.material.window import create_window
from src.material.collision import check_collisions

# Created instance
_player = Player()
_data = create_window()

# Variables used in management from directional keys
k_jump = False
k_left = False
k_right = False

running = True

# Created of fuctions basic of gameloop
def handler_events():
    key_events()
    _player.velX = 0
    _player.velY = 0
    _player.position_actual = _player.stop

    if k_jump is True:
        _player.velY = -3
        _player.position_actual = _player.jump
        if k_left is True:
            _player.velX = -3
            _player.position_actual = _player.left
        elif k_right is True:
            _player.velX = 3
            _player.position_actual = _player.right
    elif k_left is True:
        _player.velX = -3
        _player.position_actual = _player.left
    elif k_right is True:
        _player.velX = 3
        _player.position_actual = _player.right


def update():
    _player.posX += _player.velX
    _player.posY += _player.velY
    _player.centerX = _player.posX + _player.bolt
    _player.centerY = _player.posY + _player.bolt
    check_collisions()


def render():
    _data['sprite'].render(_player.position_actual, int(_player.posX), int(_player.posY))


def _gameloop():
    global running
    while running:
        handler_events()
        update()
        render()
        SDL_Delay(17)
    return 0


def key_events():
    """
    This method handles the events of pressing and releasing the keys.
    get_events() = get the events of SDL
    SDL_KEYDOWN = a pressing of key
    SDL_KEYUP =  a releasing of key
    :return: null
    """
    global running, k_jump, k_left, k_right
    events = ext.get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key.keysym.sym == SDLK_SPACE:
                k_jump = True
            if event.key.keysym.sym == SDLK_LEFT:
                k_left = True
            if event.key.keysym.sym == SDLK_RIGHT:
                k_right = True

        elif event.type == SDL_KEYUP:
            if event.key.keysym.sym == SDLK_SPACE:
                k_jump = False
            if event.key.keysym.sym == SDLK_LEFT:
                k_left = False
            if event.key.keysym.sym == SDLK_RIGHT:
                k_right = False