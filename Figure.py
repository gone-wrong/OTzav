import pygame


class Figure:
    def __init__(self, x, y, color=(200, 200, 200), text="", PROPORTION=1):

        self.PROPORTION = PROPORTION
        self.x = x * PROPORTION
        self.y = y * PROPORTION
        self.width = 100 * PROPORTION
        self.height = 150 * PROPORTION
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, int(36 * PROPORTION))

        self.damage_taken = ""
        self.damage_taken_duration = 0
        self.status_effect = ""
        self.status_effect_type = ""
        self.status_effect_duration = 0

        # Oval Scaling
        self.oval_width = 80 * PROPORTION
        self.oval_height = 40 * PROPORTION
        self.oval_x_offset = 80 * PROPORTION


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=int(10 * self.PROPORTION))

        # Draw for text messages
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

        # Draw damage_taken text
        if self.damage_taken:
            if self.damage_taken_duration > 0:
                self.damage_taken_duration -= 1
                self.draw_oval_text(screen, self.damage_taken,
                                    (self.x - self.oval_x_offset, self.y + self.height // 2),
                                    (200, 50, 50))  # Red
            else:
                self.reset_damage_taken()

        # Draw status_effect text
        if self.status_effect:
            if self.status_effect_duration > 0:
                self.status_effect_duration -= 1
                oval_color = (100, 200, 100) if self.status_effect_type == "Bloom" else (200, 50, 50)
                self.draw_oval_text(screen, self.status_effect,
                                    (self.x + self.width + self.oval_x_offset, self.y + self.height // 2),
                                    oval_color)
            else:
                self.reset_status_effect()


    def draw_oval_text(self, screen, text, position, bg_color):
        text_surface = self.font.render(text, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=position)

        # Draw oval background
        pygame.draw.ellipse(screen, bg_color,
                            (position[0] - self.oval_width // 2, position[1] - self.oval_height // 2,
                             self.oval_width, self.oval_height))

        # Draw text
        screen.blit(text_surface, text_rect)


    def set_damage_taken(self, msg):
        self.damage_taken = msg
        self.damage_taken_duration = 60


    def reset_damage_taken(self):
        self.damage_taken = ""
        self.damage_taken_duration = 0


    def set_status_effect(self, msg, effect_type):
        self.status_effect = msg
        self.status_effect_type = effect_type
        self.status_effect_duration = 60


    def reset_status_effect(self):
        self.status_effect = ""
        self.status_effect_type = ""
        self.status_effect_duration = 0