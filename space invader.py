import math
import random
import pygame
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
PLAYER_START_X = 360
PLAYER_START_Y =370
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 50
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLSION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load('background.png')
pygame.display.set_caption("Space invader")
icon= pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
playerImg = pygame.image.load('player.png')
playerx = PLAYER_START_X
playery = PLAYER_START_Y
playerX_change = 0
enemyImg = []
enemyX=[]
enemyY=[]
enemyX_change = []
enemyY_change=[]
num_of_enemies =6
for _i in range(num_of_enemies)
enemyImg.append(pygame.image.load('enemy.png'))
enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
enemyX_change.append(ENEMY_SPEED_X)
enemyY_change.append(ENEMY_SPEED_Y)


bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change =0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"
score_value =0
font = pygame.font,Font('freesansbold.ttf',32)
textX = 10
textY = 10
