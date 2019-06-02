from collections import OrderedDict
from player import Player
import world

def play():
    print("\n Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player) # New line
        choose_action(room, player)


        # if player.move_north:
        #     actions["n"] = player.move_north
        #     actions["N"] = player.move_north
        #     print("n")
        # elif player.move_south:
        #     actions["s"] = player.move_south
        #     actions["S"] = player.move_south
        #     print("s")
        # elif player.move_east:
        #     actions["e"] = player.move_east
        #     actions["E"] = player.move_east
        #     print("e")
        # elif player.move_west:
        #     actions["w"] = player.move_west
        #     actions["W"] = player.move_west
        #     print("w")
        # elif player.inventory:
        #     actions["i"] = player.print_inventory
        #     actions["I"] = player.print_inventory
        #     print("i: View inventory")
        # elif player.attack:
        #     actions["a"] = player.attack
        #     actions["A"] = player.attack
        #     print("a: Attack")
        # elif player.heal:
        #     actions["h"] = player.heal
        #     actions["H"] = player.heal
        #     print("h: Heal")
        # else:
        #     print("Invalid action!")

def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("Invalid action!")

def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, "i", player.print_inventory, "Display inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, "a", player.attack, "Attack")
    else:
        if world.tile_at(room.x, room.y - 1):
            action_adder(actions, "n", player.move_north, "Go north")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, "s", player.move_south, "Go south")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, "e", player.move_east, "Go east")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, "w", player.move_west, "Go west")
    if player.hp < 100:
        action_adder(actions, "h", player.heal, "Heal")

    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}: {}".format(hotkey, name))

play()
