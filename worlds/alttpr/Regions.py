from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from BaseClasses import Entrance, Location, Region

from .ALttPDoorRandomizer.BaseClasses import CrystalBarrier, PotItem, PotFlags, RegionType
from .ALttPDoorRandomizer.source.dungeon import EnemyList
from .ALttPDoorRandomizer import PotShuffle
from .ALttPDoorRandomizer import Regions as DoorRandomizerRegions
from .ALttPDoorRandomizer.source.rom import DataTables
from .RomAddresses import location_table_pot_items, location_table_sprite_items
from .StateAdapter import adapt_door_rando_rule

if TYPE_CHECKING:
    from .World import ALttPRWorld


location_name_to_id = {}
lookup_id_to_name = {}
lookup_name_to_id = {}
logger = logging.getLogger("alttpr")


class ALttPRRegion(Region):
    game = "The Legend of Zelda: A Link to the Past"
    has_crystal_switch = False
    is_in_dungeon = False


class ALttPRLocation(Location):
    game = "The Legend of Zelda: A Link to the Past"


class ALttPREntrance(Entrance):
    game = "The Legend of Zelda: A Link to the Past"
    crystal = CrystalBarrier.Null


class ALttPRCrystalPath:
    def __init__(self, color: CrystalBarrier, crystal_switch_region: ALttPRRegion, path: list[ALttPREntrance]):
        self.color = color
        self.crystal_switch_region = crystal_switch_region
        self.path = path


dungeon_vanilla_entrance_regions = {
    "Hyrule Castle": ["Hyrule Castle Lobby", "Hyrule Castle West Lobby", "Hyrule Castle East Lobby", "Sanctuary"],
    "Eastern Palace": ["Eastern Lobby"],
    "Desert Palace": ["Desert Main Lobby", "Desert West Lobby", "Desert East Lobby", "Desert Back Lobby"],
    "Tower of Hera": ["Hera Lobby"],
    "Agahnims Tower": ["Tower Lobby"],
    "Palace of Darkness": ["PoD Lobby"],
    "Swamp Palace": ["Swamp Lobby"],
    "Skull Woods": ["Skull 1 Lobby", "Skull 2 West Lobby", "Skull 2 East Lobby", "Skull 3 Lobby"],
    "Thieves Town": ["Thieves Lobby"],
    "Ice Palace": ["Ice Lobby"],
    "Misery Mire": ["Mire Lobby"],
    "Turtle Rock": ["TR Main Lobby", "TR Lazy Eyes", "TR Big Chest Entrance", "TR Eye Bridge"],
    "Ganons Tower": ["GT Lobby"],
}



def create_and_connect_regions(world: ALttPRWorld) -> None:
    # First define every region, then loop through a second time to connect them.
    # Otherwise we're trying to connect to regions that don't exist yet.
    ap_regions = {}
    crystal_switches = {dungeon: [] for dungeon in world.door_rando_world.dungeons}
    event_locations = get_event_locations(world)

    for region in world.door_rando_world.regions:
        ap_region = ALttPRRegion(region.name, world.player, world.multiworld)
        ap_region.is_in_dungeon = region.type == RegionType.Dungeon
        if region.crystal_switch:
            ap_region.has_crystal_switch = region.crystal_switch
            crystal_switches[region.dungeon].append(ap_region)

        for location in region.locations:
            # Skip all locations that aren't randomized with the user's options
            if ("Shop - " in location.name or "Upgrade - " in location.name) and not world.options.shopsanity:
                continue
            elif " Item " in location.name:
                # TODO: Retro
                continue
            elif location.item and "Farmable" in location.item.name:
                # These are in logic to see if the player can farm rupees or bombs.
                # TODO: Overworld shuffle
                continue
            else:
                # The dungeon prize locations aren't in lookup_name_to_id (not sure how they're removed?),
                # so they won't have an ID, which is how an event location is defined.
                id = lookup_name_to_id.get(location.name, None)
                if not id and \
                   " - Prize" not in location.name and \
                   location.name not in event_locations:
                    raise Exception(f"Found unknown location {location.name} in region {region.name}.")

                if world.is_excluded_key_drop_location(location) or location.name in event_locations:
                    id = None

                ap_location = ALttPRLocation(
                    world.player, location.name, id, ap_region
                )
                ap_location.access_rule = adapt_door_rando_rule(location.access_rule, world.door_rando_world, world.player, world.crystal_paths)
                ap_region.locations.append(ap_location)

        ap_regions[region.name] = ap_region

    # Now make all the connections
    for region in world.door_rando_world.regions:
        ap_region = ap_regions[region.name]
        for exit in region.exits:
            if exit.connected_region is None:
                continue

            # Need to check for always impassible doors, other door logic like keys is handled in access_rule
            blocked = False if not exit.door else exit.door.blocked

            ap_entrance = ALttPREntrance(world.player, exit.name, parent=ap_region)
            ap_entrance.access_rule = adapt_door_rando_rule(exit.access_rule if not blocked else lambda state: False, world.door_rando_world, world.player, world.crystal_paths)
            if exit.door:
                ap_entrance.crystal = exit.door.crystal
            ap_region.exits.append(ap_entrance)
            ap_entrance.connect(ap_regions[exit.connected_region.name])

    world.multiworld.regions += list(ap_regions.values())
    find_crystal_switch_paths(world, crystal_switches)


def find_crystal_switch_paths(world: ALttPRWorld, dungeon_crystal_info):
    # For each entrance in a dungeon that has crystal logic (orange/blue blocks), find
    # all possible paths to that entrance with the blocks in the correct position.
    for dungeon, crystal_switches in dungeon_crystal_info.items():
        entrance_regions = dungeon.entrance_regions if dungeon.entrance_regions else [world.get_region(region_name) for region_name in dungeon_vanilla_entrance_regions[dungeon.name]]
        for entrance_region in entrance_regions:
            find_crystal_switch_path(world, entrance_region, entrance_region, set(), [], CrystalBarrier.Orange)
        for crystal_switch in crystal_switches:
            find_crystal_switch_path(world, crystal_switch, crystal_switch, set(), [], CrystalBarrier.Either)


def find_crystal_switch_path(world: ALttPRWorld, start_region: ALttPRRegion, current_region: ALttPRRegion, past_regions: set[ALttPRRegion], path: list[ALttPREntrance], color: CrystalBarrier) -> None:
    # Recursive helper function for finding paths through a dungeon from a crystal switch in start_region, to make sure
    # the crystal block logic is handled correctly.
    if current_region in past_regions or not current_region.is_in_dungeon:
        # Only follow new paths through the dungeon
        return

    if current_region.has_crystal_switch and current_region != start_region:
        # Found another crystal switch, no need to continue
        return

    # Hera basement cage is the only location that's blocked by crystal blocks, everything else is an entrance
    if current_region.name == "Hera Basement Cage":
        if not current_region.name in world.crystal_paths:
            world.crystal_paths[current_region.name] = []
        world.crystal_paths[current_region.name].append(ALttPRCrystalPath(color, start_region, path))

    past_regions.add(current_region)
    for exit in current_region.exits:
        if not exit.crystal or exit.crystal == CrystalBarrier.Either:
            find_crystal_switch_path(world, start_region, exit.connected_region, past_regions.copy(), path + [exit], color)
            continue

        if (exit.crystal == CrystalBarrier.Orange and color == CrystalBarrier.Blue) or \
           (exit.crystal == CrystalBarrier.Blue and color == CrystalBarrier.Orange):
            # Blocked by orange/blue blocks
            continue

        if not current_region.name in world.crystal_paths:
            world.crystal_paths[current_region.name] = []
        world.crystal_paths[current_region.name].append(ALttPRCrystalPath(color, start_region, path))
        world.multiworld.register_indirect_condition(start_region, exit)
        find_crystal_switch_path(world, start_region, exit.connected_region, past_regions.copy(), path + [exit], exit.crystal)


def get_event_locations(world: ALttPRWorld):
    # TODO: I feel like most of these aren't needed until door randomizer is added, and some of them still seem unnecessary (e.g. Skull Star Tile).
    # It's fine if it doesn't affect anything for players, but if it shows up in the player log or Poptracker than that could be an annoyance.
    # TODO: Maybe get these directly from OWR?
    event_locations = {
        "Ganon": "Triforce",
        "Agahnim 1": "Beat Agahnim 1",
        "Agahnim 2": "Beat Agahnim 2",
        "Lost Old Man": "Escort Old Man",
        "Old Man Drop Off": "Return Old Man",
        "Locksmith": "Sign Vandalized",
        "Kiki": "Pick Up Kiki",
        "Kiki Assistance": "Dark Palace Opened",
        "Frog": "Get Frog",
        "Missing Smith": "Return Smith",
        "Dark Blacksmith Ruins": "Pick Up Purple Chest",
        "Middle Aged Man": "Deliver Purple Chest",
        "Big Bomb": "Pick Up Big Bomb",
        "Pyramid Crack": "Detonate Big Bomb",
        "Floodgate": "Open Floodgate",
        "Trench 1 Switch": "Trench 1 Filled",
        "Trench 2 Switch": "Trench 2 Filled",
        "Swamp Drain": "Drained Swamp",
        "Attic Cracked Floor": "Shining Light",
        "Suspicious Maiden": "Maiden Rescued",
        "Revealing Light": "Maiden Unmasked",
        "Ice Block Drop": "Convenient Block",
        "Skull Star Tile": "Hidden Pits",
        "Turtle Medallion Pad": "Turtle Opened",
        'Eastern Palace - Boss Kill': 'Beat Boss',
        "Desert Palace - Boss Kill": "Beat Boss",
        "Tower of Hera - Boss Kill": "Beat Boss",
        "Palace of Darkness - Boss Kill": "Beat Boss",
        "Swamp Palace - Boss Kill": "Beat Boss",
        "Skull Woods - Boss Kill": "Beat Boss",
        "Thieves\' Town - Boss Kill": "Beat Boss",
        "Ice Palace - Boss Kill": "Beat Boss",
        "Misery Mire - Boss Kill": "Beat Boss",
        "Turtle Rock - Boss Kill": "Beat Boss",
        "Zelda Pickup": "Zelda Herself",
        "Zelda Drop Off": "Zelda Delivered",
        # Some events are only created in certain modes
        # "Master Sword Pedestal": "Triforce",
        # "Murahdahla": "Triforce",
        # "Flute Activation": "Ocarina (Activated)",
    }

    goal = world.options.goal.value
    if goal == "triforcehunt":
        event_locations["Ganon"] = "Nothing"
    if goal == "triforcehunt" or goal == "trinity":
        event_locations["Murahdahla"] = "Triforce"
    if goal == "pedestal" or goal == "trinity":
        event_locations["Master Sword Pedestal"] = "Triforce"
    if world.options.world_mode.value != "inverted" and not world.options.pre_activated_flute.value:
        event_locations["Flute Activation"] = "Ocarina (Activated)"

    return event_locations



# Add info on all locations to lookup_id_to_name and lookup_name_to_id.
# This is used by the client to send items we pick up.
def init_lookups():
    global lookup_id_to_name
    global lookup_name_to_id

    lookup_id_to_name = {x: y for x, y in DoorRandomizerRegions.lookup_id_to_name.items()}
    lookup_name_to_id = {x: y for x, y in DoorRandomizerRegions.lookup_name_to_id.items()}

    for event in DoorRandomizerRegions.location_events:
        lookup_name_to_id[event] = None

    for super_tile, pot_list in PotShuffle.vanilla_pots.items():
        for pot_index, pot in enumerate(pot_list):
            if pot.item != PotItem.Hole:
                if pot.item == PotItem.Key:
                    loc_name = next(loc for loc, datum in PotShuffle.key_drop_data.items()
                                    if datum[1] == super_tile)
                else:
                    continue
                    # TODO: Pottery Lottery
                    # descriptor = 'Large Block' if pot.flags & PotFlags.Block else f'Pot #{pot_index+1}'
                    # loc_name = f'{pot.room} {descriptor}'
                location_table_pot_items[loc_name] = (2 * super_tile, 0x8000 >> pot_index)
                location_id = DoorRandomizerRegions.pot_address(pot_index, super_tile)
                lookup_name_to_id[loc_name] = location_id
                lookup_id_to_name[location_id] = loc_name
    uw_table = DataTables.get_uw_enemy_table()
    key_drop_data = {(v[1][1], v[1][2]): k for k, v in PotShuffle.key_drop_data.items() if v[0] == 'Drop'}
    for super_tile, enemy_list in uw_table.room_map.items():
        index_adj = 0
        for index, sprite in enumerate(enemy_list):
            if sprite.sub_type == 0x07:  # overlord
                index_adj += 1
                continue
            if (super_tile, index) in key_drop_data:
                loc_name = key_drop_data[(super_tile, index)]
                location_id = PotShuffle.key_drop_data[loc_name][1][0]
            else:
                continue
                # TODO: Enemy drop shuffle
                # loc_name = f'{sprite.region} Enemy #{index+1}'
                # location_id = EnemyList.drop_address(index, super_tile)
            # if index < index_adj:
            #     logging.info(f'Problem at {hex(super_tile)} {loc_name}')
            location_table_sprite_items[loc_name] = (2 * super_tile, 0x8000 >> (index-index_adj))
            lookup_name_to_id[loc_name] = location_id
            lookup_id_to_name[location_id] = loc_name

init_lookups()