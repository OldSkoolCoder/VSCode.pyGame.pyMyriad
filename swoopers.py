import pygame
import settings
import element
import hostile
import bomb
import random

class Swooper(hostile.Hostile):
    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave,150,.3,2)

        self.movementTimerReset = settings.FRAMES_PER_SECOND / 4
        #self.myValue = 150

        self.dY = 1
        self.dX = self.determineRandomDirection()


    def update(self):
        self.wrapBottomToTop()
        self.wrapLeftAndRight()

        if self.movementTimer == 0:
            self.determineRandomChangeOfDirection()
            self.Colour = random.randint(0,7)
            if self.fourPercentChance():
                self.game.ordinance.add(bomb.Bomb(self.game, self.X, self.Y + self.rect.height/2))

        self.updateMovementTimer()
        super().setAnimationFrame(self.animation[self.Colour],True)
