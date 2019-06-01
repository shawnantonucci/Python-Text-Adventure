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

def play():
    inventory = [Rock(), Dagger(), "Gold(5)", "Slice of bread"]
    print("Escape from Cave Terror!")

    while True:
        action_input = get_player_command()
        if action_input in ["n", "N", "north", "North", "^"]:
            print("Go North!")
        elif action_input in ["s", "S", "south", "South", "v"]:
            print("Go South!")
        elif action_input in ["e", "E", "east", "East", ">"]:
            print("Go East!")
        elif action_input in ["w", "W", "west", "West", "<"]:
            print("Go West!")
        elif action_input in ["i", "I", "inventory", "Inventory"]:
            print("Inventory: ")
            for item in inventory:
                print('* ' + str(item))
            # print(inventory)
        else:
            print("Invalid Action")

def get_player_command():
    return input("Action: ")


def most_powerful_weapon(inventory):
    max_damage = 0
    best_weapon = None
    for item in inventory:
        try:
            if item.damage > max_damage:
                best_weapon = item
                max_damage = item.damage
        except AttributeError:
             pass

    return best_weapon

play()
