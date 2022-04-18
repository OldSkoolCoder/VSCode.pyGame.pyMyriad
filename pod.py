import pygame
import settings
import element
import hostile
import mine
import brick
import builder
import bomber
import virus
import plasmaBall
import random

class Pod(hostile.Hostile):

    def __init__(self,game,HostileNo,Wave):
        super().__init__(game,HostileNo,Wave, 0.4)
        self.animationSet = self.animation.copy()
        
        self.animation.clear()
        super().loadAnimationSeries('Alien18-',self.noOfFrames,0,0.4)
        self.animationSetShielded = self.animation.copy()
        self.animation.clear()

        self.myValue = 1000
        self.reflective = False

        self.speed = 2
        self.movementTimerReset = settings.FRAMES_PER_SECOND
        self.movementTimer = 1
        self.speedDivisor = 2

        self.X = random.randint((settings.PlayableArea.LeftMost + (self.rect.width + 10)), (settings.PlayableArea.RightMost - (self.rect.width + 10)))
        self.determineDiagonalStartDirection()
        self.dX = self.dX / self.speedDivisor
        self.dY = self.dY / self.speedDivisor

    def update(self):
        self.wrapBottomToTop()   
        self.wrapLeftAndRight()         
        #self.move(self.dX,0,self.speed)
        #self.X += self.dX

        if self.movementTimer == 0:
            self.dX = self.dX * self.speedDivisor
            self.dY = self.dY * self.speedDivisor
            self.determineRandomChangeOfDirection()
            self.dX = self.dX / self.speedDivisor
            self.dY = self.dY / self.speedDivisor

            if self.twentyTwoPercentChance():
                self.game.ordinance.add(plasmaBall.PlasmaBall(self, self.X, self.Y))  # 7 since we dont know our own wave(doesnt really matter)  bullet type 3 (F)

            if self.twentyTwoPercentChance():
                randNo = random.random()
                if randNo > .83:
                    # Brick
                    self.game.ordinance.add(brick.Brick(self.game, self.X, self.Y))
                    pass
                elif randNo > .66:
                    # Mine
                    self.game.ordinance.add(mine.Mine(self.game, self.X, self.Y))
                elif randNo > .49:
                    # Reflector
                    pass
                elif randNo > .33:
                    # Bomber
                    self.game.hostiles.add(bomber.Bomber(self.game, self.X, self.Y))
                    pass
                elif randNo > .16:
                    # Builder
                    self.game.ordinance.add(builder.Builder(self.game, self.X, self.Y))
                    pass
                else:
                    # Virus
                    self.game.hostiles.add(virus.Virus(self.game, self.X, self.Y))
                    pass

        self.updateMovementTimer()

        if int(self.movementTimer /8) % 2 == 1:
            super().setAnimationFrame(self.animationSetShielded[self.Colour],True)
        else:
            super().setAnimationFrame(self.animationSet[self.Colour],True)
