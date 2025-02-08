from Element import Element, Fire, Earth, Water, Lightning

class Character:
    STATUS_EFFECTS = {None, "Burning", "Zapped"}
    APPLIED_ELEMENTS = {None, Fire, Earth, Water, Lightning}
    REACTIONS = {
        frozenset([Fire, Earth]): "Burning",
        frozenset([Fire, Lightning]): "Explode",
        frozenset([Water, Earth]): "Bloom",
        frozenset([Water, Lightning]): "Zapped"
    }

    def __init__(self, health=100, level=1):
        self.max_health = health # Default 100
        self.health = health
        self.level = level  # Default 1
        self.status_effect = None
        self.applied_element = None
        self.prev_applied_element = None
        self.reaction_level = 0


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


    def apply_status_effect(self, effect):
        if effect in self.STATUS_EFFECTS:
            self.status_effect = effect
        else:
            print(f"Invalid status effect: {effect}.")


    def remove_status_effect(self):
        self.status_effect = None


    def apply_element(self, element):
        #if isinstance(element, tuple(self.APPLIED_ELEMENTS))
        if isinstance(element, Element):
            self.prev_applied_element = self.applied_element
            self.applied_element = element
            self.trigger_reaction()
        else:
            print(f"Invalid applied element: {element}.")


    def remove_applied_element(self):
        self.applied_element = None


    def trigger_reaction(self):
        if self.prev_applied_element and self.applied_element:
            reaction = self.REACTIONS.get(frozenset([type(self.prev_applied_element), type(self.applied_element)]))

            if reaction:
                self.reaction_level = self.prev_applied_element.level + self.applied_element.level
                self.prev_applied_element = None
                self.applied_element = None
                self.status_effect = reaction
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


    def handle_burning(self):
        pass

    def handle_explode(self):
        pass

    def handle_bloom(self):
        pass

    def handle_zapped(self):
        pass


