# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging
import math

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove = [] # List of location names

    # Okay you just don't get to fight him again in free play for some reason.
    locationNamesToRemove.append("The Wilds I - Galleom I")

    # Add your code here to calculate which locations to remove
    enabled_secret_characters = is_option_enabled(multiworld, player, "secret_character_shuffle")
    enabled_hoarde_shuffle = is_option_enabled(multiworld, player, "hoarde_shuffle")
    for location in world.location_table:
         if "Secret Battle" in location.get("category", []) and not enabled_secret_characters:
            locationNamesToRemove.append(location["name"])
         if "Hoarde" in location.get("category", []) and not enabled_hoarde_shuffle:
            locationNamesToRemove.append(location["name"])
    
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)
    if hasattr(multiworld, "clear_location_cache"):
        multiworld.clear_location_cache()

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove = [] # List of item names

    # Check for how Boss Trophies need to be removed and add them to the remove queue
    if get_option_value(multiworld, player, "tabuu_requirements") != 2 or 3:
        trophies_to_remove = 8
    else:
        trophies_to_remove = 8 - get_option_value(multiworld, player, "tabuu_boss_amount")
    for i in range(1, trophies_to_remove):
        itemNamesToRemove.append("Boss Trophy")

    # Remove Progressive Trainers, Pokemon, or both depending on settings
    if get_option_value(multiworld, player, "trainer_behaviour") == 0:
        itemNamesToRemove.append("Squirtle")
        itemNamesToRemove.append("Ivysaur")
        itemNamesToRemove.append("Charizard")
        for i in range(4):
            itemNamesToRemove.append("Progressive Pokémon Trainer")
    elif get_option_value(multiworld, player, "trainer_behaviour") == 1:
        for i in range(4):
            itemNamesToRemove.append("Progressive Pokémon Trainer")
    elif get_option_value(multiworld, player, "trainer_behaviour") == 2:
        itemNamesToRemove.append("Pokémon Trainer")
        itemNamesToRemove.append("Squirtle")
        itemNamesToRemove.append("Ivysaur")
        itemNamesToRemove.append("Charizard")

    # Remove Progressive Samuses, or Zero Suit and Samus depending on settings
    if get_option_value(multiworld, player, "samus_behaviour") == 0:
        for i in range(2):
            itemNamesToRemove.append("Progressive Samus")
    elif get_option_value(multiworld, player, "samus_behaviour") == 1:
        for i in range(2):
            itemNamesToRemove.append("Progressive Samus")
    elif get_option_value(multiworld, player, "samus_behaviour") == 2:
        itemNamesToRemove.append("Samus")
        itemNamesToRemove.append("Zero Suit Samus")

    # Remove Progressive Zeldas, or Zelda/Sheik depending on settings
    if get_option_value(multiworld, player, "zelda_behaviour") == 0:
        for i in range(2):
            itemNamesToRemove.append("Progressive Zelda")
    if get_option_value(multiworld, player, "zelda_behaviour") == 1:
        for i in range(2):
            itemNamesToRemove.append("Progressive Zelda")
    elif get_option_value(multiworld, player, "zelda_behaviour") == 2:
        itemNamesToRemove.append("Zelda")
        itemNamesToRemove.append("Sheik")

    # Remove characters that are in the Extra category from the pool if secret_character_shuffle is not on.
    if not is_option_enabled(multiworld, player, "secret_character_shuffle"):
        itemNamesToRemove.append("Toon Link")
        itemNamesToRemove.append("Jigglypuff")
        itemNamesToRemove.append("Wolf")

    for itemName in itemNamesToRemove:
        for i in item_pool:
            if i.name == itemName:
                item_pool.remove(i)

    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:

    return item_pool

    # Some other useful hook options:


# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    
    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int) -> list:
    # Check if Boss Hunt is enabled
    if get_option_value(multiworld, player, "tabuu_requirements") != (2 or 3):
        return

    boss_trophies = [
        item for item in multiworld.itempool
            if "Boss Trophy" in world.item_name_to_item.values()
    ]
    #boss_names = next(
    #    iter([
    #        name for name, location in world.location_name_to_location.items()
    #            if "Boss" in location.get("category", [])
    #    ])
    #)
    boss_locations = [
        location for location in multiworld.get_locations(player)
    ]
    print(boss_trophies)
    print(boss_locations)
    for boss in boss_trophies:
        if len(boss_locations) == 0:
            break
        location_to_place_at = world.random.choice(boss_locations)
        location_to_place_at.place_locked_item(boss)
        multiworld.itempool.remove(boss)
        boss_locations.remove(location_to_place_at)


# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass
