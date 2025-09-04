import pygame as pg
from sys import exit

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Runner")
clock = pg.time.Clock()
test_font = pg.font.Font("font/Pixeltype.ttf", 50)

sky_surf = pg.image.load("graphics/sky.png").convert()
ground_surf = pg.image.load("graphics/ground.png").convert()

score_surf = test_font.render("My Game",False, "Black")
score_rect = score_surf.get_rect(center = (400,50))

snail_surface = pg.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (750,300))

player_surf = pg.image.load("graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (100,300))

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        # if event.type == pg.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos): print("collide")

    screen.blit(sky_surf,(0,0))
    screen.blit(ground_surf, (0,300))
    pg.draw.rect(screen,"Pink", score_rect)
    pg.draw.rect(screen,"Pink", score_rect,10)
    pg.draw.line(screen,"Blue",(0,0),(800,400),5)
    screen.blit(score_surf,score_rect)
  
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.right = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)
    

    # if player_rect.colliderect(snail_rect):
    #     print("collision")
    
    # mouse_pos = pg.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print("collide")

    pg.display.update()
    clock.tick(60)