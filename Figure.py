import pygame

class Figure:
    def __init__(self, x, y, color=(200, 200, 200), text=""):

        self.x = x
        self.y = y
        self.width = 100
        self.height = 150
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 36)  # Default font


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=10)

        # Draw for text messages
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)