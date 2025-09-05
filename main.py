import pygame as pg
from sys import exit

def display_score():
    current_time = int((pg.time.get_ticks() -start_time)/1000)
    score_surf = test_font.render(f"Score: {current_time}",False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50)) 
    screen.blit(score_surf,score_rect)
    return current_time

pg.init()
screen = pg.display.set_mode((800,400))
pg.display.set_caption("Runner")
clock = pg.time.Clock()
test_font = pg.font.Font("font/Pixeltype.ttf", 50)
game_active = False
start_time = 0
score = 0

sky_surf = pg.image.load("graphics/sky.png").convert()
ground_surf = pg.image.load("graphics/ground.png").convert()

snail_surface = pg.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (750,300))

player_surf = pg.image.load("graphics/Player/player_stand.png").convert_alpha()
player_rect = player_surf.get_rect(bottomright = (100,300))

#Intro
player_stand = pg.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand = pg.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

#Game Title & Instructions
title = test_font.render("Pixel Runner",False,"yellow")
title_rect = title.get_rect(midbottom = (400, 100))
instructions = test_font.render("Press Space to Run",False,"yellow")
instructions_rect = instructions.get_rect(topleft = (270,300))

player_gravity = 0

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if game_active:
            if event.type == pg.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos): 
                    player_gravity = -20

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and player_rect.bottom >=300:
                    player_gravity = -20

        else:
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                game_active = True
                snail_rect.x = 800
                start_time = pg.time.get_ticks()
            

    if game_active:
        screen.blit(sky_surf,(0,0))
        screen.blit(ground_surf, (0,300))

        # pg.draw.line(screen,"Blue",(0,0),(800,400),5)
        score = display_score()
    
        snail_rect.x -= 5
        if snail_rect.right <= 0: snail_rect.right = 800
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom > 300: player_rect.bottom = 300 
        screen.blit(player_surf, player_rect)

        #collision
        if snail_rect.colliderect(player_rect):
            game_active = False
    
    else:
        screen.fill((94,129,162))
        screen.blit(title, title_rect)
        screen.blit(player_stand, player_stand_rect)

        score_message  = test_font.render(f"Score: {score}", False, "yellow")
        score_message_rect  = score_message.get_rect(topleft = (340,300))

        if score == 0: screen.blit(instructions, instructions_rect)
        else: screen.blit(score_message, score_message_rect)
    

    pg.display.update()
    clock.tick(60)