from enum import Enum

class Direction(Enum):
    
     """ Энумиратор прдназначенный для напраления пуль, зависит от того, ко выпустил пулю: враг - DOWN = -1, игрок -  UP = 1"""
     
     UP = 1
     DOWN = -1 

class Bullet:

    """ Класс пули, пуля имеет свой урон  damage = 25 и скорость движения peed = 10"""

    damage = 25
    
    speed = 10

    def __init__(self, spawn_point,sprite, side, if_player = False):
        
        """ Конструктор класса, приниимает параметры точки выстрела по координатам x, y (self.x, self), графики пули self.sprite, направление self.width или self.height
        и выстрел игроком self.if_player"""

        self.x = spawn_point[0]
        self.y = spawn_point[1]
        self.sprite = sprite
        self.width = sprite.get_width()
        self.height = sprite.get_height()
        self.side = side
        self.if_player = if_player

    def move(self):
        """ Метод двигает пулю в определённом напралвении по оси y"""
        self.y += -1 * self.side.value * self.speed