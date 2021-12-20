from typing import KeysView
import pygame as pg

from sprites import *

pg.init()
 
WIDTH = 800
HEIGHT = 600
 
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED= (255,0,0)
 
ting_pos_x = 400
ting_pos_y = 400
 
ting_size_x = 10
ting_size_y = 10
 
speed = 10
 
direction_x = speed
direction_y = -speed
 
screen = pg.display.set_mode((WIDTH,HEIGHT))
 
clock = pg.time.Clock()
FPS = 120
 
all_sprites = pg.sprite.Group()
enemies =pg.sprite.Group()

slime = Enemy()
all_sprites.add(slime)
enemies.add(slime)

player = Player()
all.sprites.add(player)



playing = True
while playing:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
            pg.quit()
 
    # hvis helt til høyre
    #if ting_pos_x + ting_size_x > WIDTH:
        #ting_pos_x = WIDTH - ting_size_x
    # hvis helt til venstre
    #if ting_pos_x < 0:
        #ting_pos_x = 0
 
    # opp og ned
    #if ting_pos_y < 0:
        #ting_pos_y = 0
    #if ting_pos_y + ting_size_y > HEIGHT:
        #ting_pos_y = HEIGHT - ting_size_y
 
    # tegner ting til skjerm på valgt posisjon, og størrelse
    screen.fill(WHITE)
 
    all_sprites.update()

    hits = pg.sprite.spritecollide(player, enemies, True)
    while len(enemies) < 10:
            slime = Enemy()
            all_sprites.add(slime)
            enemies.add(slime)

    all_sprites.draw(screen)

    pg.display.update()