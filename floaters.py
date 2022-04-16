import pygame
import settings
import element
import random

class Floater(element.Element):

    def __init__(self,game,X,Y):

        imgDir = 'Aliens/SpaceShips/Wave01'
        super().__init__(game,X,Y,imgDir)

        self.noOfFrames = 8
        super().loadAnimationSeries('Alien01-',self.noOfFrames,0,.2)

        self.Colour = random.randint(0,7)
        super().setAnimationFrame(self.animation[self.Colour],True)

        self.imDead = False
        self.myValue = 100

        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 0
        self.dX = 1
        self.speed = 2

        self.dX = 1
        self.prevdX = 0

    def update(self):
        if not self.move(0,self.dY,self.speed):
            self.Y = 5 + self.rect.height / 2

        if not self.move(self.dX,0,self.speed):
            self.dY = 1
            self.prevdX = self.dX
            self.dX = 0
            self.movementTimer = 1

        if self.movementTimer == 0:
            if self.dY == 1:
                self.dY = 0
                if self.prevdX == 1:
                    self.dX = -1
                else:
                    self.dX = 1

        self.movementTimer +=1
        if self.movementTimer >= self.movementTimerReset:
            self.movementTimer = 0

        super().setAnimationFrame(self.animation[self.Colour],True)

