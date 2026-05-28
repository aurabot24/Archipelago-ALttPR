from dataclasses import dataclass
from enum import Enum

from Options import FreeText, PerGameCommonOptions, Range, TextChoice, Toggle


class WorldMode(TextChoice):
    """Open: Start from Link's House or Sanctuary, without needing to save Zelda in Hyrule Castle
    Standard: Start at Link's House and save Zelda in Hyrule Castle before accessing the rest of the world
    Inverted: The Light World and Dark World have been flipped.
        - Link starts at their house (swapped with the Bomb Shop) or Dark Sanctuary
        - All Dark World portals now take you to the Light World
        - Link is a bunny in the Light World unless you have the Moon Pearl
        - Agahnim's Tower and Ganon's Tower have swapped places. Agahnim's Tower now requires crystals to enter
        - Ganon is hiding in a new hole on top of Hyrule Castle
        - The Magic Mirror takes you from the Light World to the Dark World
        - The Flute must be activated in Kakariko Village, but will then take you to locations across the Dark World
        - Light World terrain has been modified so that mirror-locked locations can be reached without the mirror
        - The top of Turtle Rock can be accessed by jumping from its tail"""
    display_name = "World Mode"
    option_open = "open"
    option_standard = "standard"
    option_inverted = "inverted"
    # option_retro = "retro"
    default = "open"


class Goal(TextChoice):
    """Sets the goal for this seed.

    crystals: Collect the required number of crystals and kill Ganon.
    ganon: Collect the required number of crystals, kill Agahnim on top of Ganon's Tower, then kill Ganon.
    dungeons: Complete all 12 dungeons, including Agahnim's Tower and Ganon's Tower, then kill Ganon.
    pedestal: Collect all 3 pendants and pull the Master Sword from its pedestal.
    triforcehunt: Collect the required number of pieces of the Triforce, then talk to Murahdahla outside Hyrule Castle.
    ganonhunt: Collect the required number of pieces of the Triforce, then kill Ganon.
    trinity: Either kill Ganon, pull the pedestal, or collect the required number of Triforce pieces and talk to Murahdahla outside Hyrule Castle.
    completionist: Collect every check in the game, then kill Ganon."""
    display_name = "Goal"
    option_crystals = "crystals"
    option_ganon = "ganon"
    option_dungeons = "dungeons"
    option_pedestal = "pedestal"
    option_triforcehunt = "triforcehunt"
    option_ganonhunt = "ganonhunt"
    option_trinity = "trinity"
    option_completionist = "completionist"
    default = "crystals"


class OpenPyramid(TextChoice):
    """ Whether the Pyramid hole leading to Ganon should be open at the start. Choosing "auto" will open or close it based on your goal setting;
    it will be open for crystals, trinity, and ganonhunt, and closed for other goals, or if crossed entrance is enabled regardless of the goal."""
    display_name = "Open Pyramid"
    option_auto = "auto"
    option_open = "yes"
    option_closed = "no"
    default = "auto"


class CrystalsNeededForGanonsTower(Range):
    """How many crystals are needed to enter Ganon's Tower"""
    display_name = "Crystals Needed for Ganon's Tower"
    range_start = 0
    range_end = 7
    default = 7


class CrystalsNeededForGanon(Range):
    """How many crystals are needed before Ganon can be killed"""
    display_name = "Crystals Needed for Ganon"
    range_start = 0
    range_end = 7
    default = 7


class TriforceHuntGoal(Range):
    """How many Triforce Pieces are required to beat the game when the goal is set to Triforce Hunt or Ganon Hunt"""
    display_name = "Triforce Hunt Goal"
    range_start = 1
    range_end = 50  # TODO: What should the max number of triforce pieces be?
    default = 20


class TriforceHuntTotal(Range):
    """How many Triforce Pieces are in the item pool when the goal is set to Triforce Hunt or Ganon Hunt"""
    display_name = "Triforce Hunt Total"
    range_start = 1
    range_end = 50
    default = 30


class MapShuffle(Toggle):
    """Maps can now appear outside of their dungeon. The map screen will not show if a dungeon gives a pendant or crystal until its map has been found."""
    display_name = "Map Shuffle"


class CompassShuffle(Toggle):
    """Compasses can now appear outside of their dungeon."""
    display_name = "Compass Shuffle"


class SmallKeyShuffle(Toggle):
    """Small keys can now appear outside of their dungeon."""
    display_name = "Small Key Shuffle"


class BigKeyShuffle(Toggle):
    """Big keys can now appear outside of their dungeon."""
    display_name = "Big Key Shuffle"


class KeyDropShuffle(Toggle):
    """Shuffle keys that are dropped by enemies or hidden under pots."""
    display_name = "Key Drop Shuffle"
    default = False


class EntranceShuffle(TextChoice):
    """Randomize where each building, cave, and dungeon entrance leads to."""
    display_name = "Entrance Shuffle"
    option_vanilla = "vanilla"
    option_crossed = "crossed"
    default = "vanilla"
    # TODO: Entrance shuffles other than vanilla and crossed


class Zelgawoods(Toggle):
    """If entrance shuffle is enabled, add Skull Woods entrances and dropdowns to the entrance shuffle. The main Skull Woods entrance/big chest
    dropdown and the second Skull Woods entrance/the dropdown in the back are both added to the dropdown pool. The other two dropdowns in the
    front are vanilla, and at least one of the entrances in the back of the Skull Woods area must be a connector."""
    # TODO: If I have a good link to the image description a picture is better than text descriptions
    display_name = "Zelgawoods"


class DoorShuffle(TextChoice):
    """Randomize the layout of each dungeon. Rooms are rearranged or appear in other dungeons, and doors are randomized.

    * Dungeons always have their original boss room, which drops that dungeon's prize.
    * Dropdowns are vanilla, and rooms connected by a dropdown are always in the same dungeon.
    * Dungeons may have different key counts. Agahnims Tower could have a Big Key, and other dungeons may not have a Big Key.
    * Killing Blind requires bombing the cracked floor in the attic, which may be in a different dungeon.
    * Bringing the Maiden to the Thieves Town boss room will tell you which dungeon has the attic.
    * Locations will have the name of their original dungeon, not the dungeon they appear in.

    vanilla: Dungeons have their vanilla layout
    basic: Dungeon layouts are shuffled, but each room stays in its own dungeon
    partitioned: Dungeon layouts are shuffled, with rooms from different dungeons being mixed together. Rooms in light world dungeons including Hyrule
        Castle and Agahnims Tower are shuffled together, early dark world dungeons (Palace of Darkness to Thieves Town) are shuffled together, and
        Mitts-locked dungeons (Ice Palace to Ganons Tower) are shuffled together.
    crossed: Rooms from all dungeons are shuffled together."""
    display_name = "Door Shuffle"
    option_vanilla = "vanilla"
    option_basic = "basic"
    option_partitioned = "partitioned"
    option_crossed = "crossed"
    default = "vanilla"


class LobbyShuffle(Toggle):
    """Whether the first room in each dungeon is randomized."""
    display_name = "Lobby Shuffle"
    default = False


class DoorTypeShuffle(Toggle):
    """Randomize the type of each door (small key, big key, bombable, trap, etc.)"""
    display_name = "Door Type Shuffle"
    default = False


class EnemyShuffle(TextChoice):
    """All enemies except bosses are randomized. Logical enemy shuffle might require defeating enemies that
    require specific items (Eyegore, Freezors, etc.) to progress in a dungeon."""
    display_name = "Enemy Shuffle"
    option_vanilla = "none"
    option_shuffled = "random"
    option_logical = "logical"
    default = "none"


class BossShuffle(TextChoice):
    """Bosses are randomized. This includes the Armos/Lanmolas/Moldorm rematches in Ganon's Tower, but not Ganon or either Aganhim fight. Some bosses cannot appear in some locations.

    * Vanilla: Bosses are in their original locations.
    * Simple: Bosses are shuffled randomly. Armos Knights, Lanmolas, and Moldorm will be fought twice.
    * Full: Bosses are shuffled randomly, and three random bosses will be fought twice.
    * Chaos: Bosses are shuffled randomly, and any boss can be fought any number of times."""
    display_name = "Boss Shuffle"
    option_vanilla = "none"
    option_simple = "simple"
    option_full = "full"
    option_chaos = "random"
    default = "none"


class Shopsanity(Toggle):
    """All shops contain randomized items, including Potion Shop and Capacity Upgrade Fairy. Adds 32 items to the item pool. Each type of potion can be purchased
    at a random shop."""
    display_name = "Shopsanity"
    default = False


class PrizeShuffle(Toggle):
    """Adds Pendants and Crystals to the itempool."""
    display_name = "Prize Shuffle"
    default = False


class FluteShuffle(TextChoice):
    """Randomize the Flute spot destinations. Balanced will spread the Flute spots around the overworld, while Chaos will place them randomly."""
    display_name = "Flute Shuffle"
    option_vanilla = "vanilla"
    option_balanced = "balanced"
    option_chaos = "random"
    default = "vanilla"


class Pseudoboots(Toggle):
    """Psuedoboots give Link the ability to dash like Pegasus Boots, but they cannot bonk rocks, open King's Tomb, knock items off torches/the Library, or clear small gaps"""
    display_name = "Pseudoboots"
    default = False


class MirrorScroll(Toggle):
    """Mirror Scroll is an inventory item that warps Link to the start of their current dungeon, and is replaced upon finding the Magic Mirror."""
    display_name = "Mirror Scroll"
    default = False


class PreActivatedFlute(Toggle):
    """The Flute does not need to be activated at the village statue after finding it."""
    display_name = "Pre Activated Flute"
    default = False


class Sprite(FreeText):
    """A custom sprite to use for Link. Must be 'Link' or the exact name of a sprite listed at https://alttpr.com/en/sprite_preview.
    If an error occurs when loading the sprite, the default Link sprite will be used."""
    display_name = "Sprite"
    default = "Link"


class HeartBeepRate(TextChoice):
    """The rate at which heart beeps are played when Link is at low health."""
    display_name = "Heart Beep Rate"
    option_double = "double"
    option_normal = "normal"
    option_half = "half"
    option_quarter = "quarter"
    option_never = "off"
    default = "normal"


class HeartColor(TextChoice):
    """The color of Link's heart meter."""
    display_name = "Heart Color"
    option_red = "red"
    option_blue = "blue"
    option_green = "green"
    option_yellow = "yellow"
    default = "red"


class FastMenu(TextChoice):
    """The rate at which the menu opens and closes."""
    display_name = "Fast Menu"
    option_normal = "normal"
    option_instant = "instant"
    option_double = "double"
    option_triple = "triple"
    option_quadruple = "quadruple"
    option_half = "half"
    default = "normal"


# class OWPalettes(TextChoice):
#     """The palette of the overworld sprites."""
#     display_name = "Overworld Palettes"
#     option_default = "default"
#     option_randomized = "randomized"
#     option_blackout = "blackout"
#     default = "default"


# class UWPalettes(TextChoice):
#     """The palette of the underworld sprites."""
#     display_name = "Underworld Palettes"
#     option_default = "default"
#     option_randomized = "randomized"
#     option_blackout = "blackout"
#     default = "default"


class DisableMusic(Toggle):
    """Disables game music."""
    display_name = "Disable Music"
    default = False


# class ShuffleSFX(Toggle):
#     """Shuffles the soundtrack."""
#     display_name = "Shuffle SFX"
#     default = False


# class ShuffleSFXInstruments(Toggle):
#     """Shuffles the soundtrack instruments."""
#     display_name = "Shuffle SFX Instruments"
#     default = False


# class ShuffleSongInstruments(Toggle):
#     """Shuffles the soundtrack instruments on a per-song basis, so each song will have its own shuffled set of instruments."""
#     display_name = "Shuffle Song Instruments"
#     default = False


class MSUResume(Toggle):
    """While using an MSU, when entering and leaving a building/cave/dungeon, the overworld music will pick up where it left off, instead of restarting every time."""
    display_name = "MSU Resume"
    default = False


@dataclass
class ALttPROptions(PerGameCommonOptions):
    world_mode: WorldMode
    goal: Goal
    open_pyramid: OpenPyramid
    crystals_needed_for_ganons_tower: CrystalsNeededForGanonsTower
    crystals_needed_for_ganon: CrystalsNeededForGanon
    triforce_hunt_goal: TriforceHuntGoal
    triforce_hunt_total: TriforceHuntTotal
    map_shuffle: MapShuffle
    compass_shuffle: CompassShuffle
    small_key_shuffle: SmallKeyShuffle
    big_key_shuffle: BigKeyShuffle
    key_drop_shuffle: KeyDropShuffle
    entrance_shuffle: EntranceShuffle
    zelgawoods: Zelgawoods
    door_shuffle: DoorShuffle
    lobby_shuffle: LobbyShuffle
    door_type_shuffle: DoorTypeShuffle
    enemy_shuffle: EnemyShuffle
    boss_shuffle: BossShuffle
    shopsanity: Shopsanity
    prize_shuffle: PrizeShuffle
    flute_shuffle: FluteShuffle
    pre_activated_flute: PreActivatedFlute
    pseudoboots: Pseudoboots
    mirror_scroll: MirrorScroll
    sprite: Sprite
    heart_beep_rate: HeartBeepRate
    heart_color: HeartColor
    fast_menu: FastMenu
    # ow_palettes: OWPalettes
    # uw_palettes: UWPalettes
    disable_music: DisableMusic
    # shuffle_sfx: ShuffleSFX
    # shuffle_sfxinstruments: ShuffleSFXInstruments
    # shuffle_songinstruments: ShuffleSongInstruments
    msu_resume: MSUResume
