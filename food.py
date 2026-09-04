"""Food entity for the Snake game."""

from __future__ import annotations

import random

import pygame

from config import Settings
from player import GameObject


class Food(GameObject):
    """Apple that the snake can collect."""

    def __init__(
        self,
        width: int,
        height: int,
        color: tuple[int, int, int],
    ) -> None:
        """Initialize the food."""
        super().__init__(width, height, color)

    def random_position(self) -> None:
        """Place the food at a random position inside the game area."""
        max_x = Settings.WIDTH - Settings.FOOD_MARGIN
        max_y = Settings.HEIGHT - Settings.FOOD_MARGIN

        self.rect.x = random.randrange(max_x)
        self.rect.y = random.randrange(max_y)