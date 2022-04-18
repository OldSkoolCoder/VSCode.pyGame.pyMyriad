import pygame
import settings
import element

class ShieldIndicator(element.Element):

    def __init__(self,game,X,Y):

        self.frameShield = 0
        self.frameBlank = 1

        imgDir = 'Player/'
        super().__init__(game,X,Y-20,imgDir)

        image = self.loadAnimationFrame('Shield', 1,0,0.25)
        self.animation.append(image)

        self.currentFrameNo = self.frameShield

        self.setAnimationFrame(self.animation[self.currentFrameNo],True)

    def update(self):
        self.setAnimationFrame(self.animation[self.currentFrameNo],True)


