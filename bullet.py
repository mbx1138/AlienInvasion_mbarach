"""
Title: Alien Invasion
Author: Matt Barach
Purpose: Defines the Bullet class and manages fired bullets.

Starter Code: Based on Alien Invasion from Python Crash Course (3rd Edition)
https://github.com/ehmatthes/pcc_3e/tree/main

Custom Asset Attribution: 
Asset: Assets Free Laser Bullets Pack 2020
Author: Wenrexa
Source: https://opengameart.org/content/assets-free-laser-bullets-pack-2020
License: CC0

Date: 7/29/2026
"""


import pygame
from pygame.sprite import Sprite

from pathlib import Path

BULLET_PNG = Path("images/bullet.png")

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load(BULLET_PNG)
        self.rect = self.image.get_rect()

        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Add the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
        self.play_bullet_sound()

    def play_bullet_sound(self):
        effect = pygame.mixer.Sound('Assets\sound\laser.mp3')
        effect.play()