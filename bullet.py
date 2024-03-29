import pygame
import settings
import element
import random

class Bullet(element.Element):
    def __init__(self,game,x,y,wave,deviation=0.0):

        bulletSet = "CEG"[game.powerUp]

        imgDir = 'Lasers/Set' + bulletSet
        super().__init__(game,x,y,imgDir)

        self.done = False
        self.game.soundFx.playSound('bullet')
        self.deviation = deviation

        image = super().loadAnimationFrame(f'Laser{bulletSet}',wave - 1, 90, 0.25)
        #image1 = pygame.transform.rotozoom(image,90,.25)

        self.animation.append(image)

        image = pygame.transform.flip(image,True,False)
        self.animation.append(image)

        super().setAnimationFrame(self.animation[0],True)

        self.noOfFrames = 2
        self.speed = 24

        self.dX = 0
        if deviation != 0:
            self.dX = self.deviation

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / 4

    def update(self):
        super().move(self.dX,-1,self.speed-1,False)
        #self.Y -=24

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        frameNo = frameNo % 2

        super().setAnimationFrame(self.animation[frameNo],True)

        if self.Y < settings.PlayableArea.Top - self.rect.height:
            self.done = True
        else:
            self.rect.centerx = self.X
            self.rect.centery = self.Y


