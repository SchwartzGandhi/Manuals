from typing import Optional
from Options import OptionError
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, get_option_value
from BaseClasses import MultiWorld, CollectionState

import re

def Check_Ruins_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    red_requirement = get_option_value(multiworld, player, "trainer_behaviour")
    if red_requirement == 0:
        red = "|Pokémon Trainer|"
    elif red_requirement == 1:
        red = "(|Pokémon Trainer| AND (|Squirtle| OR |Ivysaur| OR |Charizard|))"
    elif red_requirement == 2:
        red = "|Progressive Pokémon Trainer: 2|"
    else:
        raise OptionError("Option Pokémon Trainer Behaviour is not set to a valid number.")
    return f"|Lucas| AND {red}"

def Check_Facility_1_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    samus_requirement = get_option_value(multiworld, player, "samus_behaviour")
    if samus_requirement == 0:
        samus = "|@Samus Aran|"
    elif samus_requirement == 1:
        samus = "|Zero Suit Samus|"
    elif samus_requirement == 2:
        samus = "|Progressive Samus: 1|"
    else:
        raise OptionError("Option Samus Behaviour is not set to a valid number.")
    return samus

def Check_Facility_2_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    samus_requirement = get_option_value(multiworld, player, "samus_behaviour")
    if samus_requirement == 0:
        samus = "|@Samus Aran|"
    elif samus_requirement == 1:
        samus = "|Zero Suit Samus|"
    elif samus_requirement == 2:
        samus = "|Progressive Samus: 1|"
    else:
        raise OptionError("Option Samus Behaviour is not set to a valid number.")
    return f"{samus} AND |Pikachu|"

def Check_Bomb_Factory_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    samus_requirement = get_option_value(multiworld, player, "samus_behaviour")
    if samus_requirement == 0:
        samus = "|@Samus Aran|"
    elif samus_requirement == 1:
        samus = "|Samus|"
    elif samus_requirement == 2:
        samus = "|Progressive Samus: 2|"
    else:
        raise OptionError("Option Samus Behaviour is not set to a valid number.")
    return f"{samus} AND |Pikachu|"

def Check_Halberd_Exterior_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    zelda_requirement = get_option_value(multiworld, player, "zelda_behaviour")
    if zelda_requirement == 0:
        zelda = "|@Zelda/Sheik|"
    elif zelda_requirement == 1:
        zelda = "|Sheik|"
    elif zelda_requirement == 2:
        zelda = "|Progressive Zelda: 2|"
    else:
        raise OptionError("Option Zelda Behaviour is not set to a valid number.")
    return f"|Peach| AND {zelda}"

def Check_Halberd_Bridge_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    zelda_requirement = get_option_value(multiworld, player, "zelda_behaviour")
    if zelda_requirement == 0:
        zelda = "|@Zelda/Sheik|"
    elif zelda_requirement == 1:
        zelda = "|Sheik|"
    elif zelda_requirement == 2:
        zelda = "|Progressive Zelda: 2|"
    else:
        raise OptionError("Option Zelda Behaviour is not set to a valid number.")
    return f"|Snake| AND |Lucario| AND |Peach| AND {zelda} AND |Fox| AND |Falco|"

def Check_Entrance_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    zelda_requirement = get_option_value(multiworld, player, "zelda_behaviour")
    if zelda_requirement == 0:
        zelda = "|@Zelda/Sheik|"
    elif zelda_requirement == 1:
        zelda = "|Zelda|"
    elif zelda_requirement == 2:
        zelda = "|Progressive Zelda: 1|"
    else:
        raise OptionError("Option Zelda Behaviour is not set to a valid number.")
    samus_requirement = get_option_value(multiworld, player, "samus_behaviour")
    if samus_requirement == 0:
        samus = "|@Samus Aran|"
    elif samus_requirement == 1:
        samus = "|Samus|"
    elif samus_requirement == 2:
        samus = "|Progressive Samus: 2|"
    else:
        raise OptionError("Option Samus Behaviour is not set to a valid number.")
    red_requirement = get_option_value(multiworld, player, "trainer_behaviour")
    if red_requirement == 0:
        red = "|Pokémon Trainer|"
    elif red_requirement == 1:
        red = "(|Pokémon Trainer| AND (|Squirtle| OR |Ivysaur| OR |Charizard|))"
    elif red_requirement == 2:
        red = "|Progressive Pokémon Trainer: 2|"
    else:
        raise OptionError("Option Pokémon Trainer Behaviour is not set to a valid number.")
    return f"|Captain Falcon| AND |Donkey Kong| AND |Diddy Kong| AND |Fox| AND |Falco| AND |Ice Climbers| AND |Marth| AND |Ike| AND |Kirby| AND |Link| AND |Lucario| AND |Lucas| AND |Mario| AND |Meta Knight| AND |Mr. Game & Watch| AND |Olimar| AND |Peach| AND {zelda} AND |Pikachu| AND |Pit| AND {red} AND |R.O.B.| AND {samus} AND |Snake| AND |Yoshi|"

def Check_Ganondorf_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    zelda_requirement = get_option_value(multiworld, player, "zelda_behaviour")
    if zelda_requirement == 0:
        zelda = "|@Zelda/Sheik|"
    elif zelda_requirement == 1:
        zelda = "|Zelda|"
    elif zelda_requirement == 2:
        zelda = "|Progressive Zelda: 1|"
    else:
        raise OptionError("Option Zelda Behaviour is not set to a valid number.")
    return f"|Link| AND {zelda}"

def Check_Great_Maze_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    maze_percentage = get_option_value(multiworld, player, "maze_fighter_percentage")
    
    maze_requirement = get_option_value(multiworld, player, "great_maze_requirements")
    if maze_requirement == 0:
        return "|@Fighter: 1|"
    elif maze_requirement == 1:
        return "|Luigi| AND |Ness| AND |King Dedede| AND |Bowser| AND |Kirby|"
    elif maze_requirement == 2:
        return f"|@Fighter: {maze_percentage}%|"
    elif maze_requirement == 3:
        return f"|Luigi| AND |Ness| AND |King Dedede| AND |Bowser| AND |Kirby| AND |@Fighter: {maze_percentage}%|"
    elif maze_requirement == 4:
        return "|@Fighter: ALL|"
    else:
        return True

def Check_Tabuu_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    tabuu_percentage = get_option_value(multiworld, player, "tabuu_fighter_percentage")
    
    boss_amount = get_option_value(multiworld, player, "tabuu_boss_amount")
    tabuu_requirement = get_option_value(multiworld, player, "tabuu_requirements")
    if tabuu_requirement == 0:
        return True
    elif tabuu_requirement == 1:
        return f"|@Fighter: {tabuu_percentage}%|"
    elif tabuu_requirement == 2:
        return f"|Boss Trophy: {boss_amount}|"
    elif tabuu_requirement == 3:
        return f"|@Fighter: {tabuu_percentage}%| AND |Boss Trophy: {boss_amount}|"
    else:
        return True

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(world: World, multiworld: MultiWorld, state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

