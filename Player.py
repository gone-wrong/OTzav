from Character import Character
from HealthBar import HealthBar

class Player(Character):
    def __init__(self, health=100, level=1):
        super().__init__(health, level)

        self.health_bar = HealthBar(x=650, y=900, max_health=self.health)

        # Player-specific elemental levels
        self.fire_level = 1
        self.earth_level = 1
        self.water_level = 1
        self.lightning_level = 1


    def take_damage(self, amount):
        super().take_damage(amount)
        self.health_bar.update(self.health)


    def heal(self, amount):
        super().heal(amount)
        self.health_bar.update(self.health)


    def draw(self, screen):
        self.health_bar.draw(screen)


    def __str__(self):
        return (super().__str__() +
                f"\nPlayer Fire Level: {self.fire_level}, Earth Level: {self.earth_level}, "
                f"Water Level: {self.water_level}, Lightning Level: {self.lightning_level}")


    def upgrade_element(self, element_type):
        if element_type == "Fire":
            self.fire_level += 1
            print(f"Fire level increased to {self.fire_level}")
        elif element_type == "Earth":
            self.earth_level += 1
            print(f"Earth level increased to {self.earth_level}")
        elif element_type == "Water":
            self.water_level += 1
            print(f"Water level increased to {self.water_level}")
        elif element_type == "Lightning":
            self.lightning_level += 1
            print(f"Lightning level increased to {self.lightning_level}")
        else:
            print("Invalid element type.")


    def get_element_level(self, element_type):
        if element_type == "Fire":
            return self.fire_level
        elif element_type == "Earth":
            return self.earth_level
        elif element_type == "Water":
            return self.water_level
        elif element_type == "Lightning":
            return self.lightning_level
        else:
            print("Invalid element type.")
            return None


