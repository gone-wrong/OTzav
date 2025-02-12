import pygame
from Button import Button


class UpgradeMenu:
    def __init__(self, player, PROPORTION):
        self.PROPORTION = PROPORTION  # Store proportion
        self.width = int(530 * PROPORTION)
        self.height = int(250 * PROPORTION)
        self.x = int(20 * PROPORTION)
        self.y = int(20 * PROPORTION)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_showing = False
        self.player = player
        self.font_size = int(36 * PROPORTION)

        # Button settings
        label_width = int(40 * PROPORTION)
        button_width = int(40 * PROPORTION)
        button_height = int(40 * PROPORTION)
        row_spacing = int(50 * PROPORTION)
        button_spacing = int(50 * PROPORTION)  # Space between buttons

        start_x = self.x + int(30 * PROPORTION)
        row_y = self.y + int(50 * PROPORTION)

        self.buttons = []
        self.probability_buttons = []
        self.labels = []
        self.stat_texts = []

        elements = [
            ("F", "Fire", (200, 100, 100)),
            ("E", "Earth", (100, 200, 100)),
            ("W", "Water", (100, 100, 200)),
            ("L", "Lightning", (200, 200, 100)),
        ]

        for i, (label, element, color) in enumerate(elements):
            label_x = start_x + (i % 2) * (self.width // 2)
            button_x = label_x + label_width + int(10 * PROPORTION)
            probability_button_x = button_x + button_spacing
            stat_x = probability_button_x + button_spacing + int(20 * PROPORTION)
            label_y = row_y + (i // 2) * row_spacing

            self.labels.append((label, label_x, label_y + int(8 * PROPORTION)))

            self.buttons.append(Button(button_x, label_y, button_width, button_height, "+", color,
                                       lambda e=element: self.upgrade_element(e), PROPORTION))

            self.probability_buttons.append(Button(probability_button_x, label_y, button_width, button_height, "x", color,
                                                   lambda e=element: self.upgrade_element_probability(e), PROPORTION))

            self.stat_texts.append((element, stat_x, label_y + int(8 * PROPORTION)))

        # Upgrade max cards button
        self.cards_upgrade_button = Button(self.x + int(50 * PROPORTION), row_y + int(2 * row_spacing),
                                           int(250 * PROPORTION), int(40 * PROPORTION),
                                           "Upgrade Max Cards", (180, 180, 180), self.upgrade_cards, PROPORTION)

        # Close button (bottom-right corner)
        self.close_button = Button(self.x + self.width - int(50 * PROPORTION),
                                   self.y + self.height - int(50 * PROPORTION),
                                   int(40 * PROPORTION), int(40 * PROPORTION),
                                   "X", (255, 50, 50), self.hide, PROPORTION)

    def upgrade_element(self, element_type):
        if self.player.skill_points >= 1:
            self.player.upgrade_element(element_type)
            self.player.skill_points -= 1
        else:
            print("Not enough skill points for element upgrade.")

    def upgrade_element_probability(self, element_type):
        if self.player.skill_points >= 2:
            self.player.upgrade_element_probability(element_type)
            self.player.skill_points -= 2
            print(f"Upgraded {element_type} probability.")
        else:
            print("Not enough skill points for probability upgrade.")

    def upgrade_cards(self):
        if self.player.skill_points >= 3:
            self.player.upgrade_max_cards_flipped()
            self.player.skill_points -= 3
        else:
            print("Not enough skill points.")

    def show(self):
        self.is_showing = True

    def hide(self):
        self.is_showing = False

    def draw(self, screen):
        if self.is_showing:
            pygame.draw.rect(screen, (50, 50, 50), self.rect, border_radius=int(15 * self.PROPORTION))  # Menu background
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 3, border_radius=int(15 * self.PROPORTION))  # White border

            # Draw labels
            font = pygame.font.Font(None, self.font_size)

            # Skill Points display (top-left corner)
            skill_points_text = font.render(f"Skill points: {self.player.skill_points}", True, (255, 255, 255))
            screen.blit(skill_points_text, (self.x + int(20 * self.PROPORTION), self.y + self.height - int(40 * self.PROPORTION)))

            # Element Labels
            for label, x, y in self.labels:
                text_surface = font.render(label, True, (255, 255, 255))
                screen.blit(text_surface, (x, y))

            # Element Stats (Levels & Probabilities)
            for element, x, y in self.stat_texts:
                level = getattr(self.player, element.lower()).level
                probability = self.player.probabilities[element]
                stat_text = font.render(f"{level}/{probability}", True, (255, 255, 255))
                screen.blit(stat_text, (x, y))

            # Draw Buttons
            for button in self.buttons:
                button.draw(screen)

            for prob_button in self.probability_buttons:
                prob_button.draw(screen)

            self.cards_upgrade_button.draw(screen)
            self.close_button.draw(screen)

    def handle_click(self, mouse_pos):
        if self.is_showing:
            for button in self.buttons:
                if button.is_clicked(mouse_pos):
                    button.handle_click()
            for prob_button in self.probability_buttons:
                if prob_button.is_clicked(mouse_pos):
                    prob_button.handle_click()
            if self.cards_upgrade_button.is_clicked(mouse_pos):
                self.cards_upgrade_button.handle_click()
            if self.close_button.is_clicked(mouse_pos):
                self.close_button.handle_click()
