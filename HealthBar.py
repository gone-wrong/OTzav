import pygame

class HealthBar:
    def __init__(self, x, y, max_health, PROPORTION):
        self.x = x * PROPORTION
        self.y = y * PROPORTION
        self.width = 300 * PROPORTION
        self.height = 20 * PROPORTION
        self.max_health = max_health
        self.current_health = max_health
        self.color = (255, 0, 0)  #Default red
        self.border_color = (255, 255, 255)  #Default white
        self.font = pygame.font.Font(None, int(24 * PROPORTION))


    def update(self, new_health):
        self.current_health = max(0, min(new_health, self.max_health))


    def draw(self, screen):
        health_ratio = self.current_health / self.max_health
        current_width = int(self.width * health_ratio)

        # Bar background
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, self.width, self.height))

        # Current health bar
        pygame.draw.rect(screen, self.color, (self.x, self.y, current_width, self.height))

        # Draw the border
        pygame.draw.rect(screen, self.border_color, (self.x, self.y, self.width, self.height), 2)

        # Draw the current_health/max_health text
        health_text = f"{self.current_health} / {self.max_health}"
        text_surface = self.font.render(health_text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect) # blit(image/position)