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

    def attack_character(self, character):
        super().damage_character(character)
        character.apply_element(self)


class Earth(Element):
    def __init__(self):
        super().__init__()

    def attack_character(self, character):
        super().damage_character(character)
        character.apply_element(self)


class Water(Element):
    def __init__(self):
        super().__init__()

    def attack_character(self, character):
        super().damage_character(character)
        character.apply_element(self)


class Lightning(Element):
    def __init__(self):
        super().__init__()

    def attack_character(self, character):
        super().damage_character(character)
        character.apply_element(self)

