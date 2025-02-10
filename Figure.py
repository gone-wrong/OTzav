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

        self.damage_taken = ""
        self.damage_taken_duration = 0
        self.status_effect = ""
        self.status_effect_type = ""
        self.status_effect_duration = 0


    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=10)

        # Draw for text messages
        text_surface = self.font.render(self.text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        screen.blit(text_surface, text_rect)

        # Draw damage_taken text
        if self.damage_taken:
            if self.damage_taken_duration > 0:
                self.damage_taken_duration -= 1
                self.draw_oval_text(screen, self.damage_taken, (self.x - 80, self.y + self.height // 2),
                                    (200, 50, 50))  # Red
            else:
                self.reset_damage_taken()


        # Draw status_effect text
        if self.status_effect:
            if self.status_effect_duration > 0:
                print("drawing status effect")
                self.status_effect_duration -= 1
                if self.status_effect_type == "Bloom":
                    oval_color = (100, 200, 100)
                else:
                    oval_color = (200, 100, 100)
                self.draw_oval_text(screen, self.status_effect, (self.x + self.width + 80, self.y + self.height // 2),
                                    oval_color)  # Green for Bloom, Red otherwise (for Burning)
            else:
                print("stopped drawing status effect")
                self.reset_status_effect()


    def draw_oval_text(self, screen, text, position, bg_color):
        oval_width, oval_height = 80, 40
        text_surface = self.font.render(text, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=position)

        # Draw oval background
        pygame.draw.ellipse(screen, bg_color,
                            (position[0] - oval_width // 2, position[1] - oval_height // 2, oval_width, oval_height))

        # Draw text
        screen.blit(text_surface, text_rect)


    def set_damage_taken(self, msg):
        self.damage_taken = msg
        self.damage_taken_duration = 60


    def reset_damage_taken(self):
        self.damage_taken = ""
        self.damage_taken_duration = 0


    def set_status_effect(self, msg, type):
        self.status_effect = msg
        self.status_effect_type = type
        self.status_effect_duration = 60


    def reset_status_effect(self):
        self.status_effect = ""
        self.status_effect_type = 0
        self.status_effect_duration = 0
