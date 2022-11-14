class Mapmanager(): # класс карты
    def __init__(self): # конструктор
        self.model = 'block' # моделька
        self.texture = 'block.png' # текстура модельки
        self.color = (0.5, 0.3, 0.0, 1) # цвет модельки              
        self.startNew()
        self.addBlock((0,10, 0))
    def delBlock(self, position):
       """удаляет блоки в указанной позиции """
       blocks = self.findBlocks(position)
       for block in blocks:
           block.removeNode()
    def findBlocks(self, pos):
        return self.land.findAllMatches("=at=" + str(pos))

    def startNew(self):
        self.land = render.attachNewNode("Land") #render кориневый узел граф. сцены. attachNewNode("Land") - добавляем новый узел с картой проэкта

    def addBlock(self, position):
        self.block = loader.loadModel(self.model) # создание модельки
        self.block.setTexture(loader.loadTexture(self.texture)) # создание текстурки и закрепление на модели
        self.block.setPos(position) # position persa
        self.block.setColor(self.color) # установка цвета модельки
        self.block.reparentTo(self.land) # устанавливает родителя render для нашего об'єкта
        self.block.setTag("at", str(position))
    def clear(self):
        self.land.removeNode() # удаляет старый узел карты
        self.startNew() # добавляет новый узел карты

    def loadLand(self, filename):
        self.clear()
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    for z0 in range(int(z)+1):
                        block = self.addBlock((x, y, z0))
                    x += 1
                y += 1
        return x, y         
