import pygame
from configparser import ConfigParser

from pygame import draw

config = ConfigParser()
config.read('./.config')

# screen window configuration
WINDOW_WIDTH = int(config['DEFAULT']['SCREEN_WIDTH'])
WINDOW_HEIGHT = int(config['DEFAULT']['SCREEN_HEIGHT'])
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Pong")
pygame.display.set_icon(pygame.image.load("resources/image/ball.png"))

# game configuration
clock = pygame.time.Clock()
GAME_STATE = 0  # 0:ready,1:active,-1:over
FPS = 60


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, size, colour=(255, 255, 255)) -> None:
        super().__init__()
        self.pos_x = x
        self.pos_y = y
        self.radius = 10*size
        self.colour = colour
        self.image = pygame.Surface((self.radius*2, self.radius*2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        pygame.draw.circle(self.image, self.colour,
                           (self.radius, self.radius), self.radius)


# create game
ball = Ball(150, 200, 1)
ball_group = pygame.sprite.Group()
ball_group.add(ball)


run = True
while run:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if GAME_STATE == 0:
        # draw partition
        pygame.draw.line(screen, (222, 222, 222), (WINDOW_WIDTH //
                         2, 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT))
        # agents action
        ball_group.draw(screen)
        ball_group.update()
    pygame.display.update()
    clock.tick(FPS)  # control fps
