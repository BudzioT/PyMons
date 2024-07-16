import os

import pygame


class Settings:
    """Settings of the game"""
    def __init__(self):
        """Create the settings"""
        # Window dimensions
        self.WINDOW_WIDTH = 1280
        self.WINDOW_HEIGHT = 720

        # Size of a single tile
        self.TILE_SIZE = 64

        # Basic speed of animations
        self.ANIMATION_SPEED = 6

        # File base absolute path
        self.BASE_PATH = os.path.dirname(os.path.abspath(__file__))

        # Battle outline size
        self.BATTLE_OUTLINE = 4


# Instantiate the settings
settings = Settings()
