import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Runner")
clock = pg.time.Clock()
test_font = pg.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pg.image.load("graphics/sky.png").convert()
ground_surface = pg.image.load("graphics/ground.png").convert()
text_surface = test_font.render("My Game",False, "Black")
snail_surface = pg.image.load("graphics/snail/snail1.png").convert_alpha()
snail_x_pos = 700

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(350,50))
    if snail_x_pos == 0:
        snail_x_pos = 700
    snail_x_pos -= 4
    screen.blit(snail_surface, (snail_x_pos,270))

    pg.display.update()
    clock.tick(60)