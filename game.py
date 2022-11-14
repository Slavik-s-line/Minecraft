from direct.showbase.ShowBase import ShowBase # подлючить класс к базовой сцены
from mapmanager import Mapmanager # подключение для создания карты
from hero import Hero
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager() #создаем карту
        x,y = self.land.loadLand("land.txt")
        self.hero = Hero((x//2,y//2,2),self.land)
        base.camLens.setFov(90) #устанавливаем угол обзора камеры

game = Game()  
game.run() 