from Character import Character
from HealthBar import HealthBar
from Figure import Figure


class Enemy(Character):
    def __init__(self, health=100, level=1):
        super().__init__(health, level)

        self.health_bar = HealthBar(x=650, y=50, max_health=self.health)
        self.figure = Figure(x=750, y=100, text="Enemy")

    def take_damage(self, amount):
        super().take_damage(amount)
        self.health_bar.update(self.health)


    def heal(self, amount):
        super().heal(amount)
        self.health_bar.update(self.health)


    def draw(self, screen):
        self.health_bar.draw(screen)
        self.figure.draw(screen)  # Draw the Enemy Figure


    def __str__(self):
        return super().__str__()

