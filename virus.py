import pygame
import settings
import element
import hostile
import random

class Virus(hostile.Hostile):

    def __init__(self,game,X,Y):
        super().__init__(game,1,14,500,.2,1)

        self.reflective = False

        self.speed = 6
        self.movementTimerReset = settings.FRAMES_PER_SECOND / 2
        self.movementTimer = 1

        self.X = X
        self.Y = Y
        #self.myValue = 500
        self.dY = 1
        #self.hitValue = 3

    def update(self):
        self.targetPlayerAI(self.game.Player)
        self.wrapLeftAndRight()
        self.fallOffTheBottom()   

        super().setAnimationFrame(self.animation[self.Colour],True)
