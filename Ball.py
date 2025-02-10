import pygame
from Element import Fire, Earth, Water, Lightning


class Ball:
    def __init__(self):
        self.x = 671
        self.y = 760
        self.rects = []
        for i in range(10):
            self.rects.append(pygame.Rect(self.x+2*i, self.y+10*i, 60-6*i, 60-6*i))
        self.anim_state = 0
        self.anim_counter = 0
        self.anim_max_counter = 50


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
            pygame.draw.rect(screen, color, self.rects[0], border_radius=30)

        if self.anim_state == 1:
            if self.anim_counter <= self.anim_max_counter:
                x_step = (100 / self.anim_max_counter)
                y_step = (-600 / self.anim_max_counter)

                for rect in self.rects:
                    rect.x += x_step
                    rect.y += y_step

                for i in range(min(10, self.anim_counter)):
                    pygame.draw.rect(screen, color, self.rects[i], border_radius=30 - 3 * i)

                self.anim_counter += 1

            if self.anim_counter >= self.anim_max_counter:
                self.anim_state = 2

        if self.anim_state == 2:
            # Reset position after animation
            for i in range(10):
                self.rects[i].x = self.x + 2 * i
                self.rects[i].y = self.y + 10 * i
            self.anim_counter = 0


    def reset(self):
        self.used = False
        self.anim_state = 0
        self.anim_counter = 0