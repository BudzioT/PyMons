from os.path import join as path_join

import pygame
from pytmx.util_pygame import load_pygame

from src.settings import settings


class Game:
    """The entire game"""
    def __init__(self):
        """Initialize the game"""
        # Initialize pygame's resources
        pygame.init()

        # Create the main display
        self.surface = pygame.display.set_mode((settings.WINDOW_WIDTH,
                                                settings.WINDOW_HEIGHT))
        # Set its caption
        pygame.display.set_caption("PyMons")

        # Import all game's important assets
        self._load_assets()

    def run(self):
        """Run the game"""
        # Game's loop
        while True:
            # Handle all events
            self._get_events()

            # Update the display surface
            self._update_surface()

    def _get_events(self):
        """Get and handle input events"""
        # Go through each event
        for event in pygame.event.get():
            # If user requested quitting, do it
            if event.type == pygame.QUIT:
                # Free pygame's resources
                pygame.quit()
                # Quit the program
                exit()

    def _update_surface(self):
        """Draw everything onto display surface"""
        # Update the display
        pygame.display.update()

    def _load_assets(self):
        """Load game's assets"""
        self.maps = {
            "world": load_pygame(path_join(settings.BASE_PATH, "../data/maps/world.tmx"))
        }


# If this file is the main one, create and run the game
if __name__ == "__main__":
    game = Game()
    game.run()
