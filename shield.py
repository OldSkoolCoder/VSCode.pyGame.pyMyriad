import pygame
import settings
import element
import shieldCounter

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
        self.shieldCountDown = 0
        self.shieldPhase = settings.Shield.phaseStart

        self.setAnimationFrame(self.animation[self.currentFrameNo],True)

    def update(self):
        if self.activated:
            self.invincibleTimer +=1
            if self.invincibleTimer >= settings.Player.shieldActiveTimeFPS:
                self.activated = False
                self.invincibleTimer = 0
                self.currentFrameNo = self.frameBlank
                self.game.Player.invincible = False
                self.game.removeShields()
                self.game.soundFx.stopSound('shield4')


            elif self.invincibleTimer >= settings.Player.shieldActiveTimeWarningFPS:
                if self.shieldPhase == 0:
                    self.game.soundFx.stopSound('shield2')
                    self.game.soundFx.playSoundContinuously('shield4')
                    self.shieldPhase = 1

                if int(self.invincibleTimer // 15) % 2:
                    self.currentFrameNo = self.frameBlank
                    if int(self.invincibleTimer // 2) % 30 and self.shieldPhase == settings.Shield.phaseBlank:
                        countDown = f'{self.shieldCountDown}'
                        textCountDown = shieldCounter.ShieldCounter(self.game, settings.Screen.WIDTH / 2, settings.Screen.HEIGHT / 2, countDown, 'Vinegar Stroke',50)
                        self.game.points.append(textCountDown)
                        self.shieldCountDown -= 1
                        self.shieldPhase = settings.Shield.phaseShow
                else:
                    self.currentFrameNo = self.frameShield
                    if int(self.invincibleTimer // 2) % 30 == 0 and self.shieldPhase == settings.Shield.phaseShow:
                        self.shieldPhase = settings.Shield.phaseBlank

        self.X = self.game.Player.X
        self.Y = self.game.Player.Y - 25

        self.setAnimationFrame(self.animation[self.currentFrameNo],True)

    def activateShield(self):
        if not self.activated:
            self.currentFrameNo = self.frameShield
            self.invincibleTimer = 0
            self.activated = True
            self.shieldCountDown = 3
            self.shieldPhase = settings.Shield.phaseStart
            self.game.soundFx.playSoundContinuously('shield2')

