import enemies
import npc
import random
from colorama import init, Fore, Back, Style

init()

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = None

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        pass

class StartTile(MapTile):
    def intro_text(self):
        return """
        You wake up in the middle of the woods. It's pretty dark out
        and you are soaking wet! You seem lost in direction and
        have no idea where you are. Good thing you never leave
        the house unprepared! You reach in your pocket and pull
        out a golden compass.
        """

class ForestTrailTile(MapTile):
    def intro_text(self):
        return """
        The tree branches are swaying, and the crickets are playing
        a song in the background. The trail is barly visable with the
        full moon shining your path.
        """

class VictoryTile(MapTile):
    def modify_player(self, player):
        player.victory = True

    def intro_text(self):
        return """
        You escape the quarantine zone!
        """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = enemies.Zombie()
            self.alive_text = "\nA zombie sets its sights on you and runs at you! \n"
            self.dead_text = "\nThe zombies drops to the ground. \n"
        elif r < 0.80:
            self.enemy = enemies.ZombieDog()
            self.alive_text = "\nA zombie dog growls and lunges at you! \n"
            self.dead_text = "\nThe zombies drops to the ground. \n"
        elif r < 0.95:
            self.enemy = enemies.ZombieBear()
            self.alive_text = """\nA zombie bear is sitting down eating a human
            a human corpse. It turns his head around and makes eye contact.
            The zombie bear lunges at you. \n
            """
            self.dead_text = "\nThe zombies bear drops to the ground shaking everything. \n"
        else:
            self.enemy = enemies.MutantCreature()
            self.alive_text = """\nA mutant zombie that is times the size of a regular human
            slams onto the ground in front of you. \n
            """
            self.dead_text = """\nThe mutant starts to grow 6 times the size and explodes.
            blood and flesh fly everywhere. \n
            """

        super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(Fore.RED + "Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))
            print(Style.RESET_ALL)

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        while True:
            user_input = input("Choose an item or press Q to exit: ")
            if user_input in ["Q", "q"]:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's to exspensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ["S", "s"]:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        A creepy old man hidden in an alley hollers at you to come
        see what he has for sale.
        """

class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return """
            Nothing here is of any interest to you.
            """
        else:
            return """
            Someone left some gold laying around! You pick it up.
            """

world_dsl = """
|EN|EN|VT|EN|EN|
|EN|     |     |     |EN|
|EN|FG|EN|     |TT|
|TT|     |ST|FG|EN|
|FG|     |EN|     |FG|
"""

world_map = []

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

tile_type_dict = {"VT": VictoryTile,
                            "EN": EnemyTile,
                            "ST": StartTile,
                            "FG": FindGoldTile,
                            "TT": TraderTile,
                            "     ": None}


world_map = []

start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
