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

        super().loadAnimationSeries('ShipFlames',self.noOfFrames * 2)
        self.thrustedAnimationSet = self.animation.copy()

        self.animation.clear()
        super().loadAnimationSeries('Ship',self.noOfFrames * 2)
        self.animationSet = self.animation.copy()

        self.animation.clear()
        super().setAnimationFrame(self.animationSet[0],True)

        self.ticksPerFrame = settings.FRAMES_PER_SECOND / self.noOfFrames
        self.HaveWeFired = False

    def events(self):
        keys = pygame.key.get_pressed()

        #changed so if left and right both pressed you go nowhere. 
        self.dx = 0 
        if keys[pygame.K_LEFT]:
            self.dx -= 1
            self.rotateLeft = True
        if keys[pygame.K_RIGHT]:
            self.dx += 1
            self.rotateLeft = False

        self.dy =  1
        if keys[pygame.K_UP]:
            self.thrustActive = True
            self.dy = -1
        else:
            self.thrustActive = False

        if keys[pygame.K_1]:
            self.game.powerUp = 0


        if keys[pygame.K_2]:
            self.game.powerUp = 1

        if keys[pygame.K_3]:
            self.game.powerUp = 2



        self.fireTimer -=1

        if self.fireTimer < 0 and keys[pygame.K_SPACE] and not(self.HaveWeFired): 

               if self.bulletSide % 2:
                    self.game.bullets.add(bullet.Bullet(self.game, self.X-12, (self.Y - self.rect.height/2),self.game.wave))
                    self.bulletSide = 2
                else:
                    self.game.bullets.add(bullet.Bullet(self.game, self.X+12, (self.Y - self.rect.height/2),self.game.wave))
                    self.bulletSide = 1
                    
            self.timer = (self.timer + 1) % 3
            self.fireTimer = settings.Player.reloadTime * self.held # self.held is a time multiplyer to slow rapidfire down (Garymeg)
            self.held += 0.05                                        # keep slowing down rapidfire (Garymeg)
            
        # is fire released?    (Garymeg)
        if not keys[pygame.K_SPACE]:
            self.held = 1                                           # reset autofire (Garymeg)

          self.game.bullets.add(bullet.Bullet(self.game, self.X-12, (self.Y - self.rect.height/2),self.game.wave))
                self.game.bullets.add(bullet.Bullet(self.game, self.X+12, (self.Y - self.rect.height/2),self.game.wave))
                self.HaveWeFired = True
                self.fireTimer = settings.Player.reloadTime
   
        if not(keys[pygame.K_SPACE]) and self.HaveWeFired:
            self.HaveWeFired = False

    def update(self):
        super().move(self.dx,0,self.speed-abs(self.dx))
        super().move(0,self.dy,self.speed-abs(self.dy))

        self.tickCounter += 1
        if self.tickCounter >= settings.FRAMES_PER_SECOND:
            self.tickCounter = 0

        frameNo = int(self.tickCounter // self.ticksPerFrame)
        if self.rotateLeft == True:
            frameNo = 3 - frameNo
        if self.HaveWeFired:
            frameNo += 4

        #if (int(self.tickCounter // self.ticksPerFrame) == self.tickCounter / self.ticksPerFrame):
        if self.thrustActive:
            super().setAnimationFrame(self.thrustedAnimationSet[frameNo],True)
        else:
            super().setAnimationFrame(self.animationSet[frameNo],True)
