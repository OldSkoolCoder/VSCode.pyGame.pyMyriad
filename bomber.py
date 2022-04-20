import pygame
import settings
import element
import hostile
import random

class Bomber(hostile.Hostile):

    def __init__(self,game,X,Y):
        super().__init__(game,1,11,random.randint(1,6) * 100,.3,2)

        self.reflective = False

        self.speed = 2
        self.movementTimerReset = settings.FRAMES_PER_SECOND / 2
        self.movementTimer = 1

        self.X = X
        self.Y = Y
        #self.myValue = random.randint(1,6) * 100
        self.dY = 1

    def update(self):
        self.targetPlayerAI(self.game.Player)
        self.wrapLeftAndRight()
        self.fallOffTheBottom()   

        super().setAnimationFrame(self.animation[self.Colour],True)
