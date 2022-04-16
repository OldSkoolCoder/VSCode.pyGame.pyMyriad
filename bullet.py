import pygame
import settings
import element
import random

class Bullet(element.Element):
    def __init__(self,game,x,y,wave):

        bulletSet = "CEG"[game.powerUp]

        imgDir = 'Lasers/Set' + bulletSet
        super().__init__(game,x,y,imgDir)

        self.done = False
        
        image = super().loadAnimationFrame('Laser' + bulletSet,wave - 1)
        image1 = pygame.transform.rotozoom(image,90,.25)

        self.animation.append(image1)

        image2 = pygame.transform.flip(image1,True,False)
        self.animation.append(image2)

        super().setAnimationFrame(self.animation[0],True)

        self.noOfFrames = 2

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 4
        

    def update(self):
        self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        frameNo = frameNo % 2

        super().setAnimationFrame(self.animation[frameNo],True)

        if self.Y < -self.rect.height:
            self.done = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


