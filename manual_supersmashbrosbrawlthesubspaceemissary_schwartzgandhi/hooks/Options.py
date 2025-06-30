# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class WorldStructure(Choice):
    """Determines how you gain access to a level.
    Stages: The stages themselves are shuffled into the pool and recieving the item will grant you access to it.
    Characters: Stages are locked by the characters that open every level and having every charcter will grant you access to it.
    (ie: recieving Lucas gives you The Ruined Zoo, recieving Snake gives you Battleship Halberd Interior, ect.)"""
    display_name = "World Structure"
    option_stages = 0
    option_characters = 1
    default = 1

class PokemonTrainerBehaviour(Choice):
    """Determines how Pokémon Trainer is accounted for in logic.
    Solo Trainer: Just Pokémon Trainer is shuffled and will have access to every Pokémon.
    Require Trainer and Pokémon: Pokémon Trainer and his three Pokémon are shuffled into the pool separately, logic will require the Trainer as well as one Pokémon.
    Progressive Trainer: Shuffle 4 Progressive Trainers into the pool, logic will require the Trainer as well as one Pokémon
    (Progressive Trainer is in the following order: Pokémon Trainer, Squirtle, Ivysaur, Charizard)
    """
    display_name = "Pokémon Trainer Behaviour"
    option_solo_trainer = 0
    option_require_trainer_and_pokemon = 1
    option_progressive_trainer = 2
    default = 0

class SamusBehaviour(Choice):
    """Determines how Samus is accounted for in logic.
    Any Samus: Having either Samus or Zero Suit Samus will allow you to enter all of her respective levels.
    Separate Samus: Logic will require either Samus or Zero Suit Samus for her respective levels.
    Progressive Samus: Shuffles 2 Progressive Samuses into the pool, Logic will behave the same as Separate Samus.
    (Progressive Samus is in the following order: Zero Suit Samus, Samus)
    """
    display_name = "Samus Behaviour"
    option_any_samus = 0
    option_separate_samus = 1
    option_progressive_samus = 2
    default = 0

class ZeldaBehaviour(Choice):
    """Determines how Zelda and Sheik is accounted for in logic.
    Any Zelda: Having either Zelda or Sheik will allow you to enter all of her respective levels.
    Separate Zelda: Logic will require either Zelda or Sheik for her respective levels.
    Progressive Zelda: Shuffles 2 Progressive Zeldas into the pool, Logic will behave the same as Separate Zelda.
    (Progressive Zelda is in the following order: Zelda, Sheik)
    """
    display_name = "Zelda Behaviour"
    option_any_zelda = 0
    option_separate_zelda = 1
    option_progressive_zelda = 2
    default = 0

class SecretCharcterShuffle(Toggle):
    """Shuffles Toon Link, Jigglypuff, Wolf, and their respective checks into the game."""
    display_name = "Shuffle Secret Characters"
    default = False

class HoardeShuffle(Toggle):
    """Send a check whenever you complete a hoarde battle"""
    display_name = "Shuffle Hoarde Battles"
    default = False

class GreatMazeRequirements(Choice):
    """Determines how you want The Great Maze to be unlocked.
    Open: having any fighter will unlock The Great Maze.
    Minimum Fighters: having Luigi, Ness, King Dedede, Bowser and Kirby will unlock the Great Maze.
    Percentage of Fighters: having a specified amount of fighters will unlock The Great Maze.
    Minimum Plus Percentage: having Luigi, Ness, King Dedede, Bowser, Kirby, plus an specified amount of fighters will unlock The Great Maze.
    All Fighters: EVERYONE IS HERE!
    """
    display_name = "Great Maze Requirements"
    option_open = 0
    option_minimum_fighters = 1
    option_percentage_of_fighters = 2
    option_minimum_plus_percentage = 3
    option_all_fighters = 4
    default = 1

class GreatMazeFighterPercentage(Range):
    """Determines the ammount of fighters you need to enter The Great Maze.
    This is only used if you have Percentage of Fighters or Minimum Plus Percentage enabled in Great Maze Requirements.
    Keep in mind that this is a percentage of all the fighters you have shuffled.
    """
    display_name = "Great Maze Fighter Percentage"
    range_start = 0
    range_end = 100
    default = 50

class TabuuRequirements(Choice):
    """Determines how you want Tabuu to be unlocked.
    Open: You can fight Tabuu as soon has you have access to The Great Maze.
    Percentage of Fighters: have a specified amount of fighters be required to unlock Tabuu.
    Boss Hunt: Defeat a specified amount of bosses in other levels to unlock Tabuu.
    Fighters and Bosses: A combination of the previous two.
    """
    display_name = "Tabuu Requirements"
    option_open = 0
    option_percentage_of_fighters = 1
    option_boss_hunt = 2
    option_fighters_and_bosses = 3
    default = 1

class TabuuFighterPercentage(Range):
    """Determines the ammount of fighters you need to fight Tabuu.
    This is only used if you have Percentage of Fighters or Fighters and Bosses enabled in Tabuu Requirements.
    Keep in mind that this is a percentage of all the fighters you have shuffled.
    """
    display_name = "Tabuu Fighter Percentage"
    range_start = 0
    range_end = 100
    default = 80

class TabuuBossHunt(Range):
    """Determines the amount of bosses that must be defeated to fight Tabuu.
    This is only used if you have Boss Hunts or Fighters and Bosses enabled.
    """
    display_name = "Tabuu Boss Ammount"
    range_start = 0
    range_end = 8
    default = 4

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options.update(
        {
            'world_structure': WorldStructure,
            'trainer_behaviour': PokemonTrainerBehaviour,
            'samus_behaviour': SamusBehaviour,
            'zelda_behaviour': ZeldaBehaviour,
            'secret_character_shuffle': SecretCharcterShuffle,
            'hoarde_shuffle': HoardeShuffle,
            'great_maze_requirements': GreatMazeRequirements,
            'maze_fighter_percentage': GreatMazeFighterPercentage,
            'tabuu_requirements': TabuuRequirements,
            'tabuu_fighter_percentage': TabuuFighterPercentage,
            'tabuu_boss_amount': TabuuBossHunt
        }
    )
    return options