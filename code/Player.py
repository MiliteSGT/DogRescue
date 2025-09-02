#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import WIN_HEIGHT
from code.Entity import Entity

# Constantes
PLAYER_SPEED = 5
JUMP_FORCE = 15
GRAVITY = 1

class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.vel_y = 0
        self.on_ground = True

    def move(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED


        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED


        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -JUMP_FORCE
            self.on_ground = False


        self.vel_y += GRAVITY
        self.rect.y += self.vel_y


        if self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.vel_y = 0
            self.on_ground = True