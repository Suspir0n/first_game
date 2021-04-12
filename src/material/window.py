from sdl2 import ext


def create_window():
    """
    This method create the window of game, passing two variables for store
    dimensions of canva and too the title from window.
    :return: null
    """
    _width = 1080
    _height = 700

    _window = ext.Window('2D Pac-Vírus', size=(_width, _height))
    _window.show()

    _resources = ext.Resources(__file__, '')
    _surface = ext.Renderer(_window)
    _factory = ext.SpriteFactory(ext.SOFTWARE)
    _sprite_renderer = _factory.create_sprite_render_system(_window)
    _processor = ext.TestEventProcessor()
    _processor.run(_window)
    pass