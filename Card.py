import pygame


class Card:
    def __init__(self, card_type, x, y, color, player, PROPORTION):
        self.PROPORTION = PROPORTION
        self.card_type = card_type
        self.x = x * PROPORTION
        self.y = y * PROPORTION
        self.width = 100 * PROPORTION
        self.height = 150 * PROPORTION
        self.color = color
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.player = player
        self.anim_state = 0
        self.anim_counter = 0
        self.anim_max_counter = 50
        self.used = False  # The same card can't be clicked more than once per turn
        self.border_radius = int(10 * self.PROPORTION)


    def draw(self, screen):
        if self.anim_state == 0:
            pygame.draw.rect(screen, (10, 10, 10), self.rect, border_radius=self.border_radius)

        if self.anim_state == 1:
            x_step = ((self.width / 2) / (self.anim_max_counter / 2))
            width_step = (self.width / (self.anim_max_counter / 2))
            if self.anim_counter <= self.anim_max_counter / 2:
                self.rect.x += x_step
                self.rect.width -= width_step
                pygame.draw.rect(screen, (10, 10, 10), self.rect, border_radius=self.border_radius)
            else:
                self.rect.x -= x_step
                self.rect.width += width_step
                pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)
            self.anim_counter += 1
            if self.anim_counter == self.anim_max_counter:
                self.anim_state = 2
        if self.anim_state == 2:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=self.border_radius)


    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos) and not self.used


    def on_click(self):
        if not self.used:
            print(f"Card '{self.card_type}' was clicked")
            self.used = True
            self.anim_state = 1


    def reset_used(self):
        self.used = False
        self.anim_state = 0
        self.anim_counter = 0


