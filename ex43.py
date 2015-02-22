# "Aliens have invaded a space ship and our hero has to go through a maze of rooms defeating them so he can escape into an escape pod to the planet below. The game will be more like a Zork or Adventure type game with text outputs and funny ways to die. The game will involve an engine that runs a map full of rooms or scenes. Each room will print its own description when the player enters it and then tell the engine what room to run next out of the map."
#
# * Map
#   - next_scene
#   - opening_scene
# * Engine
#   - play
# * Scene
#   - enter
#   * Death
#   * Central Corridor
#   * Laser Weapon Armory
#   * The Bridge
#   * Escape Pod

from sys import exit
from random import randint, choice

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map # take input as scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene() # go look in the map, in this case a_map, and since of class Map, you can call opening_scene() on it to set the current scene to the central corridor.
        last_scene = self.scene_map.next_scene('finished') # here we're doing something similar to define the "end scene" of the game as the scene we've called "finished"

        # where most of the gameplay happens:
        while current_scene != last_scene: # until you've finished the game
            next_scene_name = current_scene.enter() # run the enter() function in the current scene to see what will get returned as the name of the next scene; may depend on choices you will have to make
            current_scene = self.scene_map.next_scene(next_scene_name) # woo! once you know what the next room is that you'll be progessing to, set that to your current scene. This while loop will then loop and the enter() function of your new room will run.

        # when you've finished the game, make sure to print out the text for the last scene too!
        current_scene.enter()

class Death(Scene):

    quips = [
        "You died.",
        "Yep, you died."
    ]   

    def enter(self):
        print choice(Death.quips)
        exit(1) # exiting 1 here means "You didn't win."

class CentralCorridor(Scene):

    def enter(self):
        print "Aliens have invaded a space ship and you must go through a maze of rooms defeating them so you can escape into an escape pod to the planet below."
        print "\n"
        print "You're in the central corridor. An alien stands before you. What do you do?"
        choice = raw_input("punch or joke? >> ")
        if choice == "punch":
            print "You punch the alien, and the alien sucks you into its gooey body, where you quickly die."
            return "death"
        else:
            print "The alien begins to laugh and is completely debilitated. Congratulations! You run to the armory."
            return "laser_weapon_armory"

class LaserWeaponArmory(Scene):

    def enter(self):
        print "You're in the laser weapon armory. There's a keypad."
        choice = raw_input("What's the code? >> ")
        if choice == "1234":
            "Good job! You grab a laser weapon and sprint to the bridge."
            return "the_bridge"
        elif choice == "cheat":
            print "Let's cheat!"
            return "the_bridge"
        else:
            print "Nope, that ain't it. Try again."
            return "laser_weapon_armory"

class TheBridge(Scene):

    def enter(self):
        print "You're on the Bridge. At a distance, you see an enemy approaching."
        choice = raw_input("Shoot the enemy? y or n >> ")
        if choice == "y":
            print "Smart choice. You continue down the bridge to the escape pods."
            return "escape_pod"
        else:
            print "Well, I don't know why you wouldn't. The aliens eat you."
            return "death"

class EscapePod(Scene):

    def enter(self):
        print "There are two escape pods. Pick an escape pod."
        good_pod = str(randint(1,2))
        choice = raw_input("1 or 2? >> ")
        if choice == good_pod:
            return "finished"
        elif choice == "cheat":
            print "Let's cheat!"
            return "finished"
        else:
            return "death"

class Finished(Scene):

    def enter(self):
        print "Congratulations! You escaped!"
        return "finished"

class Map(object):

    scenes = { # dict of name_of_scene: SceneType
            "death": Death(),
            "central_corridor": CentralCorridor(),
            "laser_weapon_armory": LaserWeaponArmory(),
            "the_bridge": TheBridge(),
            "escape_pod": EscapePod(),
            "finished": Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene # takes input "central_corridor" as the start scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)
        # this converts the text name of a scene into the correct class, using the dict scenes

    def opening_scene(self):
        return self.next_scene(self.start_scene) # sets the opening scene equal to what's indicated by start_scene, in this case "central_corridor"


a_map = Map("central_corridor") # the __init__ in Map is called, which sets "central_corrider" as the start scene.
a_game = Engine(a_map) # create your game, using the map a_map that you just created as input
a_game.play() # play the game!