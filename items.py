
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


class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger. It looks pretty sharp."
        self.damage = 10

class RustySword(Weapon):
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "A rusty sword. Its pretty sharp still"
        self.damage = 20
