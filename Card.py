import pygame


class Card:
    def __init__(self, card_type, x, y, color, player):
        self.card_type = card_type
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 100, 150)
        self.player = player


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=10)


    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


    def on_click(self):
        print(f"Card '{self.card_type}' was clicked")


