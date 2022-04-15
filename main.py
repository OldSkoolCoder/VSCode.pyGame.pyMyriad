import pygame as pg
import random
import settings
import game
#import sprites

g = game.Game()
g.showStartScreen()
while g.running:
    g.new()
    g.showGameOverScreen()

pg.display.quit()
pg.quit()

