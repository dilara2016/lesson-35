import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y =380
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
