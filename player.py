import pygame
import settings
import element
import bullet

class Player(element.Element):
    def __init__(self,game):

        imgDir = 'Player/SpaceShip/'
        super().__init__(game,settings.Player.respawnX,settings.Player.respawnY,imgDir)

        self.noOfFrames = 4
        self.shieldTimer = 0
        self.fireTimer = 0
        self.thrustActive = False
        self.speed = 5
        self.timer = 0
        self.rotateLeft = False
        self.haveWeFired = False
        self.held = 1       # Variable to hold reloading delay extender (Garymeg)
        self.bulletSide = 1 # Variable to hold side ship fires from (Garymeg)

        super().loadAnimationSeries('ShipFlames',self.noOfFrames * 2)
        self.thrustedAnimationSet = self.animation.copy()

        self.animation.clear()
        super().loadAnimationSeries('Ship',self.noOfFrames * 2)
        self.animationSet = self.animation.copy()

        self.animation.clear()
        super().setAnimationFrame(self.animationSet[0],True)

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / self.noOfFrames

    def events(self):
        keys = pygame.key.get_pressed()

        #changed so if left and right both pressed you go nowhere. 
        self.dX = 0 
        if keys[pygame.K_LEFT]:
            self.dX -= 1
            self.rotateLeft = True
        if keys[pygame.K_RIGHT]:
            self.dX += 1
            self.rotateLeft = False

        self.dY =  1
        if keys[pygame.K_UP]:
            self.thrustActive = True
            self.dY = -1
        else:
            self.thrustActive = False

        if keys[pygame.K_1]:
            self.game.powerUp = 0


        if keys[pygame.K_2]:
            self.game.powerUp = 1

        if keys[pygame.K_3]:
            self.game.powerUp = 2

        self.fireTimer -=1

        if self.fireTimer < 0 and keys[pygame.K_SPACE]:
            self.shootLaser()
                    
        if self.game.fireMode == settings.Player.rapidFire:
            # is fire released?    (Garymeg)
            if not keys[pygame.K_SPACE]:
                self.held = 1                                           # reset autofire (Garymeg)
        else:
            if not(keys[pygame.K_SPACE]) and self.haveWeFired:
                self.haveWeFired = False

    def update(self):
        super().move(self.dX,0,self.speed-abs(self.dX))
        super().move(0,self.dY,self.speed-abs(self.dY))

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        if self.rotateLeft == True:
            frameNo = 3 - frameNo
        if self.haveWeFired:
            frameNo += 4

        #if (int(self.tickCounter // self.ticksPerFrame) == self.tickCounter / self.ticksPerFrame):
        if self.thrustActive:
            super().setAnimationFrame(self.thrustedAnimationSet[frameNo],True)
        else:
            super().setAnimationFrame(self.animationSet[frameNo],True)

    def shootLaser(self):
        if self.game.fireMode == settings.Player.rapidFire:
            if self.bulletSide % 2:
                self.game.bullets.add(bullet.Bullet(self.game, self.X-12, (self.Y - self.rect.height/2),self.game.wave))
                self.bulletSide = 2
            else:
                self.game.bullets.add(bullet.Bullet(self.game, self.X+12, (self.Y - self.rect.height/2),self.game.wave))
                self.bulletSide = 1

            self.fireTimer = settings.Player.reloadTime * self.held # self.held is a time multiplyer to slow rapidfire down (Garymeg)
            self.held += 0.05                                        # keep slowing down rapidfire (Garymeg)

        else:
            if not(self.haveWeFired):
                self.game.bullets.add(bullet.Bullet(self.game, self.X-12, (self.Y - self.rect.height/2),self.game.wave))
                self.game.bullets.add(bullet.Bullet(self.game, self.X+12, (self.Y - self.rect.height/2),self.game.wave))
                self.haveWeFired = True
                self.fireTimer = settings.Player.reloadTime

        #self.game.bullets.add(bullet.Bullet(self.game, self.X-12, (self.Y - self.rect.height/2),self.game.wave))
        #self.game.bullets.add(bullet.Bullet(self.game, self.X+12, (self.Y - self.rect.height/2),self.game.wave))
        #self.haveWeFired = True
