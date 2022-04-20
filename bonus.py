import pygame
import settings
import element
import random

class Bonus(element.Element):
    def __init__(self,game,BonusName):

        imgDir = 'Bonus'
        super().__init__(game,0,0,imgDir)

        self.imDead = False
        self.bonusName = BonusName

        self.noOfFrames = 2
        self.animation = self.game.assets.animationsSets['Bonus'][self.bonusName].copy()

        super().setAnimationFrame(self.animation[0],True)

        self.speed = 4

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 16
        self.reflective = False
        self.myValue = 0

        self.Y = 5 + self.rect.height / 2
        self.X = random.randint((settings.PlayableArea.LeftMost + (self.rect.width + 10)), (settings.PlayableArea.RightMost - (self.rect.width + 10)))

    def update(self):
        super().move(0,0.35,self.speed-1,False)
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


