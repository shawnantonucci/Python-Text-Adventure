def play():

    inventory = ["Dagger", "Gold(5)", "Slice of bread"]

    print("Escape from Cave Terror!")
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
        print(inventory)
    else:
        print("Invalid Action")

def get_player_command():
    return input("Action: ")

play()
