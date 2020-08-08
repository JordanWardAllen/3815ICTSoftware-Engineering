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
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.playerImg = pygame.image.load("player.png")
        self.playerImg = pygame.transform.scale(self.playerImg, (25, 25))
        self.playerX = playerX
        self.playerY = playerY
        self.rect = self.playerImg.get_rect()

    def drawPlayer(self):
        self.player = screen.blit(self.playerImg, (self.playerX, self.playerY))



    def playerMove(self):
        vel = 3
        move_ticker = 0
        leftKey = True
        rightKey = True
        upKey = True
        downKey = True

        if len(isColliding) > 0:
            if isColliding[0] == "up":
                upKey = False
            elif isColliding[0] == "down":
                downKey = False
            elif isColliding[0] == 'left':
                leftKey = False
            elif isColliding[0] == 'right':
                rightKey = False
        else:
            leftKey = True
            rightKey = True
            upKey = True
            downKey = True


        if move_ticker > 0:
            move_ticker -= 1
        if keys[K_LEFT] and leftKey == True:
            if move_ticker == 0:
                move_ticker = 5
                self.playerX -= vel

        if keys[K_RIGHT] and rightKey == True:
            if move_ticker == 0:
                move_ticker = 5
                self.playerX += vel

        if keys[K_DOWN] and downKey == True:
            if move_ticker == 0:
                move_ticker = 5
                self.playerY += vel
        if keys[K_UP] and upKey == True:
            if move_ticker == 0:
                move_ticker = 5
                self.playerY -= vel





class Wall(pygame.sprite.Sprite):
    def __init__(self, wallX,wallY, wallHeight, wallWidth):
        super().__init__()
        self.wallColour = (255,255,255)
        self.wallX = wallX
        self.wallY = wallY
        self.wallHeight = wallHeight
        self.wallWidth = wallWidth
        self.rect = pygame.draw.rect(screen, self.wallColour, (self.wallX, self.wallY, self.wallHeight, self.wallWidth))



pygame.init()

displayWindow = (600, 660)



# Set up the drawing window
screen = pygame.display.set_mode(displayWindow)
background = pygame.Surface(displayWindow)
pygame.display.set_caption("Pac Man")
move_ticker = 0

clock = pygame.time.Clock()




def imageFunc():
    screen.blit(backgroundImg, (0, 80))
    screen.blit(header, (0, 0))


backgroundImg = pygame.image.load("colourmap.png")
header = pygame.image.load("header.png")
screen.blit(background,(0,0))
player = Player(20, 150)

playerGroup = pygame.sprite.Group()
blockedGroup = pygame.sprite.Group()
running = True
isColliding = []


while running:
    keys = pygame.key.get_pressed()
    # Did the user click the window close button?
    playerGroup.add(player)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    wall1 = Wall(0, 80, 600, 10)
    wall2 = Wall(0, 650, 600, 10)
    wall3 = Wall(0, 0, 10, 660)
    wall4 = Wall(590, 0, 10, 660)
    wall5 = Wall(50, 130, 60, 40)
    wall6 = Wall(490, 130, 60, 40)
    wall7 = Wall(150, 130, 100, 40)
    wall8 = Wall(350, 130, 100, 40)
    wall9 = Wall(50, 210, 60, 40)
    wall10 = Wall(490, 210, 60, 40)
    wall11 = Wall(290, 90, 20, 80)
    wall12 = Wall(290, 230, 20, 60)
    wall13 = Wall(230, 210, 140, 20)
    wall14 = Wall(10, 290, 100, 60)
    wall15 = Wall(490, 290, 100, 60)
    wall16 = Wall(490, 390, 100, 60)
    wall17 = Wall(10, 390, 100, 60)
    wall18 = Wall(50, 490, 60, 60)
    wall19 = Wall(490, 490, 60, 60)
    wall20 = Wall(350, 510, 100, 40)
    wall21 = Wall(150, 510, 100, 40)
    wall22 = Wall(290, 470, 20, 80)
    wall23 = Wall(230, 450, 140, 20)
    wall24 = Wall(50, 590, 140, 20)
    wall25 = Wall(230, 590, 140, 20)
    wall26 = Wall(410, 590, 140, 20)
    wall27 = Wall(230, 325, 145, 85)
    wall28 = Wall(150, 390, 40, 80)
    wall29 = Wall(410, 390, 40, 80)
    wall30 = Wall(410, 210, 40, 140)
    wall31 = Wall(150, 210, 40, 140)
    wall32 = Wall(190, 270, 60, 20)
    wall33 = Wall(350, 270, 60, 20)
    imageFunc()


    player.drawPlayer()
    player.playerMove()
    pressed_keys = pygame.key.get_pressed()


    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            if player.player.colliderect(wall1) or player.player.colliderect(
                    wall2) or player.player.colliderect(wall3) or player.player.colliderect(wall4) or player.player.colliderect(wall5):
                print(isColliding)
                print("collided")
                if len(isColliding) == 0:
                    isColliding.append(pygame.key.name(key_constant))
                    key_name = pygame.key.name(key_constant)
                if len(isColliding) == 0:
                    isColliding.append(pygame.key.name(key_constant))
                    key_name = pygame.key.name(key_constant)

            else:
                isColliding.clear()

    # clock.tick(60)
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
quit()