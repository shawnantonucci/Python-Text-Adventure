
class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
         return self.name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A rock the size of a baseball."
        self.damage = 5
        self.value = 1

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger. It looks pretty sharp."
        self.damage = 10
        self.value = 20

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "A rusty sword. Its pretty sharp still"
        self.damage = 20
        self.value = 100

# Consumables
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} Hp)".format(self.name, self.healing_value)

class PlainBread(Consumable):
    def __init__(self):
        self.name = "Plain slice of bread"
        self.healing_value = 10
        self.value = 12

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Patch"
        self.healing_value = 50
        self.value = 60
