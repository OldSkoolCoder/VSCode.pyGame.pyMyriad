import pygame
import settings
import element
import bullet
import shield
import explosion

class PlayerLife(element.Element):
    def __init__(self,game, X, Y):

        imgDir = 'Player/SpaceShip/'
        super().__init__(game,X,Y,imgDir)

        self.noOfFrames = 4
        self.speed = 5
        self.timer = 0
        self.rotateLeft = False
        self.haveWeFired = False
        self.held = 1       # Variable to hold reloading delay extender (Garymeg)
        self.bulletSide = 1 # Variable to hold side ship fires from (Garymeg)
        self.invincible = False # Shield Flag

        super().loadAnimationSeries('Ship',self.noOfFrames * 2,0,.35)
        super().setAnimationFrame(self.animation[0],True)

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / self.noOfFrames
        self.dX = 0
        self.dY = 0

    def update(self):
        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        super().setAnimationFrame(self.animation[frameNo],True)