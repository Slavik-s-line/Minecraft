class Hero():
    def __init__(self,pos,land):
        self.land = land
        self.mode = True
        self.hero = loader.loadModel('smiley')
        self.hero.setScale(0.3)
        self.hero.setColor(1, 0.5, 0)
        self.hero.setPos(pos)
        self.hero.reparentTo(render)
        self.cameraBind()
        self.accept_events()
    def cameraBind(self):
        base.disableMouse()
        base.camera.setH(180)
        base.camera.reparentTo(self.hero)
        base.camera.setPos(0, 0, 1.5)
        self.cameraOn = True
    def cameraUp(self):
        pos = self.hero.getPos()
        base.mouseInterfaceNode.setPos(-pos[0], -pos[1], -pos[2]-3)
        base.camera.reparentTo(render)
        base.enableMouse()
    def accept_events(self):
        base.accept('c', self.changeView)
        base.accept('w', self.forward)
        base.accept('w' + '-repeat', self.forward)
        base.accept('d', self.right)
        base.accept('d' + '-repeat', self.right)
        base.accept('a', self.left)
        base.accept('a' + '-repeat', self.left)
        base.accept('s', self.back)
        base.accept('s' + '-repeat', self.back)
        base.accept('q', self.turn_left)
        base.accept('q' + '-repeat', self.turn_left)
        base.accept('e', self.turn_right)
        base.accept('e' + '-repeat', self.turn_right)
        base.accept('j', self.up)
        base.accept('j' + '-repeat', self.up)
        base.accept('k', self.down)
        base.accept('k' + '-repeat', self.down)
        base.accept('mouse1', self.build)
        base.accept('mouse3', self.destroy)
    def changeView(self):
        if self.cameraOn:
            self.cameraUp()
        else:
            self.cameraBind()

    def turn_right(self):
        self.hero.setH((self.hero.getH() - 5) % 360)
    def turn_left(self):
        self.hero.setH((self.hero.getH() + 5) % 360)
    def look_at(self, angle):
        x_from = round(self.hero.getX())
        y_from = round(self.hero.getY())
        z_from = round(self.hero.getZ())

        dx, dy = self.check_dir(angle)
        x_to = x_from + dx
        y_to = y_from + dy
        return x_to, y_to, z_from

    def check_dir(self,angle):
        if angle >= 0 and angle <= 20:
            return (0, -1)
        elif angle <= 65:
            return (1, -1)
        elif angle <= 110:
            return (1, 0)
        elif angle <= 155:
            return (1, 1)
        elif angle <= 200:
            return (0, 1)
        elif angle <= 245:
            return (-1, 1)
        elif angle <= 290:
            return (-1, 0)
        elif angle <= 335:
            return (-1, -1)
        else:
            return(0, -1)
    def move_to(self, angle):
        pos = self.look_at(angle)
        self.hero.setPos(pos)

    def forward(self):
        angle = (self.hero.getH()) % 360
        self.move_to(angle)
    def left(self):
        angle = (self.hero.getH() + 90) % 360
        self.move_to(angle)

    def right(self):
        angle = (self.hero.getH() + 270) % 360
        self.move_to(angle)

    def back(self):
        angle = (self.hero.getH() + 180) % 360
        self.move_to(angle)

    def up(self):
        if self.mode:
            self.hero.setZ(self.hero.getZ() + 1)
    def down(self):
        if self.mode and self.hero.getZ() > 1:
            self.hero.setZ(self.hero.getZ() - 1)

    def build(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.addBlock(pos)
        else:
            self.hero.buildBlock(pos)
    def destroy(self):
        angle = self.hero.getH() % 360
        pos = self.look_at(angle)
        if self.mode:
            self.land.delBlock(pos)
        else:
            self.hero.delBlockFrom(pos)