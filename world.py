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

world_map = [
    [None,VictoryTile(1,0),None],
    [None,EnemyTile(1,1),None],
    [ForestTrailTile(0,2),StartTile(1,2),ForestTrailTile(2,2)],
    [None,EnemyTile(1,3),None]
]


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None
