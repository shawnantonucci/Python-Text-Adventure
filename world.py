import enemies
import random

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

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
        elif r < 0.80:
            self.enemy = enemies.ZombieDog()
        elif r < 0.95:
            self.enemy = enemies.ZombieBear()
        else:
            self.enemy = enemies.MutantCreature()

        super().__init__(x, y)

    def intro_text(self):
        if self.enemy.is_alive():
            return "A {} awaits!".format(self.enemy.name)
        else:
            return "You've defeated the {}.".format(self.enemy.name)

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
