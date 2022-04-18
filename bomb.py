import pygame
import settings
import element
import random

class Bomb(element.Element):
    def __init__(self,game,x,y):

        imgDir = 'Bombs'
        super().__init__(game,x,y,imgDir)

        self.imDead = False
        self.game.soundFx.playSound('laser6')

        self.noOfFrames = 8
        super().loadAnimationSeries(f'BombN-',self.noOfFrames,0,.5)

        super().setAnimationFrame(self.animation[random.randint(0,7)],True)

        self.speed = 8

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 4
        self.reflective = False
        self.myValue = 0

    def update(self):
        super().move(0,1,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        #frameNo = int(self.tickCounter // self.ticksPerFrame)
        #frameNo = frameNo % 2

        #super().setAnimationFrame(self.animation[frameNo],True)

        if self.Y > settings.Screen.HEIGHT + self.rect.height:
            self.imDead = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


