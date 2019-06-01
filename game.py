
from player import Player
import world


def play():
    print("\n Escape from Cave Terror!")
    player = Player()
    while True:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player) # New line
        action_input = get_player_command()
        if action_input in ['n', 'N', 'north', 'North']:
            player.move_north()
        elif action_input in ['s', 'S', 'south', 'South']:
            player.move_south()
        elif action_input in ['e', 'E', 'east', 'East']:
            player.move_east()
        elif action_input in ['w', 'W', 'west', 'West']:
            player.move_west()
        elif action_input in ['i', 'I', 'inventory', 'Inventory']:
            player.print_inventory()
        elif action_input in ["a", "A", 'attack', 'Attack']:
            player.attack()
        elif action_input in ["h", "H", 'heal', 'Heal']:
            player.heal()
        else:
            print("Invalid action!")


def get_player_command():
    return input('Action: ')


play()
