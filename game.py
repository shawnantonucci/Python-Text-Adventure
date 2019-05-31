def play():
    print("Escape from Cave Terror!")
    action_input = get_player_command()
    if action_input == "n" or action_input == "N" or action_input == "North" or action_input == "north":
        print("Go North!")
    elif action_input == "s" or action_input == "S" or action_input == "South" or action_input == "south":
        print("Go South!")
    elif action_input == "e" or action_input == "E" or action_input == "East" or action_input == "east":
        print("Go East!")
    elif action_input == "w" or action_input == "W" or action_input == "West" or action_input == "west":
        print("Go West!")
    else:
        print("Invalid Action")

def get_player_command():
    return input("Action: ")

play()
