import pygame
import random
import settings
import game
#import sprites 

g  = game.Game()
g.showStartScreen()
while g.running:
    g.new()
    g.showGameOverScreen()

pygame.display.quit()
pygame.quit()

