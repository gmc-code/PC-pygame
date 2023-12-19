"""
Level Module

This module defines the level class. It is a sprite that
displays the current level number.
"""

import pygame

from ..config import RESOLUTION


class Level(pygame.sprite.Sprite):
    """Level Class"""
    def __init__(self, level):
        super().__init__()
        self.level = level
        self.color = (200,200,200) 
        self.font = pygame.font.Font(None, 30)
        self.image = self.font.render(str(self.level), True, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (100, RESOLUTION[1]-25)
        self.draw_rect = self.rect.inflate(40,10)
