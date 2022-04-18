import pygame
import settings
import element
import random

class PlasmaBall(element.Element):
    def __init__(self,game,x,y):

        imgDir = 'Lasers/SetA'
        super().__init__(game,x,y,imgDir)

        self.imDead = False
        self.game.soundFx.playSound('laser3')

        image = super().loadAnimationFrame(f'LaserA',random.randint(0,9), 270, 1)
        self.animation.append(image)

        image = pygame.transform.rotozoom(image,0,.5)
        self.animation.append(image)

        super().setAnimationFrame(self.animation[0],True)

        self.noOfFrames = 2
        self.speed = 12

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 32
        self.reflective = False
        self.myValue = 0

    def update(self):
        super().move(0,1,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        frameNo = frameNo % 2

        super().setAnimationFrame(self.animation[frameNo],True)

        if self.Y > settings.PlayableArea.Bottom + self.rect.height:
            self.imDead = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


