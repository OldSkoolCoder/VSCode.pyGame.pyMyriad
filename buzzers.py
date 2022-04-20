import pygame
import settings
import element
import hostile
import bomb
import random

class Buzzers(hostile.Hostile):
    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave,200,.3,2)

        self.movementTimerReset = settings.FRAMES_PER_SECOND / 6
        self.movementTimer = 1

        self.speed = 7
        #self.myValue = 200
        self.dY = 0
        self.prevdX = 0
        self.dX = self.determineStartXDirection()
        self.dropping = False

    def update(self):
        didFallOffScreen = self.wrapBottomToTop()
        if didFallOffScreen:
            self.dX = self.determineStartXDirection()
            self.dY = 0
            self.dropping = False

        if self.dropping == False:
            self.zigzagMovement(self.movementTimer)

        if self.movementTimer == 0 and not self.dropping:
            if self.fourPercentChance():
                self.game.ordinance.add(bomb.Bomb(self.game, self.X, self.Y + self.rect.height/2))

            if self.fourPercentChance():
                self.dropping = True
                self.dX = 0
                self.dY = 1


        self.updateMovementTimer()

        super().setAnimationFrame(self.animation[self.Colour],True)

