import pygame
import settings
import random

class ShieldCounter():
    def __init__(self, Game, X, Y, Value, FontName, FontSize, FontSizeIncrement = 15):
        FontName += ".ttf"

        self.fontName = FontName
        self.fontSize = FontSize
        self.fontSizeIncrement = FontSizeIncrement
        self.X = X
        self.Y = Y
        self.value = Value
        self.alpha = settings.Point.defaultAlpha
        self.alphaReduction = self.alpha / (settings.FRAMES_PER_SECOND)
        self.game = Game

    def draw(self):
        pgFont = pygame.font.Font(settings.Point.fontDir + self.fontName, self.fontSize)

        textSurface = pgFont.render(str(self.value), True, (255, 0, 0))
        textRect = textSurface.get_rect()
        textRect.centerx = self.X
        textRect.centery = self.Y

        self.game.screen.blit(textSurface, textRect)

    def update(self):
        self.alpha -= self.alphaReduction
        self.fontSize += self.fontSizeIncrement
        if self.alpha < 0:
            self.alpha = 0