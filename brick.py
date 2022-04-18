import pygame
import settings
import element
import random

class Brick(element.Element):
    def __init__(self,game,x,y):

        imgDir = 'Bombs/Large'
        super().__init__(game,x,y,imgDir)

        self.done = False
        self.noOfFrames = 8
        self.hitValue = random.randint(4,8)

        self.loadAnimationSeries('BombL-',self.noOfFrames, 90)
        super().setAnimationFrame(self.animation[self.hitValue-1],True)

        self.speed = 2
        self.imDead = False

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 4
        self.dY = 1
        self.dX = 0

        self.noOfLayers = 5

    def update(self):
        for i in range(self.noOfLayers-1):
            if int(self.Y) == int((i + 1) * (settings.Screen.HEIGHT / self.noOfLayers)):
                self.dY = 0
        
        super().move(self.dX,self.dY,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        super().setAnimationFrame(self.animation[self.hitValue-1],True)

        if self.Y < -self.rect.height:
            self.done = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


