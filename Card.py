import pygame


class Card:
    def __init__(self, card_type, x, y, width=100, height=150, color=(255, 255, 255)):
        self.card_type = card_type
        self.x = x
        self.y = y
        self.width = width #default 100
        self.height = height #default 150
        self.color = color #default white
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        """Draws the card on the screen."""
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

    def is_clicked(self, mouse_pos):
        """
        Checks if the card has been clicked.

        :param mouse_pos: Tuple (x, y) of the mouse position.
        :return: True if clicked, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)

    def on_click(self):
        """Function that runs when the card is clicked."""
        print(f"Card '{self.card_type}' was clicked!")