import pygame


class Card:
    def __init__(self, card_type, x, y, color, player):
        self.card_type = card_type
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, 100, 150)
        self.player = player
        self.anim_state = 0
        self.anim_counter = 0
        self.anim_max_counter = 50
        self.used = False  # The same card can't be clicked more than once per turn

    def draw(self, screen):
        if self.anim_state == 0:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)

        if self.anim_state == 1:
            if self.anim_counter <= self.anim_max_counter / 2:
                x_step = (50 / (self.anim_max_counter / 2))
                width_step = (100 / (self.anim_max_counter / 2))

                self.rect.x += x_step
                self.rect.width -= width_step
                pygame.draw.rect(screen, (10, 10, 10), self.rect, border_radius=10)
            else:
                x_step = (50 / (self.anim_max_counter / 2))
                width_step = (100 / (self.anim_max_counter / 2))

                self.rect.x -= x_step
                self.rect.width += width_step
                pygame.draw.rect(screen, self.color, self.rect, border_radius=10)
            self.anim_counter += 1
            if self.anim_counter == self.anim_max_counter:
                self.anim_state = 2
        if self.anim_state == 2:
            pygame.draw.rect(screen, self.color, self.rect, border_radius=10)


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


