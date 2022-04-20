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
 


# Asteroids -> Meteors
# A/C/E -> A/E/H
# B/D/F -> B/F/I
# G -> C/G/J

# Meteors -> Meteorites
# A/E/H -> A/D
# B/F/I -> B/E
# C/G/J -> C/F 