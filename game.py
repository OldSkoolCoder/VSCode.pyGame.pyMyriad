import pygame
import random
import settings
#import sprites
import player
import bullet
import floaters
import boxes
import explosion

class Game:
    def __init__(self):
        # Initialise game code
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.Screen.WIDTH, settings.Screen.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.fireMode = settings.Player.singleShot
        #self.fireMode = settings.Player.rapidFire
        self.showHitBoxes = False
        self.bgY = 0
        self.bgRelY = 0


        self.explosionSets = {}
        self.explosionSets['Set1'] = []
        self.loadAnimationSeries('Explosion/Set1', 'Exp-',62,self.explosionSets['Set1'],0,2)

        self.explosionSets['Set2'] = []
        self.loadAnimationSeries('Explosion/Set2', 'Exp-',62,self.explosionSets['Set2'],0,2)
        self.explosionSets['Set3'] = []
        self.loadAnimationSeries('Explosion/Set3', 'Exp-',62,self.explosionSets['Set3'],0,2)

        self.bullets = pygame.sprite.Group()
        self.hostiles = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.points = []


    def new(self):
        self.level = 1
        self.wave = 5
        self.powerUp = 0

        # Starts a new game
        self.allSprites = pygame.sprite.Group()

        self.bullets.empty()
        self.hostiles.empty()

        # Add Player Sprites
        self.Player = player.Player(self) 
        self.allSprites.add(self.Player)

        # Add Enemy Sprites
        for i in range(self.level * 5):
            self.hostiles.add(boxes.Box(self, i, self.wave))

        self.newLevel()
        self.run()

    def newLevel(self):
        backgroundFrameNo = format(str(self.level).rjust(2,'0')) 
        self.background = pygame.image.load(f'Assets/BackDrops/Background{backgroundFrameNo}.jpg')

    def run(self):
        # Game Loop Code
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FRAMES_PER_SECOND)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop Update Method
        self.allSprites.update()
        self.bullets.update()
        self.Player.update()
        self.hostiles.update()
        self.explosions.update()

        self.bulletHitHostiles()
        self.removeDoneBullets()
        self.removeDeadHostiles()
        self.removeExplosions()

    def events(self):
        self.Player.events()

        # Game Loop Events handler
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop draw screen
        # self.screen.fill(settings.Colours.BLACK)
        self.bgRelY = self.bgY % self.background.get_rect().height

        # Draw Section
        self.screen.blit(self.background, (0,(self.bgRelY - self.background.get_rect().height)))
        if self.bgRelY < settings.Screen.HEIGHT:
            self.screen.blit(self.background, (0,self.bgRelY))
        self.bgY +=1

        self.allSprites.draw(self.screen)
        self.bullets.draw(self.screen)
        self.hostiles.draw(self.screen)
        self.explosions.draw(self.screen)

        # After redrawing the screen, flip it
        pygame.display.flip()

    def showStartScreen(self):
        # Show the start screen of the game
        pass

    def showGameOverScreen(self):
        # show the Game over screen
        pass

    def removeDoneBullets(self):
        for eachBullet in self.bullets:
            if eachBullet.done:
                self.bullets.remove(eachBullet)

    def bulletHitHostiles(self):
        for eachBullet in self.bullets:
            hostilesHits = pygame.sprite.spritecollide(eachBullet, self.hostiles, False)
            if hostilesHits:
                for eachHostile in hostilesHits:
                    if not eachHostile.reflective:
                        #Add Explosion to Sprite Array
                        self.explosions.add(explosion.Explosion(self, eachHostile.X, eachHostile.Y,self.explosionSets))
                        eachHostile.imDead = True
                
                eachBullet.done = True
                
    def removeDeadHostiles(self):
        for eachHostile in self.hostiles:
            if eachHostile.imDead:
                self.hostiles.remove(eachHostile)

    def removeExplosions(self):
        for eachExplosion in self.explosions:
            if eachExplosion.imDone:
                self.explosions.remove(eachExplosion)

    def loadAnimationFrame(self, imageDir, imageName, frameNo, angle=0,zoom=1):
        frameNumber = format(str(frameNo).rjust(3,'0'))
        # 'Assets/Asteroids/seta001.png'
        filename = f'Assets/{imageDir}/{imageName}{frameNumber}.png'
        imageFrame = pygame.image.load(filename)#.convert()

        if angle !=0 or zoom != 1:
            imageFrame = pygame.transform.rotozoom(imageFrame,angle,zoom)
        return imageFrame

    def loadAnimationSeries(self, imageDir, imageName, NoOfFrames, animationSet, angle=0,zoom=1):
        for frameNo in range(NoOfFrames):    # NoOfFrames = 10 = 0 -> 9
            animationSet.append(self.loadAnimationFrame(imageDir,imageName,frameNo,angle,zoom))
