"""
Ball class definition.

This module defines the ball class. It is used to
display and animate balls that bounce around the screen.
"""

import random

import pygame

from ..asset import load_image
from ..config import RESOLUTION, BALL_IMAGE


class Ball(pygame.sprite.Sprite):
    """Ball Class"""
    def __init__(self, *args, **kwargs):
        """Initialize ball object."""
        super().__init__()
        self.paddle = kwargs['paddle']
        self.on_lose = kwargs['on_lose']
        self.image, self.rect = load_image(BALL_IMAGE)
        #self.sound = asset.load_sound('sounds/blip.wav')
        self.draw_rect = self.rect.inflate(170, 170)
        self.rect.center = (random.randint(1, RESOLUTION[0]-35), 450)
        self.x_vel = int(kwargs['speed']) + random.randint(1,4)
        self.y_vel = -(int(kwargs['speed']) + random.randint(1,4))
        self.left_wall = pygame.Rect(0, 0, 1, RESOLUTION[1]) 
        self.right_wall = pygame.Rect(799, 0, 1, RESOLUTION[1])
        self.top_wall = pygame.Rect(0, 0, RESOLUTION[0], 1)
        self.bottom_wall = pygame.Rect(0, RESOLUTION[1]-40, RESOLUTION[0], 1)       
        
        
    def update(self, *args, **kwargs):
        """Update the ball position and check for rect collisions."""
        self.rect = self.rect.move(self.x_vel, self.y_vel)
        self.draw_rect.center = self.rect.center
        
        if self.rect.colliderect(self.left_wall) or self.rect.colliderect(self.right_wall): #ball has hit side of screen
            self.x_vel = -self.x_vel 
            #self.sound.play()
        elif self.rect.colliderect(self.top_wall):     #ball has hit top of screen
            self.y_vel = -self.y_vel 
            #self.sound.play()
        elif self.rect.colliderect(self.paddle.rect):  #ball has hit paddle
            self.y_vel = -self.y_vel
            #self.sound.play()
        elif self.rect.colliderect(self.bottom_wall):  #ball has missed paddle
            self.on_lose()
            #self.sound.play()
