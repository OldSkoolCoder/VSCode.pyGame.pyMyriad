import pygame
import settings
import element
import random

class Meteorite(element.Element):
    def __init__(self,game):

        imgDir = f'/Asteroids/Small'
        super().__init__(game,-50,-50,imgDir)

        meteorSet = "ABCDEF"[random.randint(0,5)]
        self.rotation = random.randint(0,1)

        self.hitBoxScaler = .5
        self.delaying = True
        self.delayingTime = int((random.random() * 2) * settings.FRAMES_PER_SECOND)

        # Required for Hostile Group
        self.imDead = False
        self.reflective = False
        self.myValue = 10

        self.noOfFrames = 16

        super().loadAnimationSeries(f'Meteorite{meteorSet}-',self.noOfFrames)

        super().setAnimationFrame(self.animation[0],True,self.hitBoxScaler)

        self.Y = 5 + self.rect.height / 2
        self.dY = 1

        self.X = random.randint((settings.PlayableArea.LeftMost + (self.rect.width + 10)), (settings.PlayableArea.RightMost - (self.rect.width + 10)))
        self.dX = self.determineRandomDirection()

    def update(self):
        if not self.delaying:
            self.wrapBottomToTop()
            self.wrapLeftAndRight()

            self.frameNo = int(self.tickCounter // 4)

            if self.rotation == 0:
                super().setAnimationFrame(self.animation[self.frameNo],True,self.hitBoxScaler)
            else:
                frame = (self.noOfFrames-1) - self.frameNo
                super().setAnimationFrame(self.animation[frame],True,self.hitBoxScaler)

            self.tickCounter +=1
            if self.tickCounter >= (self.noOfFrames-1)*4:
                self.tickCounter = 0
        else:
            self.delayingTime -= 1
            if self.delayingTime == 0:
                self.delaying = False


