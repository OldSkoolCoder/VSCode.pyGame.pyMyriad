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

        super().loadAnimationSeries('ShipFlames',self.noOfFrames)
        self.thrustedAnimationSet = self.animation.copy()

        self.animation.clear()
        super().loadAnimationSeries('Ship',self.noOfFrames)
        self.animationSet = self.animation.copy()

        self.animation.clear()
        super().setAnimationFrame(self.animationSet[0],True)

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / self.noOfFrames
        self.HaveWeFired = False

    def events(self):
        keys = pygame.key.get_pressed()

        self.dx = 0
        if keys[pygame.K_LEFT]:
            self.dx = -1
        elif keys[pygame.K_RIGHT]:
            self.dx = 1

        self.dy = 1
        if keys[pygame.K_UP]:
            self.thrustActive = True
            self.dy = -1
        else:
            self.thrustActive = False

        self.fireTimer -=1

        if self.fireTimer < 0 and (self.timer > 0 or keys[pygame.K_SPACE]):
            if self.timer == 0:
                self.game.bullets.add(bullet.Bullet(self.game, self.X-12, (self.Y - self.rect.height/2),self.game.wave))
                self.game.bullets.add(bullet.Bullet(self.game, self.X+12, (self.Y - self.rect.height/2),self.game.wave))

            self.timer = (self.timer + 1) % 3
            self.fireTimer = settings.Player.reloadTime

    def update(self):
        super().move(self.dx,0,self.speed-abs(self.dx))
        super().move(0,self.dy,self.speed-abs(self.dy))

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)

        #if (int(self.tickCounter // self.ticksPerFrame) == self.tickCounter / self.ticksPerFrame):
        if self.thrustActive:
            super().setAnimationFrame(self.thrustedAnimationSet[frameNo],True)
        else:
            super().setAnimationFrame(self.animationSet[frameNo],True)
