import pygame
import random

# initialization
pygame.init()

# creating the screen
screen = pygame.display.set_mode((800, 600))
# setting background
background = pygame.image.load('feild background.jfif')
# caption and icon
pygame.display.set_caption("FEILD INVADERS")
icon = pygame.image.load('ufo1.png')
pygame.display.set_icon(icon)
# player
playerImg = pygame.image.load('water ball gun.png')
player_X = 370
player_Y = 480
playerx_change = 0

# enemy
enemyImg = pygame.image.load('fox.png')
enemyx_change = 1
enemyy_change = 40

enemy_X = random.randint(0,736)
enemy_Y = random.randint(0,156)
# ready- cant see bullet
# fire- bullet is fired and visible on screen
# bullet
bulletImg = pygame.image.load('water ball.png')
bullet_x = 50
bullet_y = 480
bulletx_change = 0
bullety_change = 3
bullet_state = "ready"


def player(x,y):
    screen.blit(playerImg, (x,y))
def enemy(x,y):
    screen.blit(enemyImg, (x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x,y))




# game loop
running = True
while running:
    # rgb-red,green and blue
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerx_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerx_change = 0.1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_x = player_X
                    fire_bullet(bullet_x,bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerx_change = 0
    player_X += playerx_change
    # setting boundaries closed
    if player_X <= 0:
        player_X = 0
    elif player_X >= 736:
        player_X = 736
    # enemy movements
    enemy_X += enemyx_change
    if enemy_X <= 0:
        enemyx_change = 1
        enemy_Y += enemyy_change
    elif enemy_X >= 736:
        enemyx_change = -1
        enemy_Y += enemyy_change
    # bullet movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullety_change

    fire_bullet(bullet_x,bullet_y)
    enemy(enemy_X,enemy_Y)
    player(player_X,player_Y)
    pygame.display.update()