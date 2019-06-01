class Enemy:
     def __init__(self):
         raise NotImplementedError("Do not create raw Enemy objects")

     def __str__(self):
         return self.name

     def is_alive(self):
        return self.hp > 0

class Zombie(Enemy):
    def __init__(self):
        self.name = "Zombie"
        self.hp = 10
        self.damage = 2

class ZombieDog(Enemy):
    def __init__(self):
        self.name = "Zombie Dog"
        self.hp = 20
        self.damage = 4

class ZombieBear(Enemy):
    def __init__(self):
        self.name = "Zombie Bear"
        self.hp = 40
        self.damage = 8

class MutantCreature(Enemy):
    def __init__(self):
        self.name = "Mutant"
        self.hp = 80
        self.damage = 10
