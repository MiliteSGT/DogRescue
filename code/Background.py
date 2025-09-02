#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED
from code.Entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        speed = ENTITY_SPEED.get(self.name, 1)
        self.rect.centerx -= speed

        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
