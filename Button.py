import pygame


class Button:
    def __init__(self, x, y, width, height, text, color=(170, 170, 170), on_click=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color # Default Grey
        self.text = text
        self.font = pygame.font.Font(None, 30)
        self.on_click = on_click # On click function


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, border_radius=8)

        # Button text
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)


    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)


    def handle_click(self):
        if self.on_click:
            self.on_click()
