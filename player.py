"""Snake player entity."""

from __future__ import annotations

from typing import Sequence

import pygame

from config import Settings


class GameObject(pygame.sprite.Sprite):
    """Base class for drawable Pygame game entities."""

    def __init__(
        self,
        width: int,
        height: int,
        color: tuple[int, int, int],
    ) -> None:
        """Initialize the game object."""
        super().__init__()

        self.image: pygame.Surface = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect: pygame.Rect = self.image.get_rect()


class Snake(GameObject):
    """Player-controlled snake."""

    def __init__(
        self,
        width: int,
        height: int,
        color: tuple[int, int, int],
    ) -> None:
        """Initialize the snake."""
        super().__init__(width, height, color)

        self.speed: int = Settings.SNAKE_SPEED
        self.x_direction: int = 0
        self.y_direction: int = 0
        self.length: int = 0

        self.body: list[list[int]] = [
            [Settings.INITIAL_X, Settings.INITIAL_Y]
        ]

    @property
    def position(self) -> tuple[int, int]:
        """Return the snake head position."""
        return self.rect.x, self.rect.y

    def set_position(self, x: int, y: int) -> None:
        """Set the snake head position."""
        self.rect.x = x
        self.rect.y = y

        self.body[0] = [x, y]

    def set_direction(self, x: int, y: int) -> None:
        """Set the snake movement direction."""
        self.x_direction = x
        self.y_direction = y

    def move(self) -> None:
        """Move the snake head according to its current direction."""
        self.rect.x += self.x_direction * self.speed
        self.rect.y += self.y_direction * self.speed

    def grow(self) -> None:
        """Increase the snake length by one segment."""
        self.length += 1

    def update_body(self) -> None:
        """Update the snake body history."""
        self.body.append([self.rect.x, self.rect.y])

        required_segments = self.length + 1

        while len(self.body) > required_segments:
            self.body.pop(0)

    def draw(self, surface: pygame.Surface) -> None:
        """Draw the snake head and body onto the given surface."""
        for segment in self.body:
            pygame.draw.rect(
                surface,
                Settings.SNAKE_COLOR,
                (
                    segment[0],
                    segment[1],
                    Settings.HEAD_SIZE,
                    Settings.HEAD_SIZE,
                ),
            )

    def reset(self) -> None:
        """Reset the snake to its initial state."""
        self.rect.x = Settings.INITIAL_X
        self.rect.y = Settings.INITIAL_Y

        self.x_direction = 0
        self.y_direction = 0
        self.length = 0

        self.body = [
            [Settings.INITIAL_X, Settings.INITIAL_Y]
        ]

    def occupies_position(self, position: Sequence[int]) -> bool:
        """Return whether the snake occupies the specified position."""
        return any(
            segment[0] == position[0] and segment[1] == position[1]
            for segment in self.body
        )