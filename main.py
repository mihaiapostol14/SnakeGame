"""Application launcher for the Snake game."""

from game import Game


class App:
    """Application entry point."""

    def __init__(self) -> None:
        """Initialize the application."""
        self.game = Game()

    def execute(self) -> None:
        """Start the Snake game."""
        self.game.run()


if __name__ == "__main__":
    App().execute()