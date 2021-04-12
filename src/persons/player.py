from src.material.window import create_window


class Player:
    def __init__(self):
        _data = create_window()
        self.jump = _data['factory'].from_image(_data['resources'].get_path('poorM_jump.png'))
        self.left = _data['factory'].from_image(_data['resources'].get_path('poorM_left.png'))
        self.right = _data['factory'].from_image(_data['resources'].get_path('poorM_jump.png'))
        self.stop = _data['factory'].from_image(_data['resources'].get_path('poorM_stop_left.png'))
        self.died = _data['factory'].from_image(_data['resources'].get_path('poorM_died.png'))
        self.position_actual = self.stop
        self.posX = 100
        self.posY = 100
        self.bolt = 50
        self.velX = 3
        self.velY = 3
        self.centerX = self.posX + self.bolt
        self.centerY = self.posY + self.bolt