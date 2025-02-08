from Character import Character
from HealthBar import HealthBar
from Figure import Figure
from Element import Fire, Earth, Water, Lightning  # Import Element Classes


class Player(Character):
    def __init__(self, health=100, level=1):
        super().__init__(health, level)

        self.health_bar = HealthBar(x=650, y=900, max_health=self.health)
        self.figure = Figure(x=750, y=720, text="Player")

        # Player-specific elemental abilities as instances of the Element classes
        self.fire = Fire()
        self.earth = Earth()
        self.water = Water()
        self.lightning = Lightning()


    def take_damage(self, amount):
        super().take_damage(amount)
        self.health_bar.update(self.health)


    def heal(self, amount):
        super().heal(amount)
        self.health_bar.update(self.health)


    def draw(self, screen):
        self.health_bar.draw(screen)
        self.figure.draw(screen)  # Draw the Player Figure


    def __str__(self):
        return (super().__str__() +
                f"\nFire Level: {self.fire.level}, Earth Level: {self.earth.level}, "
                f"Water Level: {self.water.level}, Lightning Level: {self.lightning.level}")


    def upgrade_element(self, element_type):
        """Upgrades the level of a specific element instance."""
        if element_type == "Fire":
            self.fire.level += 1
            print(f"Fire level increased to {self.fire.level}")
        elif element_type == "Earth":
            self.earth.level += 1
            print(f"Earth level increased to {self.earth.level}")
        elif element_type == "Water":
            self.water.level += 1
            print(f"Water level increased to {self.water.level}")
        elif element_type == "Lightning":
            self.lightning.level += 1
            print(f"Lightning level increased to {self.lightning.level}")
        else:
            print("Invalid element type.")


    def player_attack(self, enemy, element):
        enemy.apply_element(element) # Applies element to the enemy and checks for reactions
        element.damage_character(enemy) # Deals elements damage to enemy




