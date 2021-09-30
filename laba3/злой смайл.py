import pygame as pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
polygon(screen, (200, 200, 200), [(0,0), (0,400),
                               (400,400), (400,0)])
circle(screen, (255, 255, 0), (200, 200), 120, 0)
circle(screen, (0, 0, 0), (200, 200), 120, 5)

circle(screen, (255,0, 0), (150, 170), 20, 0)
circle(screen, (0, 0, 0), (150, 170), 20, 5)
circle(screen, (0, 0, 0), (150, 170), 5, 0)

circle(screen, (255,0, 0), (250, 170), 15, 0)
circle(screen, (0, 0, 0), (250, 170), 15, 5)
circle(screen, (0,0, 0), (250, 170), 5, 0)

rect(screen,(0, 0, 0), (150, 260, 100, 30), 0)
polygon(screen, (0, 0, 0), [(140,120), (180,130),
                               (170,140), (130,130)], 0)
polygon(screen, (0, 0, 0), [(260,120), (220,130),
                               (230,140), (270,130)], 0)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
