from os import X_OK
import pygame
from configparser import ConfigParser

config = ConfigParser()
config.read('./.config')
WINDOW_WIDTH = int(config['DEFAULT']['SCREEN_WIDTH'])
WINDOW_HEIGHT = int(config['DEFAULT']['SCREEN_HEIGHT'])
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("resources/image/ball.png"))
GAME_STATE = 0  # 0:ready,1:active,-1:over


run = True
while run:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
