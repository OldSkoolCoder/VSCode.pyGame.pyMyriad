import pygame
import settings
import element
import hostile
import random

class Floater(hostile.Hostile):
    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave, 0.15)

        self.movementTimer = 1

        self.dY = 0
        self.prevdX = 0
        if self.determineRowPosition(HostileNo) % 2 == 1:
            self.dX = -1
        else:
            self.dX = 1

    def update(self):
        self.wrapBottomToTop()

        self.zigzagMovement(self.movementTimer)

        self.updateMovementTimer()

        super().setAnimationFrame(self.animation[self.Colour],True)

