#Fire + Lightning -> Explode
#Fire + Earth -> Burning
#Water + Lightning -> Zapped
#Water + Earth -> Bloom

class Element:
    def __init__(self, level=1):
        self.level = level # default 1
        self.damage = 5 # default 5


    def damage_character(self, character):
        damage_dealt = self.damage * self.level
        character.take_damage(damage_dealt)



class Fire(Element):
    def __init__(self):
        super().__init__()

    def burn_character(self, character):
        pass

    def explode_character(self, character):
        pass

    def attack_character(self, character):
        super().damage_character(character)
        if character.applied_element == "Earth":
            self.burn_character(character)
        elif character.applied_element == "Lightning":
            self.explode_character(character)
        else:
            character.applied_element = "Fire"


