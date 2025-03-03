from Character import Character
from HealthBar import HealthBar
from Figure import Figure
from Element import Fire, Earth, Water, Lightning  # Import Element Classes


class Player(Character):
    def __init__(self, health=100, level=1, PROPORTION=1):
        super().__init__(health, level, Figure(x=750, y=720, text="Player", PROPORTION=PROPORTION), HealthBar(x=650, y=900, max_health=100, PROPORTION=PROPORTION))


        # Player-specific elemental abilities as instances of the Element classes
        self.fire = Fire()
        self.earth = Earth()
        self.water = Water()
        self.lightning = Lightning()
        self.probabilities = {"Fire": 2, "Earth": 2, "Lightning": 2, "Water": 2}
        self.max_cards_flipped = 2
        self.skill_points = 0


    def take_damage(self, amount):
        super().take_damage(amount)
        # self.health_bar.update(self.health)
        # self.figure.set_damage_taken(f"-{amount}")


    def heal(self, amount):
        super().heal(amount)
        # self.health_bar.update(self.health)
        # self.figure.set_status_effect(f"+{amount}", "Bloom")


    def draw(self, screen):
        self.health_bar.draw(screen)
        self.figure.draw(screen)  # Draw the Player Figure


    def __str__(self):
        return (super().__str__() +
                f"\nFire Level: {self.fire.level}, Earth Level: {self.earth.level}, "
                f"Water Level: {self.water.level}, Lightning Level: {self.lightning.level}")


    def upgrade_max_cards_flipped(self):
        self.max_cards_flipped += 1
        print(f"Upgraded max_cards_flipped to {self.max_cards_flipped}")


    def upgrade_element(self, element_type):
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


    def upgrade_element_probability(self, element_type):
        if element_type in self.probabilities:
            self.probabilities[element_type] += 1
            print(f"New probabilities: {self.probabilities}")
        else:
            print("Invalid element type.")



    def player_attack(self, enemy, element):
        enemy.apply_element(element) # Applies element to the enemy and checks for reactions
        element.damage_character(enemy) # Deals elements damage to enemy




