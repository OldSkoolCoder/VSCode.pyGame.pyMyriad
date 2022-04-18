import pygame

class Assets():
    def __init__(self):
        self.animationsSets = {}

        self.animationsSets['Explosion'] = {}
        self.animationsSets['Explosion']['Set1'] = self.loadAnimationSeries('Explosion/Set1', 'Exp-',62,0,2)
        self.animationsSets['Explosion']['Set2'] = self.loadAnimationSeries('Explosion/Set2', 'Exp-',62,0,2)
        self.animationsSets['Explosion']['Set3'] = self.loadAnimationSeries('Explosion/Set3', 'Exp-',62,0,2)

        self.animationsSets['Asteroid'] = {}
        self.animationsSets['Asteroid']['SetA'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidA-',16,0,.5)
        self.animationsSets['Asteroid']['SetB'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidB-',16,0,.5)
        self.animationsSets['Asteroid']['SetC'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidC-',16,0,.5)
        self.animationsSets['Asteroid']['SetD'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidD-',16,0,.5)
        self.animationsSets['Asteroid']['SetE'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidE-',16,0,.5)
        self.animationsSets['Asteroid']['SetF'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidF-',16,0,.5)
        self.animationsSets['Asteroid']['SetG'] = self.loadAnimationSeries('Asteroids/Large', 'AsteroidG-',16,0,.5)

        self.animationsSets['Meteorite'] = {}
        self.animationsSets['Meteorite']['SetA'] = self.loadAnimationSeries('Asteroids/Small', 'MeteoriteA-',16)
        self.animationsSets['Meteorite']['SetB'] = self.loadAnimationSeries('Asteroids/Small', 'MeteoriteB-',16)
        self.animationsSets['Meteorite']['SetC'] = self.loadAnimationSeries('Asteroids/Small', 'MeteoriteC-',16)
        self.animationsSets['Meteorite']['SetD'] = self.loadAnimationSeries('Asteroids/Small', 'MeteoriteD-',16)
        self.animationsSets['Meteorite']['SetE'] = self.loadAnimationSeries('Asteroids/Small', 'MeteoriteE-',16)
        self.animationsSets['Meteorite']['SetF'] = self.loadAnimationSeries('Asteroids/Small', 'MeteoriteF-',16)

        self.animationsSets['Alien'] = {}
        self.animationsSets['Alien']['Wave01'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave01', 'Alien01-',8,0,.3)
        self.animationsSets['Alien']['Wave02'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave02', 'Alien02-',8,0,.3)
        self.animationsSets['Alien']['Wave03'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave03', 'Alien03-',8,0,.3)
        #self.animationsSets['Alien']['Wave04'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave04', 'Alien04-',8,0,.4)
        self.animationsSets['Alien']['Wave05'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave05', 'Alien05-',8,0,.4)
        self.animationsSets['Alien']['Wave05b'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave05', 'Alien15-',8,0,.4)
        self.animationsSets['Alien']['Wave06'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave06', 'Alien06-',8,0,.4)
        self.animationsSets['Alien']['Wave07'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave07', 'Alien07-',8,0,.3)
        self.animationsSets['Alien']['Wave08'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave08', 'Alien08-',8,0,.4)
        self.animationsSets['Alien']['Wave08b'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave08', 'Alien18-',8,0,.4)
        #self.animationsSets['Alien']['Wave09'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave09', 'Alien09-',8)
        self.animationsSets['Alien']['Wave10'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave10', 'Alien10-',8,0,.2)
        self.animationsSets['Alien']['Wave11'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave11', 'Alien11-',8,0,.3)
        #self.animationsSets['Alien']['Wave12'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave12', 'Alien12-',8)
        #self.animationsSets['Alien']['Wave13'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave13', 'Alien13-',8)
        self.animationsSets['Alien']['Wave14'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave14', 'Alien14-',8,0,.2)
        self.animationsSets['Alien']['Wave15'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave05', 'Alien15-',8,0,.3)
        #self.animationsSets['Alien']['Wave18'] = self.loadAnimationSeries('Aliens/SpaceShips/Wave8', 'Alien18-',8,0,.4)

    def loadAnimationFrame(self, imgDir, imageName, frameNo, angle=0,zoom=1):
        frameNumber = format(str(frameNo).rjust(3,'0'))
        # 'Assets/Asteroids/seta001.png'
        filename = f'Assets/{imgDir}/{imageName}{frameNumber}.png'
        imageFrame = pygame.image.load(filename)#.convert()

        if angle !=0 or zoom != 1:
            imageFrame = pygame.transform.rotozoom(imageFrame,angle,zoom)
        return imageFrame

    def loadAnimationSeries(self, imgDir, imageName, NoOfFrames,angle=0,zoom=1):
        animation = []
        for frameNo in range(NoOfFrames):    # NoOfFrames = 10 = 0 -> 9
            animation.append(self.loadAnimationFrame(imgDir, imageName,frameNo,angle,zoom))

        return animation