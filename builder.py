import pygame
import settings
import element
import hostile
import bomb
import brick
import reflector
import random

class Builder(hostile.Hostile):
    def __init__(self,game,X,Y):
        super().__init__(game,1,15,0.3)

        self.movementTimer = 1

        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 0

        self.dY = 0
        self.prevdX = 0
        self.dX = 1 / 2

        self.X = X
        self.Y = Y
        self.speed = 2

    def update(self):
        self.wrapLeftAndRight()

        if self.movementTimer == 0:
            if self.twentyTwoPercentChance():
                if self.fiftyPercentChance():
                    self.game.ordinance.add(brick.Brick(self.game, self.X, self.Y + self.rect.height/2))
                else:
                    self.game.hostiles.add(reflector.Reflector(self.game, self.X, self.Y + self.rect.height/2))
                    pass

        self.updateMovementTimer()

        super().setAnimationFrame(self.animation[self.Colour],True)

