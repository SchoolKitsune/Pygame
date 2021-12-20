import pygame as pg
vec = pg.math.Vector2
from random import randint

enemy_image = pg.image.load("slime.png")

player_image = pg.image.load("player.png")

class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = player_image
        self.image = pg.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.pos = vec(500, 500)
        self.rect.center = self.pos
        self.speed = 1

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.pos.y -= self.speed

        if keys[pg.K_s]:
            self.pos.y += self.speed

        if keys[pg.K_a]:
            self.pos.x -= self.speed

        if keys[pg.K_d]:
            self.pos.x += self.speed

        self.rect.center = self.pos

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.pos = vec(1000, randint(0, 600))
        self.rect.center = self.pos
        self.speed_x = 1
    def update(self):
        self.pos.x += self.speed_x

        if self.pos.x > 800:
            self.speed_x = -1

        if self.pos.x < 0:
            self.speed_x = 1

        self.rect.center = self.pos









        self.life = 1
