import pygame
import settings
import element
import random

class Explosion(element.Element):

    def __init__(self,game,X,Y,explosionSet):

        set = 'Set' + "123"[random.randint(0,2)]

        super().__init__(game,X,Y,'')

        self.noOfFrames = 62
        self.animation = explosionSet[set].copy()

        super().setAnimationFrame(self.animation[0],True)

        self.imDone = False
        self.tickCounter = 0

    def update(self):
        super().setAnimationFrame(self.animation[self.tickCounter],True)
        
        self.tickCounter +=1
        if self.tickCounter >= self.noOfFrames:
            self.imDone = True

