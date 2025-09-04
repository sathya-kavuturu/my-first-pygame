import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((1280,720))
pg.display.set_caption("Runner")
clock = pg.time.Clock()
test_surface = pg.Surface((100,100))
test_surface.fill("orange")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(test_surface,(200,100))
    pg.display.update()
    clock.tick(60)