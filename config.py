"""Configuration classes for the Snake game."""

from pathlib import Path
from typing import Final


class Settings:
    """Centralized configuration for the Snake game."""

    WIDTH: Final[int] = 600
    HEIGHT: Final[int] = 600
    TITLE: Final[str] = "SNAKE GAME"

    BACKGROUND_COLOR: Final[tuple[int, int, int]] = (0, 0, 0)
    SNAKE_COLOR: Final[tuple[int, int, int]] = (0, 255, 89)
    APPLE_COLOR: Final[tuple[int, int, int]] = (255, 40, 47)
    SCORE_COLOR: Final[tuple[int, int, int]] = (255, 255, 255)

    HEAD_SIZE: Final[int] = 22
    FPS: Final[int] = 20
    SNAKE_SPEED: Final[int] = 10

    INITIAL_X: Final[int] = 0
    INITIAL_Y: Final[int] = 0

    SCORE_POSITION: Final[tuple[int, int]] = (220, 0)
    LENGTH_POSITION: Final[tuple[int, int]] = (10, 0)

    FOOD_MARGIN: Final[int] = 100
    GAME_OVER_DELAY: Final[float] = 1.0

    BASE_DIR: Final[Path] = Path(__file__).resolve().parent
    ASSETS_DIR: Final[Path] = BASE_DIR / "assets"
    IMAGE_DIR: Final[Path] = ASSETS_DIR / "image"
    MUSIC_DIR: Final[Path] = ASSETS_DIR / "music"

    BACKGROUND_IMAGE: Final[Path] = IMAGE_DIR / "bg.png"
    THEME_MUSIC: Final[Path] = MUSIC_DIR / "Snake Game - Theme Song.mp3"
    GAME_OVER_MUSIC: Final[Path] = MUSIC_DIR / "music_by_game_over.mp3"

    FONT_NAME: Final[str] = "Arial"
    FONT_SIZE: Final[int] = 40