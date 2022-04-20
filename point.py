import pygame
import settings
import random

class Point():
    def __init__(self, Game, X, Y, Value, FontName):
        FontName += ".ttf"

        self.fontName = FontName
        self.fontSize = settings.Point.fontSize
        self.X = X
        self.Y = Y
        self.value = Value
        self.alpha = settings.Point.defaultAlpha
        self.game = Game

        self.game.totalPoints += Value


    def draw(self):
        pgFont = pygame.font.Font(settings.Point.fontDir + self.fontName, self.fontSize)

        textSurface = pgFont.render(str(self.value), True, (0, self.alpha, self.alpha))
        textRect = textSurface.get_rect()
        textRect.centerx = self.X
        textRect.centery = self.Y

        self.game.screen.blit(textSurface, textRect)

    def update(self):
        self.alpha -= settings.Point.alphaReduction
        self.fontSize +=1
        if self.alpha < 0:
            self.alpha = 0