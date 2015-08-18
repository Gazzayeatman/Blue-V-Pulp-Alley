__author__ = 'gazza'
import os
import cmd
from league_model import LeagueModel
import sys

class Console(cmd.Cmd):

    lm = LeagueModel()

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "=>>"
        self.intro = "Welcome to Burger King, Please place your order"

    ## Commands are below

    def do_exit(self, args):
        'Exits the program'
        return -1

    def do_createLeague(self,args):
        '''createLeague [LeagueName]
        This command creates a league with the given name.
        '''
        self.lm.set_abilities_file(self.lm.read_file("abilities.txt")) #change to handle file systems
        self.lm.add_league(args)
        print(args + " created")

    def do_deleteLeague(self,args):
        '''
        deleteLeague [LeagueName]
        This command will delete you specify with a league name
        '''
        print("League deleted (Not actually shhhh)")

    def do_displayLeague(self,args):
        '''
        displayLeague
        This command will display ???
        '''
        print("Leagues go here")

    def do_displayAbilities(self,args):
        '''
        displayAbilities
        This command will display all the abilities of the current league
        '''
        print(self.lm.get_all_abilities()) #Update this plz

    def do_addCharacter(self,*args):
        '''
        addCharacter [CharacterName] [CharacterType] [Health] [Brawl] [Shoot] [Dodge] [Might] [Finesse] [Cunning]
        [Ability 1] [Ability 2] [Ability 3]
        --------------------------------------------------------------------------------------------------------
        This command adds a character to the current league.
        Your league starts with 10 roster slots.
        --------------------------------------------------------------------------------------------------------
        [Character Name] = The character's name
        [CharacterType] = Can be either 'Leader' 'SideKick' 'Ally' or 'Follower', You can only have ONE leader

        Skills. See below for examples on how to use this argument

        [Health] = A number used to represent your characters overall condition
        [Brawl] = Represents a character's overall hand-to-hand combat prowess
        [Shoot] = Indicates a character's combat effectiveness with all manner of ranged weapons
        [Dodge] = Determines the character's ability to avoid enemy attacks, perils, and other dangers.
        [Might] = Indicates a character's power, fitness and general athleticism
        [Finesse] = measures the character's co ordination, awareness and ability to manipulate
        [Cunning] = Represents a character's knowledge, resolve and ability to solve complicated problems.

        Skill levels by type

        Leader
            MUST have a health value of d10
            Select four skills to start at 3 dice and two skills to start at 2 dice
            Select four skills to start at d10 and two skills to start at d8
            Can choose 3 abilities at any level
        SideKick
            MUST have a health value of d8
            Select three skills to start at 3 dice and three skills to start at 2 dice
            Select three skills to start at d10 and three skills to start at d8
            Can choose 2 abilities at level 1 to 3
            Uses three roster slots
        Ally
            MUST have a health value of d6
            Select two skills to start at 3 dice and four skills to start at 2 dice
            All skills start at d6
            Can choose 1 ability at level 1 to 2
            Uses two roster slots
        Follower
            MUST have a health value of d6
            ALL skills must be 1d6
            Can choose 1 ability at level 1
            Uses one roster slot

        Example
            addCharacter Testing Leader d10 3d8 3d10 3d10 2d8 3d10 2d10 Mighty Brash Crafty
        '''
        league = self.lm.get_current_league()
       # if args.__len__ < 8:
        #    print("You need to make sure all fields are filled")
        #else:
        league.add_character(args[0],args[1],args[2],args[3],args[4],args[5],args[6],args[7],args[8],args[9],
                                 args[10],args[11], args[12])
        print(league.find_character(args[0]).name)

    def default(self, line):
        """Called on an input line when the command prefix is not recognized.
        In that case we execute the line as Python code.
        """
        try:
            exec(line) in self._locals, self._globals
        except Exception as e:
            print (e.__class__, ":", e)

if __name__ == '__main__':
        console = Console()
        console.cmdloop()