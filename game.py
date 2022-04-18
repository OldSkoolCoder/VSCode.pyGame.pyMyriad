import pygame
import random
import settings
#import sprites
import player
import bullet
import floaters
import boxes
import explosion
import point
import reflectedBullet
import buzzers
import meteorite
import asteroid
import swoopers
import fighters
import text
import miner
import pod

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
        self.showHitBoxes = False

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
        self.ordinance = pygame.sprite.Group()
        self.points = []

    def new(self):
        self.level = 1
        self.wave = 0
        self.powerUp = 0

        # Starts a new game
        self.allSprites = pygame.sprite.Group()

        self.bullets.empty()
        self.hostiles.empty()
        self.ordinance.empty()

        # Add Player Sprites
        self.Player = player.Player(self) 
        self.allSprites.add(self.Player)

        # Add Enemy Sprites

        self.run()

    def newLevel(self):
        backgroundFrameNo = format(str(self.level).rjust(2,'0')) 
        self.background = pygame.image.load(f'Assets/BackDrops/scrollable/Background{backgroundFrameNo}.jpg')

    def run(self):
        # Game Loop Code
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FRAMES_PER_SECOND)
            if len(self.hostiles) + len(self.ordinance) <= self.level + 1:
                self.addNextWaveLevelOfAliens()
                self.newLevel()

            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop Update Method
        self.allSprites.update()
        self.bullets.update()
        self.Player.update()
        self.hostiles.update()
        self.ordinance.update()
        self.explosions.update()

        self.bulletHitHostiles()

        if self.Player.invincible:
            self.shieldHitHostiles()
        else:
            if self.Player.alive:
                self.shipHitHostiles()

        if not self.Player.alive:
            if not self.Player.shipExplosion.imDone:
                self.Player.shipExplosion.update()
            else:
                self.allSprites.remove(self.Player.shipExplosion)
                self.Player.iAmAlive()
                #self.playing = False


        for eachPoint in self.points:
            eachPoint.update()
            if eachPoint.alpha == 0:
                self.points.remove(eachPoint)

        self.removeDoneBullets()
        self.removeDeadHostiles()
        self.removeExplosions()
        self.removeDeadOrdinance()

    def events(self):
        self.Player.events()

        # Game Loop Events handler
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    self.showHitBoxes = not self.showHitBoxes

    def draw(self):
        # Game Loop draw screen
        # self.screen.fill(settings.Colours.BLACK)
        self.bgRelY = self.bgY % self.background.get_rect().height

        # Draw Section
        self.screen.blit(self.background, (0,(self.bgRelY - self.background.get_rect().height)))
        if self.bgRelY < settings.Screen.HEIGHT:
            self.screen.blit(self.background, (0,self.bgRelY))
        self.bgY +=0.5

        self.allSprites.draw(self.screen)
        self.bullets.draw(self.screen)
        self.hostiles.draw(self.screen)
        self.ordinance.draw(self.screen)
        self.explosions.draw(self.screen)

        for eachPoint in self.points:
            eachPoint.draw()

        if self.showHitBoxes:
            for sprite in self.hostiles:
                pygame.draw.rect(self.screen, settings.Colours.RED, sprite.rect,1)
                pygame.draw.circle(self.screen, settings.Colours.RED, sprite.rect.center, sprite.radius,1)

            for ordinance in self.ordinance:
                pygame.draw.rect(self.screen, settings.Colours.RED, ordinance.rect,1)
                #pygame.draw.circle(self.screen, settings.Colours.RED, ordinance.rect.center, ordinance.radius,1)

            for bullet in self.bullets:
                pygame.draw.rect(self.screen, settings.Colours.BLUE, bullet.rect,1)
                #pygame.draw.circle(self.screen, settings.Colours.RED, bullet.rect.center, bullet.radius,1)

            pygame.draw.rect(self.screen, settings.Colours.BLUE, self.Player.rect,1)
            pygame.draw.rect(self.screen, settings.Colours.BLUE, (self.Player.rect.center,(4,4)),0)
            pygame.draw.circle(self.screen, settings.Colours.BLUE, self.Player.rect.center, self.Player.radius,1)

            pygame.draw.rect(self.screen, settings.Colours.BLUE, self.Player.shieldSprite.rect,1)
            pygame.draw.rect(self.screen, settings.Colours.BLUE, (self.Player.shieldSprite.rect.center,(4,4)),0)
            pygame.draw.circle(self.screen, settings.Colours.BLUE, self.Player.shieldSprite.rect.center, self.Player.radius,1)

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
            ordinanceHits = pygame.sprite.spritecollide(eachBullet, self.ordinance, False) # Regular Square Hit Box
            #ordinanceHits = pygame.sprite.spritecollide(eachBullet, self.ordinance, False, pygame.sprite.collide_circle) # Using Circle Hit Box
            if ordinanceHits:
                for eachOrdinance in ordinanceHits:
                    eachOrdinance.hitValue -= 1
                    if eachOrdinance.hitValue == 0:
                        self.explosions.add(explosion.Explosion(self, eachOrdinance.X, eachOrdinance.Y,self.explosionSets,0))
                        eachOrdinance.imDead = True
                        #self.points.append(point.Point(self, eachHostile.X, eachHostile.Y, eachHostile.myValue, 'Vinegar Stroke'))
                
                eachBullet.done = True

            #hostilesHits = pygame.sprite.spritecollide(eachBullet, self.hostiles, False) # Regular Square Hit Box
            hostilesHits = pygame.sprite.spritecollide(eachBullet, self.hostiles, False, pygame.sprite.collide_circle) # Using Circle Hit Box
            if hostilesHits:
                for eachHostile in hostilesHits:
                    if not eachHostile.reflective:
                        #Add Explosion to Sprite Array
                        self.explosions.add(explosion.Explosion(self, eachHostile.X, eachHostile.Y,self.explosionSets))
                        eachHostile.imDead = True
                        self.points.append(point.Point(self, eachHostile.X, eachHostile.Y, eachHostile.myValue, 'Vinegar Stroke'))
                        self.hostiles.remove(eachHostile)
                    else:
                        self.ordinance.add(reflectedBullet.ReflectedBullet(self, eachBullet.X, eachBullet.Y, self.wave, self.powerUp))
                
                eachBullet.done = True


    def removeDeadHostiles(self):
        for eachHostile in self.hostiles:
            if eachHostile.imDead:
                self.hostiles.remove(eachHostile)

    def removeExplosions(self):
        for eachExplosion in self.explosions:
            if eachExplosion.imDone:
                self.explosions.remove(eachExplosion)

    def removeDeadOrdinance(self):
        for eachOrdinance in self.ordinance:
            if eachOrdinance.imDead:
                self.ordinance.remove(eachOrdinance)

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

    def addNextWaveLevelOfAliens(self):
        self.wave +=1
        if self.wave > 9:
            self.level +=1
            self.wave = 1

        WaveTitle = f'Get Ready - Entering Wave {self.wave}'
        textWaveTitle = text.Text(self, settings.Screen.WIDTH / 2, settings.Screen.HEIGHT / 2, WaveTitle, 'Vinegar Stroke',50)
        self.points.append(textWaveTitle)

        for i in range(self.level * settings.Hostile.noPerLevel):
            if self.wave == 1:
                self.hostiles.add(floaters.Floater(self, i, self.wave))
            elif self.wave == 2:
                self.hostiles.add(swoopers.Swooper(self, i, self.wave))
            elif self.wave == 3:
                self.hostiles.add(buzzers.Buzzers(self, i, self.wave))
            elif self.wave == 4:
                self.hostiles.add(meteorite.Meteorite(self))
            elif self.wave == 5:
                self.hostiles.add(boxes.Box(self, i, self.wave))
            elif self.wave == 6:
                self.hostiles.add(miner.Miner(self, i, self.wave))
            elif self.wave == 7:
                self.hostiles.add(fighters.Fighter(self, i, self.wave))
            elif self.wave == 8:
                if i < self.level:
                    self.hostiles.add(pod.Pod(self, i, self.wave))
                    self.hostiles.add(pod.Pod(self, i, self.wave))
            elif self.wave == 9:
                self.hostiles.add(asteroid.Asteroid(self))

            if (self.wave != 4 or self.wave != 9):
                if random.random() < .04:
                    self.hostiles.add(meteorite.Meteorite(self))
                else:
                    if random.random() < .04:
                        self.hostiles.add(asteroid.Asteroid(self))

    def shieldHitHostiles(self):
        ordinanceHits = pygame.sprite.spritecollide(self.Player.shieldSprite, self.ordinance, False) # Regular Square Hit Box
        #ordinanceHits = pygame.sprite.spritecollide(eachBullet, self.ordinance, False, pygame.sprite.collide_circle) # Using Circle Hit Box
        if ordinanceHits:
            for eachOrdinance in ordinanceHits:
                self.explosions.add(explosion.Explosion(self, eachOrdinance.X, eachOrdinance.Y,self.explosionSets,0))
                eachOrdinance.imDead = True
                #self.points.append(point.Point(self, eachHostile.X, eachHostile.Y, eachHostile.myValue, 'Vinegar Stroke'))

        hostilesHits = pygame.sprite.spritecollide(self.Player.shieldSprite, self.hostiles, False, pygame.sprite.collide_circle) # Using Circle Hit Box
        if hostilesHits:
            for eachHostile in hostilesHits:
                self.explosions.add(explosion.Explosion(self, eachHostile.X, eachHostile.Y,self.explosionSets))
                eachHostile.imDead = True
                self.points.append(point.Point(self, eachHostile.X, eachHostile.Y, eachHostile.myValue, 'Vinegar Stroke'))

        self.shipHitHostiles()


    def shipHitHostiles(self):
        if not settings.Player.imIronMan:
            ordinanceHits = pygame.sprite.spritecollide(self.Player, self.ordinance, False) # Regular Square Hit Box
            if ordinanceHits:
                if not self.Player.invincible:
                    self.Player.whoopsImDead()
                
                for eachOrdinance in ordinanceHits:
                    self.explosions.add(explosion.Explosion(self, eachOrdinance.X, eachOrdinance.Y,self.explosionSets,0))
                    eachOrdinance.imDead = True
                    #self.points.append(point.Point(self, eachHostile.X, eachHostile.Y, eachHostile.myValue, 'Vinegar Stroke'))

            hostilesHits = pygame.sprite.spritecollide(self.Player, self.hostiles, False, pygame.sprite.collide_circle) # Using Circle Hit Box
            if hostilesHits:
                if not self.Player.invincible:
                    self.Player.whoopsImDead()

                for eachHostile in hostilesHits:
                    self.explosions.add(explosion.Explosion(self, eachHostile.X, eachHostile.Y,self.explosionSets))
                    eachHostile.imDead = True
                    self.points.append(point.Point(self, eachHostile.X, eachHostile.Y, eachHostile.myValue, 'Vinegar Stroke'))
