from Element import Element, Fire, Earth, Water, Lightning
import random


class Character:
    STATUS_EFFECTS = {None, "Burning", "Bloom"}
    APPLIED_ELEMENTS = {None, Fire, Earth, Water, Lightning}
    REACTIONS = {
        frozenset([Fire, Earth]): "Burning",
        frozenset([Fire, Lightning]): "Explode",
        frozenset([Water, Earth]): "Bloom",
        frozenset([Water, Lightning]): "Zapped"
    }
    OPPOSING_PAIRS = {
        (Fire, Water), (Water, Fire),  # Fire x Water
        (Lightning, Earth), (Earth, Lightning)  # Lightning x Earth
    }

    def __init__(self, health=100, level=1):
        self.max_health = health # Default 100
        self.health = health
        self.level = level  # Default 1
        self.status_effect = None
        self.status_effect_duration = 0
        self.applied_element = None
        self.prev_applied_element = None
        self.next_reaction_level = 0
        self.current_reaction_level = 0
        self.skip_turn = False


    def __str__(self):
        return (f"Character Max Health: {self.max_health}, Level: {self.level}, "
                f"Current Health: {self.health}, "
                f"Applied Element: {self.applied_element}, "
                f"Previous Applied Element: {self.prev_applied_element}, "
                f"Status Effect: {self.status_effect}")


    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0


    def heal(self, amount):
        self.health += amount


    def apply_element(self, element):
        if isinstance(element, Element):
            if self.applied_element and (type(self.applied_element), type(element)) in self.OPPOSING_PAIRS:
                print(f"Opposing elements met resetting next_reaction_level.")
                self.next_reaction_level = 0

            self.prev_applied_element = self.applied_element
            self.applied_element = element
            self.next_reaction_level += element.level + element.temp_level
            self.trigger_reaction()
        else:
            print(f"Invalid applied element: {element}.")


    def remove_applied_element(self):
        self.applied_element = None


    def trigger_reaction(self):
        if self.prev_applied_element and self.applied_element:
            reaction = self.REACTIONS.get(frozenset([type(self.prev_applied_element), type(self.applied_element)]))

            if reaction:
                self.current_reaction_level = self.next_reaction_level
                self.next_reaction_level = 0
                self.prev_applied_element = None
                self.applied_element = None
                print(f"Triggered reaction: {reaction}")
                if reaction == "Burning":
                    self.handle_burning()
                elif reaction == "Explode":
                    self.handle_explode()
                elif reaction == "Bloom":
                    self.handle_bloom()
                elif reaction == "Zapped":
                    self.handle_zapped()
            else:
                print("No reaction triggered.")

    """
        F,E,L,W lvl 5 (reaction lvl 10) = 5(BaseDamage) * 5(ElLevel) = 25 normal attack  
        Burning lvl 10 = 5(BD) * 10(reaction lvl) // 2 = 25 damage over 2 turns = 12 and 12 -> 24 total
        Explode lvl 10 = 5(BD) * 10(RL) // 3 = 16 damage
        Bloom lvl 10 = 5(BD) * 10(RL) // 3 = 16 heal
        Zapped lvl 10 = 5(BD) * 10(RL) // 2 = 25% chance to skip turn max 50%
    """

    def handle_burning(self):
        self.status_effect = "Burning"
        self.status_effect_duration = 2
        print(f"Set Burning status effect for two turns")


    def handle_explode(self):
        explode_damage = self.current_reaction_level * 5 // 3
        print(f"Exploding for {explode_damage} damage.")
        self.take_damage(explode_damage)


    def handle_bloom(self):
        self.status_effect = "Bloom"
        self.status_effect_duration = 1
        print(f"Set Bloom status effect for one turn")


    def handle_zapped(self):
        zap_chance = 5 * self.current_reaction_level // 2
        zap_chance = min(zap_chance, 50) / 100
        random_res = random.random()
        self.skip_turn = random.random() < zap_chance
        print(f"Zapped with {zap_chance}, reaction level {self.current_reaction_level}, random_res = {random_res} -> skip_turn set to {self.skip_turn}")


    def handle_status_effect(self, player):
        if self.status_effect:
            self.status_effect_duration -= 1
            if self.status_effect == "Burning":
                burn_damage = 5 * self.current_reaction_level // 4
                self.take_damage(burn_damage)
                print(f"Burned for {burn_damage} damage, reaction level {self.current_reaction_level}.")
            elif self.status_effect == "Bloom":
                bloom_heal = 5 * self.current_reaction_level // 3
                player.heal(bloom_heal)
                print(f"Bloom recovered {bloom_heal} health, reaction level {self.current_reaction_level}. ")
            else:
                print(f"Invalid status effect: {self.status_effect}.")

        if self.status_effect_duration == 0:
            self.status_effect = None
