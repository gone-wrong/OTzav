class Character:
    STATUS_EFFECTS = {None, "Burning", "Zapped"}
    APPLIED_ELEMENTS = {None, "Fire", "Water", "Earth", "Lightning"}

    def __init__(self, health=100, level=1, status_effect=None, applied_element=None):
        self.health = health  # Default 100
        self.level = level  # Default 1
        self.status_effect = status_effect \
            if status_effect in self.STATUS_EFFECTS else None
        self.applied_element = applied_element \
            if applied_element in self.APPLIED_ELEMENTS else None

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0  # Ensure health doesn't go negative

    def heal(self, amount):
        self.health += amount

    def apply_status_effect(self, effect):
        if effect in self.STATUS_EFFECTS:
            self.status_effect = effect
        else:
            print(f"Invalid status effect: {effect}.")

    def remove_status_effect(self):
        self.status_effect = None

    def __str__(self):
        return (f"Character(Level: {self.level}, Health: {self.health}, "
                f"Applied Element: {self.applied_element}, "
                f"Status Effect: {self.status_effect})")
