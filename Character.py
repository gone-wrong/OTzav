class Character:
    def __init__(self, health=100, level=1, status_effect=None, last_element=None):
        self.health = health # default 100
        self.level = level # default 1
        self.status_effect = status_effect # default None
        self.last_element = last_element # default none

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            pass

    def heal(self, amount):
        self.health += amount

    def apply_status_effect(self, effect):
        self.status_effect = effect

    def remove_status_effect(self):
        self.status_effect = None

    def __str__(self):
        return (f"Character(Level: {self.level}, Health: {self.health}, "
                f"Last Element: {self.last_element}, Status Effect: {self.status_effect})")
