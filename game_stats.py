"""
Title: Alien Invasion
Author: Matt Barach
Purpose: Defines the GameStats class

Starter Code: Based on Alien Invasion from Python Crash Course (3rd Edition)
https://github.com/ehmatthes/pcc_3e/tree/main

Date: 8/12/2026
"""


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1