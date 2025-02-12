import pygame
from Element import Fire, Earth, Water, Lightning


class Ball:
    def __init__(self, PROPORTION):
        self.PROPORTION = PROPORTION
        self.x = 571 * PROPORTION
        self.y = 760 * PROPORTION
        self.size = 60 * PROPORTION
        self.border_radius = int(30 * PROPORTION)

        self.rects = []
        for i in range(10):
            rect_x = self.x + (2 * i * PROPORTION)
            rect_y = self.y + (10 * i * PROPORTION)
            rect_width = self.size - (6 * i * PROPORTION)
            rect_height = self.size - (6 * i * PROPORTION)
            self.rects.append(pygame.Rect(rect_x, rect_y, rect_width, rect_height))

        self.anim_state = 0
        self.anim_counter = 0
        self.anim_max_counter = 50  # Animation frames

    def draw(self, screen, element):
        if element is None:
            return
        if isinstance(element, Fire):
            color = (200, 100, 100)
        elif isinstance(element, Earth):
            color = (100, 200, 100)
        elif isinstance(element, Water):
            color = (100, 100, 200)
        elif isinstance(element, Lightning):
            color = (200, 200, 100)
        else:
            color = (10,10,10)

        if self.anim_state == 0:
            pygame.draw.rect(screen, color, self.rects[0], border_radius=self.border_radius)

        if self.anim_state == 1:
            if self.anim_counter <= self.anim_max_counter:
                # Dynamically adjust step size based on `PROPORTION`
                x_step = (200 * self.PROPORTION / self.anim_max_counter)
                y_step = (-600 * self.PROPORTION / self.anim_max_counter)

                for rect in self.rects:
                    rect.x += x_step
                    rect.y += y_step

                for i in range(min(10, self.anim_counter)):
                    border = max(3, self.border_radius - (3 * i * self.PROPORTION))
                    pygame.draw.rect(screen, color, self.rects[i], border_radius=self.border_radius - int(3 * i * self.PROPORTION))

                self.anim_counter += 1

            if self.anim_counter >= self.anim_max_counter:
                self.anim_state = 2

        if self.anim_state == 2:
            # Reset position after animation
            for i in range(10):
                self.rects[i].x = self.x + (2 * i * self.PROPORTION)
                self.rects[i].y = self.y + (10 * i * self.PROPORTION)
            self.anim_counter = 0

    def reset(self):
        self.used = False
        self.anim_state = 0
        self.anim_counter = 0
