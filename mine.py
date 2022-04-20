import pygame
import settings
import element
import random

class Mine(element.Element):
    def __init__(self,game,x,y):

        imgDir = 'Bombs'
        super().__init__(game,x,y,imgDir)

        self.imDead = False

        self.noOfFrames = 2
        super().loadAnimationSeries(f'SpaceMine',self.noOfFrames,0,.5)

        super().setAnimationFrame(self.animation[0],True)

        self.speed = 4

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 16
        self.reflective = False
        self.myValue = 0

    def update(self):
        super().move(0,0.25,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        frameNo = frameNo % 2

        super().setAnimationFrame(self.animation[frameNo],True)

        if self.Y > settings.Screen.HEIGHT + self.rect.height:
            self.imDead = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


