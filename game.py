import pygame as pg 
import random
import settings
#import sprites

class Game:
    def __init__(self):
        # Initialise game code
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((settings.Dimensions.Screen.WIDTH, settings.Dimensions.Screen.HEIGHT))
        pg.display.set_caption(settings.TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        # Starts a new game
        self.allSprites = pg.sprite.Group()

        # Add Player Sprites

        # Add Enemy Sprites

        # Add any other sprites

        self.run()

    def run(self):
        # Game Loop Code
        self.playing = True
        while self.playing:
            self.clock.tick(settings.FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop Update Method
        self.allSprites.update()

    def events(self):
        # Game Loop Events handler
        for event in pg.event.get():
            # check for closing the window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    def draw(self):
        # Game Loop draw screen
        self.screen.fill(settings.Colours.BLACK)
        self.allSprites.draw(self.screen)

        # After redrawing the screen, flip it
        pg.display.flip()

    def showStartScreen(self):
        # Show the start screen of the game
        pass

    def showGameOverScreen(self):
        # show the Game over screen
        pass

