import pygame
import os

# Simple pygame program


from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Import and initialize the pygame library



pygame.init()

displayWindow = (600, 660)


# Set up the drawing window
screen = pygame.display.set_mode(displayWindow)
background = pygame.Surface(displayWindow)


clock = pygame.time.Clock()
bgColour = (0,0,0)
lineColour = (255,255,255)

vel = 1




def imageFunc(playerX, playerY):
    screen.blit(playerImg,(playerX, playerY))
    # screen.blit(backgroundImg, (0, 80))
    # screen.blit(header, (0, 0))




backgroundImg = pygame.image.load("colourmap.png")
header = pygame.image.load("header.png")
playerImg = pygame.image.load("player.png")
playerImg = pygame.transform.scale(playerImg, (25,25))

screen.blit(background,(0,0))
playerX = 50
playerY = 100

move_ticker = 0
# Run until the user asks to quit
running = True

while running:
    keys = pygame.key.get_pressed()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if move_ticker > 0:
        move_ticker -= 1
    if keys[K_LEFT]:
        if move_ticker == 0:
            move_ticker = 5
            playerX -= vel

    if keys[K_RIGHT]:
        if move_ticker == 0:
            move_ticker = 5
            playerX += vel

    if keys[K_DOWN]:
        if move_ticker == 0:
            move_ticker = 5
            playerY += vel
    if keys[K_UP]:
        if move_ticker == 0:
            move_ticker = 5
            playerY -= vel


        # if event.key == pygame.K_LEFT:
        #     playerX -= vel
        #
        # if event.key == pygame.K_UP:
        #     playerY += vel
        #
        # if event.key == pygame.K_DOWN:
        #     playerY -= vel

    # Fill the background with white


    # playerMovement(playerX, playerY)
    screen.fill((0,0,0))
    imageFunc(playerX, playerY)



    # Flip the display

    # clock.tick(50)
    pygame.display.update()






# Done! Time to quit.
pygame.quit()
quit()