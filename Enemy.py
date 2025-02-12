import pygame
from Character import Character
from HealthBar import HealthBar
from Figure import Figure
from Element import Fire, Earth, Water, Lightning


class Enemy(Character):
    def __init__(self, health=100, level=1, PROPORTION=1):
        super().__init__(health, level, Figure(x=750, y=100, text="Enemy", PROPORTION=PROPORTION), HealthBar(x=650, y=50, max_health=health, PROPORTION=PROPORTION))
        self.PROPORTION = PROPORTION


    def take_damage(self, amount):
        super().take_damage(amount)
        # self.health_bar.update(self.health)



    def heal(self, amount):
        super().heal(amount)
        # self.health_bar.update(self.health)


    def draw(self, screen):
        self.health_bar.draw(screen)
        self.figure.draw(screen) # Draw the Enemy Figure

        # Positions for indicator circles
        left_circle_x = self.figure.x - (20 * self.PROPORTION)
        right_circle_x = self.figure.x + self.figure.width + (20 * self.PROPORTION)
        circle_y = self.figure.y + (10 * self.PROPORTION)

        # Colors for indicator circle
        element_color = self.get_element_color()
        status_color = self.get_status_color()

        pygame.draw.circle(screen, element_color, (left_circle_x, circle_y), int(10 * self.PROPORTION))  # Applied Element Circle
        pygame.draw.circle(screen, status_color, (right_circle_x, circle_y), int(10 * self.PROPORTION))  # Status Effect Circle


    def get_element_color(self):
        if isinstance(self.applied_element, Fire):
            return 200, 100, 100  # Red
        elif isinstance(self.applied_element, Earth):
            return 100, 200, 100  # Green
        elif isinstance(self.applied_element, Water):
            return 100, 100, 200  # Blue
        elif isinstance(self.applied_element, Lightning):
            return 200, 200, 100  # Yellow
        return 128, 128, 128  # Grey if no element applied


    def get_status_color(self):
        if self.status_effect == "Burning":
            return 255, 0, 0  # Red
        elif self.status_effect == "Bloom":
            return 0, 255, 0  # Green
        return 128, 128, 128  # Grey if no status effect


    def __str__(self):
        return super().__str__()

