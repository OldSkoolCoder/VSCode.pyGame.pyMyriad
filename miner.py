import pygame
import settings
import element
import hostile
import mine
import random

class Miner(hostile.Hostile):

    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave,300,.4,2)
        self.animationSet = self.animation.copy()
        
        #self.myValue = 300
        self.reflective = False

        self.speed = 5
        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 1

        self.determineDiagonalStartDirection()

    def update(self):
        self.wrapBottomToTop()   
        self.wrapLeftAndRight()         
        #self.move(self.dX,0,self.speed)
        #self.X += self.dX

        if self.movementTimer == 0:
            if self.fallingOffLeftHandSide(self.X): #Hit Left Hand Side
                if self.fiftyPercentChance():
                    self.determineChangeOfDirection()
                
            if self.fallingOffRightHandSide(self.X): #Hit Right Hand Side
                if self.fiftyPercentChance():
                    self.determineChangeOfDirection()
                
            if self.twentyTwoPercentChance():
                self.determineChangeOfDirection()

            if self.fourPercentChance():
                self.game.ordinance.add(mine.Mine(self.game, self.X, self.Y))

        self.updateMovementTimer()

        super().setAnimationFrame(self.animationSet[self.Colour],True)
