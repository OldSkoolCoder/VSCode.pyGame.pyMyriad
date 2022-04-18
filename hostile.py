import pygame
import settings
import element
import player
import random

class Hostile(element.Element):

    def __init__(self,game,HostileNo,Wave,Scale=0.5):
        sWave = format(str(Wave).rjust(2,'0'))
        imgDir = f'Aliens/SpaceShips/Wave{sWave}'
        super().__init__(game, 0, 0, imgDir)

        self.noOfFrames = 8
        #super().loadAnimationSeries(f'Alien{sWave}-',self.noOfFrames,0,Scale)
        self.animation = self.game.assets.animationsSets['Alien'][f'Wave{sWave}'].copy()

        self.Colour = random.randint(0,7)
        super().setAnimationFrame(self.animation[self.Colour],True)

        self.determineInitalPosition(HostileNo)

        self.imDead = False
        self.myValue = 100

        self.movementTimerReset = settings.FRAMES_PER_SECOND / 4
        self.movementTimer = 0
        self.dX = 1
        self.speed = 5

        self.prevdY = 0
        self.prevdX = 0

        self.reflective = False

    def determineInitalPosition(self, HostileNo):
        rowNo = self.determineRowPosition(HostileNo)
        colNo = int(HostileNo % settings.Hostile.maxHostilesPerRow)
        hostileWidth = self.rect.width * 1.5
        hostileHeight = self.rect.height * 1.2

        self.X = (hostileWidth / 2) + 5 + (colNo * hostileWidth)
        self.Y = (hostileHeight / 2) + 5 + (rowNo * hostileHeight)

    def determineRowPosition(self, HostileNo):
        return int(HostileNo // settings.Hostile.maxHostilesPerRow)

    def zigzagMovement(self, movementTimer):
        if not self.move(self.dX,0,self.speed):
            self.dY = 1
            self.prevdX = self.dX
            self.dX = 0
            self.movementTimer = 1

        if movementTimer == 0:
            if self.dY == 1:
                self.dY = 0
                if self.prevdX == 1:
                    self.dX = -1
                else:
                    self.dX = 1

    def updateMovementTimer(self):
        self.movementTimer +=1
        if self.movementTimer >= self.movementTimerReset:
            self.movementTimer = 0

    def determineAntiClockWiseChangeOfDirection(self):
        if self.dX == -1:
            if self.dY == -1:
                self.dY = 0
            elif self.dY == 0:
                self.dY = 1
            else:
                self.dX = 0
        elif self.dX == 0:
            if self.dY == 1:
                self.dX = 1
            else:
                self.dX = -1
        else:
            # dX = 1
            if self.dY == -1:
                self.dX = 0
            elif self.dY == 0:
                self.dY = -1
            else:
                self.dY = 0

    def determineClockWiseChangeOfDirection(self):
        if self.dX == -1:
            if self.dY == -1:
                self.dX = 0
            elif self.dY == 0:
                self.dY = -1
            else:
                self.dY = 0
        elif self.dX == 0:
            if self.dY == 1:
                self.dX = -1
            else:
                self.dX = 1
        else:
            # dX = 1
            if self.dY == -1:
                self.dY = 0
            elif self.dY == 0:
                self.dY = 1
            else:
                self.dX = 0

    def determineChangeOfDirection(self):
        if self.dY == 1:
            if self.dX == 1:
                self.determineClockWiseChangeOfDirection()
                self.determineClockWiseChangeOfDirection()
            else:
                self.determineAntiClockWiseChangeOfDirection()
                self.determineAntiClockWiseChangeOfDirection()
        elif self.dX == 1:
            self.determineAntiClockWiseChangeOfDirection()
            self.determineAntiClockWiseChangeOfDirection()
        else:
            self.determineClockWiseChangeOfDirection()
            self.determineClockWiseChangeOfDirection()

    def determineRandomChangeOfDirection(self):
        randNo = random.random()

        if self.fiftyPercentChance():
            self.determineClockWiseChangeOfDirection()
        else:
            self.determineAntiClockWiseChangeOfDirection()

    def determineDiagonalStartDirection(self):
        self.dX = 0
        while self.dX == 0:
            self.dX = self.determineRandomDirection()
        self.dY = 1

    def determineStartXDirection(self):
        dX = 0
        while dX == 0:
            dX = self.determineRandomDirection()
        return dX

    def targetPlayerAI(self, Player):
        if self.X > Player.X:
            self.dX = -1
        else:
            self.dX = 1

    def checkToAddFlyingRocks(self, Hostiles):
        if self.fourPercentChance():
            # Add Asteroid
            pass
        else:
            if self.fourPercentChance():
                # Add Meteorite
                pass

    def fourPercentChance(self):
        if random.random() < 0.04:
            return True
        else:
            return False

    def fiftyPercentChance(self):
        if random.random() < 0.5:
            return True
        else:
            return False

    def fortyPercentChance(self):
        if random.random() < 0.4:
            return True
        else:
            return False

    def twentyTwoPercentChance(self):
        if random.random() < 0.22:
            return True
        else:
            return False
