import pygame
from Button import Button


class UpgradeMenu:
    def __init__(self, player):
        self.width = 530
        self.height = 250
        self.x = 20
        self.y = 20
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.is_showing = False
        self.player = player

        # Button settings
        label_width = 40
        button_width = 40
        button_height = 40
        row_spacing = 50
        button_spacing = 50  # Space between + and x buttons (button_spacing - button_width = 10px between)

        start_x = self.x + 30
        row_y = self.y + 50

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
            button_x = label_x + label_width + 10
            probability_button_x = button_x + button_spacing
            stat_x = probability_button_x + button_spacing + 20
            label_y = row_y + (i // 2) * row_spacing

            self.labels.append((label, label_x, label_y + 8))

            self.buttons.append(Button(button_x, label_y, button_width, button_height, "+", color,
                                       lambda e=element: self.upgrade_element(e)))

            self.probability_buttons.append(Button(probability_button_x, label_y, button_width, button_height, "x", color,
                                                   lambda e=element: self.upgrade_element_probability(e)))

            self.stat_texts.append((element, stat_x, label_y + 8))


        self.cards_upgrade_button = Button(self.x + 50, row_y + 2 * row_spacing, 250, 40,
                                           "Upgrade Max Cards", (180, 180, 180), self.upgrade_cards)

        self.close_button = Button(self.x + self.width - 50, self.y + self.height - 50, 40, 40,
                                   "X", (255, 50, 50), self.hide)



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
            pygame.draw.rect(screen, (50, 50, 50), self.rect, border_radius=15)  # Menu background
            pygame.draw.rect(screen, (255, 255, 255), self.rect, 3, border_radius=15)  # White border

            # Draw labels
            font = pygame.font.Font(None, 36)

            skill_points_text = font.render(f"Skill points: {self.player.skill_points}", True, (255, 255, 255))
            screen.blit(skill_points_text, (self.x + 20, self.y + self.height - 40))

            for label, x, y in self.labels:
                text_surface = font.render(label, True, (255, 255, 255))
                screen.blit(text_surface, (x, y))

            for element, x, y in self.stat_texts:
                level = getattr(self.player, element.lower()).level
                probability = self.player.probabilities[element]
                stat_text = font.render(f"{level}/{probability}", True, (255, 255, 255))
                screen.blit(stat_text, (x, y))

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