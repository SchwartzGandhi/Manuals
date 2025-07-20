from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value, is_option_enabled
from BaseClasses import MultiWorld, CollectionState

import re

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

def Suitcases(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|memo from bed| AND |picture of an old cruise liner| AND |note from bulletin board|"
    else: 
        return True
    
def ShowerTile(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|curtain|"
    else: 
        return True

def JohnAndLucy(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|The medical record|"
    else: 
        return True

def ShipDirection(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|stack of nautical maps|"
    else: 
        return True

def ShipSpeed(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|The ship's log|"
    else: 
        return True
    
def CaptainsCode(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|The numeral system chart|"
    else: 
        return True

def ALL(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|9 panel cross puzzle|"
    else: 
        return True

def ICE(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|Morse code chart 1| AND |Morse code chart 2| AND |Morse code chart 3|"
    else: 
        return True

def ReverseShip(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|Study nautical table|"
    else: 
        return True

def Monitor(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|Clover's note|"
    else: 
        return True
    
def Pushmaster5000(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|Pushmaster 5000 Instructions|"
    else: 
        return True
    
def ShowerDrain(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|luminol|"
    else: 
        return True

def ShowerCode(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|a piece of paper| AND |bocket filled with hot water| AND |broom wrapped in toilet paper|"
    else: 
        return True

def SpringRiver(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    if is_option_enabled(multiworld, player, 'morphogenetic_field_theory'):
        return "|towel|"
    else: 
        return True