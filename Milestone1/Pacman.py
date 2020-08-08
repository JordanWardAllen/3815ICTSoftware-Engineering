import pygame
import os

os.environ["SDL_VIDEO_CENTERED"] = "1"


class Player(pygame.sprite.Sprite):

    def __init__(self, playerX, playerY):
        # super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.playerImg = pygame.image.load("player.png")
        self.playerImg = pygame.transform.scale(self.playerImg, (27, 27))
        self.playerX = playerX
        self.playerY = playerY
        self.rect = self.playerImg.get_rect()

    def drawPlayer(self):
        self.player = screen.blit(self.playerImg, (self.playerX, self.playerY))



    def playerMove(self, lastKey,collidedKey):
        vel = 1
        leftKey = True
        rightKey = True
        upKey = True
        downKey = True


        if collidedKey == "up":
            upKey = False
        elif collidedKey == "down":
            downKey = False
        elif collidedKey == "left":
            leftKey = False
        elif collidedKey == "right":
            rightKey = False
        else:
            leftKey = True
            rightKey = True
            upKey = True
            downKey = True

        if lastKey == "up" and upKey:
            self.playerY -= vel
        elif lastKey == "down" and downKey:
            self.playerY += vel
        elif lastKey == 'left' and leftKey:
            self.playerX -= vel
        elif lastKey == 'right' and rightKey:
            self.playerX += vel

class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemyX, enemyY, status):
        super().__init__()
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.status = status
        self.rect = pygame.draw.rect(screen, (255,0,0), (self.enemyX, self.enemyY, 27, 27))

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
player = Player(17, 150)


playerGroup = pygame.sprite.Group()
blockedGroup = pygame.sprite.Group()
running = True
lastPressedList = ['']
collidedKey = ''

# Score
score_value = 0
scoreX = 15
scoreY = 45

lives_left = 3
livesX = 450
livesY = 45

font = pygame.font.Font("freesansbold.ttf", 25)



def show_score(x,y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (scoreX, scoreY))


def show_lives(x,y):
    lives = font.render("Lives left: " + str(lives_left), True, (255,255,255))
    screen.blit(lives, (livesX, livesY))


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
    show_score(scoreX, scoreY)
    show_lives(livesX, livesY)
    player.drawPlayer()
    enemy1 = Enemy(150, 175, "hunter")
    enemy2 = Enemy(350, 475, "hunter")

    pressed_keys = pygame.key.get_pressed()
    for key_constant, pressed in enumerate(pressed_keys):
        if pressed:
            lastPressedList.clear()
            lastPressedList.append(pygame.key.name(key_constant))

        # Asbolutely hideous implementation of walls due to spirteGroups not working correctly for the prototpye
        if player.player.colliderect(wall1) or player.player.colliderect(wall2) or player.player.colliderect(wall3) or player.player.colliderect(wall4) or player.player.colliderect(wall5) or player.player.colliderect(wall6) or player.player.colliderect(wall7) or player.player.colliderect(wall8) or player.player.colliderect(wall9)\
                or player.player.colliderect(wall10) or player.player.colliderect(wall11) or player.player.colliderect(wall12) or player.player.colliderect(wall13) or player.player.colliderect(wall14) or player.player.colliderect(wall15) or player.player.colliderect(wall16) or player.player.colliderect(wall17)\
                or player.player.colliderect(wall18) or player.player.colliderect(wall19) or player.player.colliderect(wall20) or player.player.colliderect(wall21) or player.player.colliderect(wall22) or player.player.colliderect(wall23) or player.player.colliderect(wall24) or player.player.colliderect(wall25) \
                or player.player.colliderect(wall26) or player.player.colliderect(wall27) or player.player.colliderect(wall28) or player.player.colliderect(wall29) or player.player.colliderect(wall30) or player.player.colliderect(wall31) or player.player.colliderect(wall32) or player.player.colliderect(wall33):
            if len(collidedKey) <= 0:
                collidedKey = lastPressedList[0]
                print(collidedKey)
        else:
            collidedKey = ''
    if player.player.colliderect(enemy1):
        lives_left -= 1
        player.playerX = 17
        player.playery = 150

    if lives_left < 0:
        #end screen to be displayed
        pygame.quit()

    player.playerMove(lastPressedList[0], collidedKey)
    # clock.tick(60)
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
quit()