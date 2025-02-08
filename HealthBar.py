import pygame

class HealthBar:
    def __init__(self, x, y, max_health):
        self.x = x
        self.y = y
        self.width = 300
        self.height = 20
        self.max_health = max_health
        self.current_health = max_health
        self.color = (255, 0, 0)  # Default red
        self.border_color = (255, 255, 255)  # Default white


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
