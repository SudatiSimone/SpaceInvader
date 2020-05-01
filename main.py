

import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Tile and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('transportation.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

def player():
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 150, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player()
    pygame.display.update()
