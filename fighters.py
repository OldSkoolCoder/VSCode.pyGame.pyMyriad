import pygame
import settings
import hostile
import bomb
import random
import reflectedBullet


class Fighter(hostile.Hostile):
    def __init__(self,game,HostileNo,Wave):     #fix image tomorrow after john has stolen waves 6 and or 7 for pods (probably use what is currently #9)
        super().__init__(game,HostileNo,Wave,0.3)

        self.myValue = 350
        self.dY = 0
        self.dX = self.determineRandomDirection()
        self.speed = 5

    def update(self):           # this enemy fires reflected bullets.
        self.wrapBottomToTop()
        self.wrapLeftAndRight()

        if self.movementTimer == 0:
            self.determineRandomChangeOfDirection()
            self.Colour = random.randint(0,7)
            if self.fourPercentChance():
                self.game.ordinance.add(bomb.Bomb(self.game, self.X, self.Y + self.rect.height/2))

            if self.fourPercentChance():
                self.game.ordinance.add(reflectedBullet.ReflectedBullet(self, self.X, self.Y, 7, 3))  # 7 since we dont know our own wave(doesnt really matter)  bullet type 3 (F)


        self.updateMovementTimer()
        super().setAnimationFrame(self.animation[self.Colour],True)