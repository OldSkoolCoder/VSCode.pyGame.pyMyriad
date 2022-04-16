import pygame
import random
import settings
#import sprites
import player
import bullet

class Game:
    def __init__(self):
        # Initialise game code
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((settings.Screen.WIDTH, settings.Screen.HEIGHT))
        pygame.display.set_caption(settings.TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.bullets = pygame.sprite.Group()


    def new(self):
        # Starts a new game
        self.allSprites = pygame.sprite.Group()

        self.bullets.empty()

        # Add Player Sprites
        self.Player = player.Player(self) 
        self.allSprites.add(self.Player)

        # Add Enemy Sprites

        # Add any other sprites
        self.level = 1
        self.wave = 1
        self.powerUp = 0
        self.run()

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

        self.removeDoneBullets()

    def events(self):
        # Game Loop Events handler
        self.Player.events()
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop draw screen
        self.screen.fill(settings.Colours.BLACK)
        self.allSprites.draw(self.screen)
        self.bullets.draw(self.screen)

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
