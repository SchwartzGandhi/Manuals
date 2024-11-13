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

def Check_Lake_Shore_Requirements(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    zelda_requirement = get_option_value(multiworld, player, "zelda_behaviour")
    if zelda_requirement == 0:
        zelda = "|@Zelda/Sheik|"
    elif zelda_requirement == 1:
        zelda = "|Sheik|"
    elif zelda_requirement == 2:
        zelda = "|Progressive Zelda: 2|"
    else:
        raise OptionError("Option Zelda Behaviour is not set to a valid number.")
    return f"(|Peach| AND |Link| AND |Yoshi|) OR ({zelda} AND |Mario| AND |Pit|)"

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
    return f"|Snake| AND |Lucario| AND |Meta Knight| AND |Peach| AND {zelda} AND |Fox| AND |Falco|"

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

def ItemValue(world: World, multiworld: MultiWorld, state: CollectionState, player: int, args: str):
    """When passed a string with this format: 'valueName:int',
    this function will check if the player has collect at least 'int' valueName worth of items\n
    eg. {ItemValue(Coins:12)} will check if the player has collect at least 12 coins worth of items
    """

    args_list = args.split(":")
    if not len(args_list) == 2 or not args_list[1].isnumeric():
        raise Exception(f"ItemValue needs a number after : so it looks something like 'ItemValue({args_list[0]}:12)'")
    args_list[0] = args_list[0].lower().strip()
    args_list[1] = int(args_list[1].strip())

    if not hasattr(world, 'item_values_cache'): #Cache made for optimization purposes
        world.item_values_cache = {}

    if not world.item_values_cache.get(player, {}):
        world.item_values_cache[player] = {
            'state': {},
            'count': {},
            }

    if (args_list[0] not in world.item_values_cache[player].get('count', {}).keys()
            or world.item_values_cache[player].get('state') != dict(state.prog_items[player])):
        #Run First Time or if state changed since last check
        existing_item_values = get_items_with_value(world, multiworld, args_list[0])
        total_Count = 0
        for name, value in existing_item_values.items():
            count = state.count(name, player)
            if count > 0:
                total_Count += count * value
        world.item_values_cache[player]['count'][args_list[0]] = total_Count
        world.item_values_cache[player]['state'] = dict(state.prog_items[player]) #save the current gotten items to check later if its the same
    return world.item_values_cache[player]['count'][args_list[0]] >= args_list[1]


# Two useful functions to make require work if an item is disabled instead of making it inaccessible
def OptOne(world: World, multiworld: MultiWorld, state: CollectionState, player: int, item: str, items_counts: Optional[dict] = None):
    """Check if the passed item (with or without ||) is enabled, then this returns |item:count|
    where count is clamped to the maximum number of said item in the itempool.\n
    Eg. requires: "{OptOne(|DisabledItem|)} and |other items|" become "|DisabledItem:0| and |other items|" if the item is disabled.
    """
    if item == "":
        return "" #Skip this function if item is left blank
    if not items_counts:
        items_counts = world.get_item_counts()

    require_type = 'item'

    if '@' in item[:2]:
        require_type = 'category'

    item = item.lstrip('|@$').rstrip('|')

    item_parts = item.split(":")
    item_name = item
    item_count = '1'

    if len(item_parts) > 1:
        item_name = item_parts[0]
        item_count = item_parts[1]

    if require_type == 'category':
        if item_count.isnumeric():
            #Only loop if we can use the result to clamp
            category_items = [item for item in world.item_name_to_item.values() if "category" in item and item_name in item["category"]]
            category_items_counts = sum([items_counts.get(category_item["name"], 0) for category_item in category_items])
            item_count = clamp(int(item_count), 0, category_items_counts)
        return f"|@{item_name}:{item_count}|"
    elif require_type == 'item':
        if item_count.isnumeric():
            item_current_count = items_counts.get(item_name, 0)
            item_count = clamp(int(item_count), 0, item_current_count)
        return f"|{item_name}:{item_count}|"

# OptAll check the passed require string and loop every item to check if they're enabled,
def OptAll(world: World, multiworld: MultiWorld, state: CollectionState, player: int, requires: str):
    """Check the passed require string and loop every item to check if they're enabled,
    then returns the require string with items counts adjusted using OptOne\n
    eg. requires: "{OptAll(|DisabledItem| and |@CategoryWithModifedCount:10|)} and |other items|"
    become "|DisabledItem:0| and |@CategoryWithModifedCount:2| and |other items|" """
    requires_list = requires

    items_counts = world.get_item_counts()

    functions = {}
    if requires_list == "":
        return True
    for item in re.findall(r'\{(\w+)\(([^)]*)\)\}', requires_list):
        #so this function doesn't try to get item from other functions, in theory.
        func_name = item[0]
        functions[func_name] = item[1]
        requires_list = requires_list.replace("{" + func_name + "(" + item[1] + ")}", "{" + func_name + "(temp)}")
    # parse user written statement into list of each item
    for item in re.findall(r'\|[^|]+\|', requires):
        itemScanned = OptOne(world, multiworld, state, player, item, items_counts)
        requires_list = requires_list.replace(item, itemScanned)

    for function in functions:
        requires_list = requires_list.replace("{" + function + "(temp)}", "{" + func_name + "(" + functions[func_name] + ")}")
    return requires_list

# Rule to expose the can_reach_location core function
def canReachLocation(world: World, multiworld: MultiWorld, state: CollectionState, player: int, location: str):
    """Can the player reach the given location?"""
    if state.can_reach_location(location, player):
        return True
    return False
