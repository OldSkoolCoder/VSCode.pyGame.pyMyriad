import pygame
import settings
import element
import random

class Planets(element.Element):
    def __init__(self,game):

        super().__init__(game,0,0,'')

        self.done = False

        self.frameNo = random.randint(0,17)
        self.animation = self.game.assets.animationsSets['Planets'].copy()
        super().setAnimationFrame(self.animation[self.frameNo],True)

        self.X = random.randint((settings.PlayableArea.LeftMost + ((self.rect.width/2) + 10)), (settings.PlayableArea.RightMost - ((self.rect.width/2) + 10)))
        self.Y = -(self.rect.height / 2)

        self.noOfFrames = 2
        self.speed = 2

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 4

    def update(self):
        super().move(0,.5,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        super().setAnimationFrame(self.animation[self.frameNo],True)

        if self.Y > settings.PlayableArea.Bottom + self.rect.height:
            self.done = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


