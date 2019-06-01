class Rock:
    def __init__(self):
        self.name = "Rock"
        self.description = "A rock the size of a baseball."
        slef.damage = 5

        def __str__(self):
            return self.name

class Dagger:
    def __init__(self):
        self.name = "Dagger"
        self.description = "A small dagger. It looks pretty sharp."
        self.damage = 10

    def __str__(self):
        return self.name

class RustySword:
    def __init__(self):
        self.name = "Rusty Sword"
        self.description = "A rusty sword. Its pretty sharp still"
        slef.damage = 20

    def __str__(self):
        return self.name


def play():
    inventory = [Dagger(), "Gold(5)", "Slice of bread"]
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

play()
