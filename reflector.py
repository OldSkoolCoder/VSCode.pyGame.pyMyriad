import pygame
import settings
import element
import hostile
import random

class Reflector(hostile.Hostile):

    def __init__(self,game,X,Y):
        super().__init__(game,1,10,0,.3,2)

        self.reflective = True

        self.speed = 2
        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 1

        self.X = X
        self.Y = Y
        self.myValue = 0
        self.dY = 1

    def update(self):
        self.fallOffTheBottom()   

        super().setAnimationFrame(self.animation[self.Colour],True)
