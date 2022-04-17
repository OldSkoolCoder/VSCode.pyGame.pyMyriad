import pygame
import settings
import element
import hostile
import random

class Box(hostile.Hostile):

    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave, 0.5)
        self.animationSet = self.animation.copy()
        
        self.animation.clear()
        super().loadAnimationSeries('Alien15-',self.noOfFrames,0,0.5)
        self.animationSetShielded = self.animation.copy()
        self.animation.clear()

        self.myValue = 250
        self.reflective = False

        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 1

        self.determineDiagonalStartDirection()

        print(self.dX, self.dY)

    def update(self):
        self.wrapBottomToTop()   
        self.wrapLeftAndRight()         
        #self.move(self.dX,0,self.speed)
        #self.X += self.dX

        if self.movementTimer == 0:
            # rotate clockwise/anticlockwise logic here
            # if self.fallingOffLeftHandSide(self.X): #Hit Left Hand Side
            #     if self.fiftyPercentChance():
            #         self.determineChangeOfDirection(self.dX, self.dY)
                
            #     if self.twentyTwoPercentChance():
            #         self.determineChangeOfDirection(self.dX, self.dY)

            # else: # Not Hit Left Hand Side
            #     if self.fallingOffRightHandSide(self.X): #Hit Right Hand Side
            #         if self.fiftyPercentChance():
            #             self.determineChangeOfDirection(self.dX, self.dY)
                    
            #         if self.twentyTwoPercentChance():
            #             self.determineChangeOfDirection(self.dX, self.dY)

            #     else: # Not Hit Right Hand Side
            #         if self.twentyTwoPercentChance():
            #             self.determineChangeOfDirection(self.dX, self.dY)

            if self.fallingOffLeftHandSide(self.X): #Hit Left Hand Side
                if self.fiftyPercentChance():
                    self.determineChangeOfDirection()
                
            if self.fallingOffRightHandSide(self.X): #Hit Right Hand Side
                if self.fiftyPercentChance():
                    self.determineChangeOfDirection()
                
            if self.twentyTwoPercentChance():
                self.determineChangeOfDirection()

            if self.fiftyPercentChance():      # 50% chance change shield state
                self.reflective = not self.reflective

        self.updateMovementTimer()

        if self.reflective:
            super().setAnimationFrame(self.animationSetShielded[self.Colour],True)
        else:
            super().setAnimationFrame(self.animationSet[self.Colour],True)
