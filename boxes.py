import pygame
import settings
import element
import random

class Box(element.Element):

    def __init__(self,game,X,Y):

        imgDir = 'Aliens/SpaceShips/Wave14'
        super().__init__(game,X,Y,imgDir)
        self.noOfFrames = 8
        super().loadAnimationSeries('Alien14-',self.noOfFrames,0,0.5)
        self.animationSet = self.animation.copy()
        
        imgDir = 'Aliens/SpaceShips/Wave15'
        super().__init__(game,X,Y,imgDir)
        self.noOfFrames = 8
        super().loadAnimationSeries('Alien15-',self.noOfFrames,0,0.5)
        self.animationSetShielded = self.animation.copy()

        self.Colour = random.randint(0,7)
        super().setAnimationFrame(self.animationSet[self.Colour],True)

        self.imDead = False
        self.myValue = 250
        self.shielded = False
        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 0
        self.dX = 1
        self.dY = 0
        self.speed = 2

    def update(self):

        if not self.move(0,self.dY,self.speed):     #move in Y
            self.dY = -self.dY
            

        if not self.move(self.dX,0,self.speed):     #move in X
            self.dX = -self.dX
        
        if self.movementTimer == 0:
            if random.randint(0,100) < 22:  #22% chance change dir
                # rotate clockwise/anticlockwise logic here
                if (self.dX < 0 and self.dY < 0) or (self.dX > 0 and self.dy < 0):  # anticlockwise


                    pass
                else:   #clockwise
                    

                    pass



            if random.randint(0,100) < 50:      # 50% chance change shield state
                self.shielded = not self.shielded

        self.movementTimer +=1
        if self.movementTimer >= self.movementTimerReset:
            self.movementTimer = 0


        if self.shielded:
            super().setAnimationFrame(self.animationSetShielded[self.Colour],True)
        else:
            super().setAnimationFrame(self.animationSet[self.Colour],True)
