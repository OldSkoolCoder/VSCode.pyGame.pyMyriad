import pygame
import settings

class Element (pygame.sprite.Sprite):
    def __init__(self,game,x,y,ImgDir):
        super().__init__()

        self.game = game

        self.X = x
        self.Y = y

        self.dX = 0             # -ve = Left, 0 = Stationary, +ve = Right
        self.dY = 0             # -ve = Up, 0 = Stationary, +ve = Down

        self.frameNo = 0
        self.tickCounter = 0
        self.noOfFrames = 0
        self.ticksPerFrame = 0

        self.imageDir = ImgDir
        self.image = None 
        self.rect = None

        self.alive = True

        self.animation = []

    def loadAnimationFrame(self, imageName, frameNo, angle=0,zoom=1):
        frameNumber = format(str(frameNo).rjust(3,'0'))
        # 'Assets/Asteroids/seta001.png'
        filename = f'Assets/{self.imageDir}/{imageName}{frameNumber}.png'
        imageFrame = pygame.image.load(filename)#.convert()

        if angle !=0 or zoom != 1:
            imageFrame = pygame.transform.rotozoom(imageFrame,angle,zoom)
        return imageFrame

    def loadAnimationSeries(self, imageName, NoOfFrames):
        for frameNo in range(NoOfFrames):    # NoOfFrames = 10 = 0 -> 9
            self.animation.append(self.loadAnimationFrame(imageName,frameNo))

    def move(self, dX, dY, speed, TestForBorder = True):
        for i in range(speed):
            if TestForBorder:
                if self.allowedToMove(self.X + dX, self.Y + dY):
                    self.X += dX
                    self.Y += dY
            else:
                self.X += dX
                self.Y += dY

    def setAnimationFrame(self,frameImage,useCentre):
        self.image = frameImage
        self.rect = self.image.get_rect()

        if useCentre:
            self.rect.centerx = self.X
            self.rect.centery = self.Y
    
    def allowedToMove(self,X,Y):
        width = self.rect.width/2
        height = self.rect.height/2

        if ((X - width) < settings.PlayableArea.LeftMost) or \
            ((X + width) > settings.PlayableArea.RightMost) or \
                ((Y - height) < settings.PlayableArea.Top) or \
                    ((Y + height) > settings.PlayableArea.Bottom):
            return False
        else:
            return True

