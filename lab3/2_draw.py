import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((202,204,206))

circle(screen, (0,0,0), (200,200), 100, 2)
circle(screen, (255,255,0), (200,200), 99,0)
rect(screen, (0,0,0),(150,250,100, 20),0)
circle(screen, (0,0,0), (150,170), 20, 1)
circle(screen, (255,0,0,),(150,170), 19, 0)
circle(screen, (0,0,0), (150, 170), 9, 0)
circle(screen, (0,0,0), (250,170), 16, 1)
circle(screen, (255,0,0), (250,170), 15,0)
circle(screen, (0,0,0), (250,170), 8, 0)
line(screen, (0,0,0), (100,100),(175,160), 15)
line(screen, (0,0,0), (300,120), (225, 157), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()