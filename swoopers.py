import pygame
import settings
import element
import hostile
#import random

class Swooper(hostile.Hostile):
    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave)

        self.movementTimerReset = settings.FRAMES_PER_SECOND /2
        self.myValue = 150

        self.dY = 1
        self.dX = self.determineRandomDirection()


    def update(self):
        self.wrapBottomToTop()
        self.wrapLeftAndRight()

        if self.movementTimer == 0:
            self.determineRandomChangeOfDirection()

        self.updateMovementTimer()

        super().setAnimationFrame(self.animation[self.Colour],True)
