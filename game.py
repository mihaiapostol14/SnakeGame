"""Main Snake game engine."""

from __future__ import annotations

from time import sleep

import pygame

from config import Settings
from food import Food
from player import Snake


class Game:
    """Main controller responsible for the complete game lifecycle."""

    def __init__(self) -> None:
        """Initialize Pygame and construct all game objects."""
        pygame.init()

        self.screen: pygame.Surface = pygame.display.set_mode(
            (Settings.WIDTH, Settings.HEIGHT)
        )

        pygame.display.set_caption(Settings.TITLE)

        self.clock: pygame.time.Clock = pygame.time.Clock()

        self.font: pygame.font.Font = pygame.font.SysFont(
            Settings.FONT_NAME,
            Settings.FONT_SIZE,
        )

        self.background_image: pygame.Surface = pygame.image.load(
            str(Settings.BACKGROUND_IMAGE)
        ).convert()

        self.snake: Snake = Snake(
            width=Settings.HEAD_SIZE,
            height=Settings.HEAD_SIZE,
            color=Settings.SNAKE_COLOR,
        )

        self.snake.set_position(
            Settings.INITIAL_X,
            Settings.INITIAL_Y,
        )

        self.food: Food = Food(
            width=Settings.HEAD_SIZE,
            height=Settings.HEAD_SIZE,
            color=Settings.APPLE_COLOR,
        )

        self.food.random_position()

        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group(
            self.snake,
            self.food,
        )

        self.food_sprites: pygame.sprite.Group = pygame.sprite.Group(
            self.food,
        )

        self.score: int = 0
        self.running: bool = True

        self.start_music()

    def start_music(self) -> None:
        """Start the game's looping theme music."""
        pygame.mixer.music.load(str(Settings.THEME_MUSIC))
        pygame.mixer.music.play(-1)

    def process_events(self) -> None:
        """Process all Pygame window and keyboard events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        self.process_keyboard()

    def process_keyboard(self) -> None:
        """Process keyboard controls for the snake."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.snake.set_direction(0, -1)

        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.snake.set_direction(0, 1)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.snake.set_direction(1, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.snake.set_direction(-1, 0)

        if keys[pygame.K_ESCAPE]:
            self.running = False

    def update(self) -> None:
        """Update the game state for the current frame."""
        self.snake.move()
        self.snake.update_body()

        self.check_boundary_collision()
        self.check_food_collision()

    def check_boundary_collision(self) -> None:
        """Check whether the snake has left the game window."""
        if (
            self.snake.rect.x < 0
            or self.snake.rect.x + self.snake.rect.width > Settings.WIDTH
            or self.snake.rect.y < 0
            or self.snake.rect.y + self.snake.rect.height > Settings.HEIGHT
        ):
            self.game_over()

    def check_food_collision(self) -> None:
        """Check whether the snake has collided with the food."""
        collisions = pygame.sprite.spritecollide(
            self.snake,
            self.food_sprites,
            dokill=False,
        )

        if self.food in collisions:
            self.snake.grow()
            self.score += 1
            self.food.random_position()

    def game_over(self) -> None:
        """Play the game-over sound and terminate the game."""
        pygame.mixer.music.load(str(Settings.GAME_OVER_MUSIC))
        pygame.mixer.music.play(0)

        sleep(Settings.GAME_OVER_DELAY)

        self.running = False

    def draw_background(self) -> None:
        """Draw the game's background."""
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.screen.blit(self.background_image, (0, 0))

    def draw_entities(self) -> None:
        """Draw all game entities."""
        self.food_sprites.draw(self.screen)
        self.snake.draw(self.screen)

    def draw_score(self) -> None:
        """Draw the score and snake length counters."""
        score_text = self.font.render(
            f"Score:{self.score}",
            True,
            Settings.SCORE_COLOR,
        )

        length_text = self.font.render(
            f"length:{self.snake.length}",
            True,
            Settings.SCORE_COLOR,
        )

        self.screen.blit(
            score_text,
            Settings.SCORE_POSITION,
        )

        self.screen.blit(
            length_text,
            Settings.LENGTH_POSITION,
        )

    def render(self) -> None:
        """Render the current game state."""
        self.draw_background()
        self.draw_entities()
        self.draw_score()

        pygame.display.update()

    def run(self) -> None:
        """Execute the main game loop."""
        while self.running:
            self.process_events()
            self.update()

            if self.running:
                self.render()

            self.clock.tick(Settings.FPS)

        self.shutdown()

    def shutdown(self) -> None:
        """Cleanly shut down Pygame."""
        pygame.mixer.music.stop()
        pygame.quit()