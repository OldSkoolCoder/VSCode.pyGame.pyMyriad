import pygame
import settings
import element

class Shield(element.Element):

    def __init__(self,game,X,Y):

        self.frameShield = 0
        self.frameBlank = 1

        imgDir = 'Player/'
        super().__init__(game,X,Y-20,imgDir)

        image = self.loadAnimationFrame('Shield', 0,0,0.5)
        self.animation.append(image)

        image = self.loadAnimationFrame('Blank', 0)
        self.animation.append(image)

        self.invincibleCount = 0
        self.invincibleTimer = 0
        self.activated = False
        self.currentFrameNo = self.frameBlank

        self.setAnimationFrame(self.animation[self.currentFrameNo],True)

    def update(self):
        if self.activated:
            self.invincibleTimer +=1
            if self.invincibleTimer >= settings.Player.shieldActiveTimeFPS:
                self.activated = False
                self.invincibleTimer = 0
                self.currentFrameNo = self.frameBlank
                self.game.Player.invincible = False

            elif self.invincibleTimer >= settings.Player.shieldActiveTimeWarningFPS:
                if int(self.invincibleTimer // 15) % 2 == 0:
                    self.currentFrameNo = self.frameBlank
                else:
                    self.currentFrameNo = self.frameShield

        self.X = self.game.Player.X
        self.Y = self.game.Player.Y - 25

        self.setAnimationFrame(self.animation[self.currentFrameNo],True)

    def activateShield(self):
        if not self.activated:
            self.currentFrameNo = self.frameShield
            self.invincibleTimer = 0
            self.activated = True
