import enemies
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
    def intro_text(self):
        return """
        You escape the forest alive!
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

    # def intro_text(self):
    #     if self.enemy.is_alive():
    #         return "A {} awaits!".format(self.enemy.name)
    #     else:
    #         return "You've defeated the {}.".format(self.enemy.name)
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print(Fore.RED + "Enemy does {} damage. You have {} HP remaining.".
                  format(self.enemy.damage, player.hp))
            print(Style.RESET_ALL)

world_dsl = """
|     |VT|     |
|     |EN|     |
|EN|ST|EN|
|     |EN|     |
"""


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
                            "     ": None}


world_map = []


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
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
