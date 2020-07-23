import pygame
import os
os.environ["SDL_VIDEO_CENTERED"] = "1"

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Player(pygame.sprite.Sprite):

    def __init__(self, playerX, playerY):
        self.playerImg = pygame.image.load("player.png")
        self.playerImg = pygame.transform.scale(self.playerImg, (25, 25))
        self.playerX = playerX
        self.playerY = playerY
        self.rect = self.playerImg.get_rect()

    def drawPlayer(self):
        self.player = screen.blit(self.playerImg, (self.playerX, self.playerY))

    def playerMove(self):
        vel = 1
        move_ticker = 0

        if move_ticker > 0:
            move_ticker -= 1
        if keys[K_LEFT]:
            if move_ticker == 0:
                move_ticker = 5
                self.playerX -= vel

        if keys[K_RIGHT]:
            if move_ticker == 0:
                move_ticker = 5
                self.playerX += vel

        if keys[K_DOWN]:
            if move_ticker == 0:
                move_ticker = 5
                self.playerY += vel
        if keys[K_UP]:
            if move_ticker == 0:
                move_ticker = 5
                self.playerY -= vel





class Wall(pygame.sprite.Sprite):
    def __init__(self, wallX,wallY, wallHeight, wallWidth):
        self.wallColour = (255,255,255)
        self.wallX = wallX
        self.wallY = wallY
        self.wallHeight = wallHeight
        self.wallWidth = wallWidth
        self.wall = pygame.draw.rect(screen, self.wallColour, (self.wallX, self.wallY, self.wallHeight, self.wallWidth))









pygame.init()

displayWindow = (600, 660)

playerGroup = pygame.sprite.Group()
blockedGroup = pygame.sprite.Group()

# Set up the drawing window
screen = pygame.display.set_mode(displayWindow)
background = pygame.Surface(displayWindow)
pygame.display.set_caption("Pac Man")
move_ticker = 0

clock = pygame.time.Clock()
vel = 2



def imageFunc(playerX, playerY):
    screen.blit(backgroundImg, (0, 80))
    screen.blit(header, (0, 0))



backgroundImg = pygame.image.load("colourmap.png")
header = pygame.image.load("header.png")


screen.blit(background,(0,0))

player = Player(50, 50)


# Run until the user asks to quit
running = True

while running:
    keys = pygame.key.get_pressed()
    hit = False

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if move_ticker > 0:
    #     move_ticker -= 1
    # if keys[K_LEFT]:
    #     if move_ticker == 0:
    #         move_ticker = 5
    #         player.playerX -= -2
    #
    # if keys[K_RIGHT]:
    #     if move_ticker == 0:
    #         move_ticker = 5
    #         playerX += vel
    #
    # if keys[K_DOWN]:
    #     if move_ticker == 0:
    #         move_ticker = 5
    #         playerY += vel
    # if keys[K_UP]:
    #     if move_ticker == 0:
    #         move_ticker = 5
    #         playerY -= vel


    screen.fill((0,0,0))
    #funky implementation
    wall1 = Wall(0,0, 600, 20)
    wall2 = Wall(0, 640, 600, 20)
    wall3 = Wall(0, 0, 20, 660)
    wall4 = Wall(580, 0, 20, 660)



    player.drawPlayer()
    player.playerMove()
    print(player.playerX, player.playerY)


    if player.player.colliderect(wall1.wall) or player.player.colliderect(wall2.wall) or player.player.colliderect(wall3.wall) or player.player.colliderect(wall4.wall):
        hit = True
        print(hit)


    # clock.tick(60)
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
quit()