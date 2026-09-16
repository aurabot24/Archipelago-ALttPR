from copy import deepcopy
from .bases import ALttPRTestBaseNoDefaultTests
from .data import slot_data_crossed, slot_data_inverted_crossed, slot_data_inverted_flute_shuffle


class BigBombShopBase(ALttPRTestBaseNoDefaultTests):
    options = {
        "prize_shuffle": True,
    }

    def assertCanReachPyramidCrackWith(self, item_combinations: list[list[str]]):
        for item_combination in item_combinations:
            item_combination.extend(["Crystal 5", "Crystal 6"])
        self.assertCanReachWith(["Pyramid Crack"], "entrance", item_combinations)


    def assertCanNotReachPyramidCrackWith(self, item_combinations: list[list[str]]):
        for item_combination in item_combinations:
            item_combination.extend(["Crystal 5", "Crystal 6"])
        self.assertCanNotReachWith(["Pyramid Crack"], "entrance", item_combinations)


class TestBigBombDefaultSettings(BigBombShopBase):
    def test_big_bomb_open(self):
        self.assertCanNotReachPyramidCrackWith([["Progressive Glove", "Progressive Glove", "Moon Pearl", "Flippers"]])
        self.assertCanReachPyramidCrackWith([["Progressive Glove", "Hammer", "Moon Pearl"],
                                             ["Progressive Glove", "Progressive Glove", "Moon Pearl", "Magic Mirror", "Beat Agahnim 1"]])


class BigBombShopEntranceShuffleBase(BigBombShopBase):
    auto_construct = False
    options = {
        "prize_shuffle": True,
        "entrance_shuffle": "crossed",
        "test_slot_data": {},
    }


class TestBigBombShopAtDesertSouth(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_desert_south(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["two-way"]["Misery Mire"] = "Elder House Exit (East)"
        slot_data["entrances"][1]["two-way"]["Bush Covered House"] = "Hookshot Cave Front Exit"
        del slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"]
        del slot_data["entrances"][1]["two-way"]["Desert Palace Entrance (South)"]
        slot_data["entrances"][1]["two-way"]["Dark Lake Hylia Ledge Fairy"] = "Bumper Cave Exit (Top)"
        slot_data["entrances"][1]["entrances"]["Desert Palace Entrance (South)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Book of Mudora", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Book of Mudora", "Ocarina (Activated)", "Beat Agahnim 1"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Magic Mirror", "Beat Agahnim 1"],
        ])


class TestBigBombShopInKak(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_in_kak(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Red Shield Shop"
        slot_data["entrances"][1]["entrances"]["Kakariko Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Progressive Glove", "Progressive Glove", "Flippers", "Moon Pearl"]])
        self.assertCanReachPyramidCrackWith([
            ["Beat Agahnim 1"],
            ["Progressive Glove", "Hammer", "Moon Pearl"],
        ])


class TestBigBombShopOnDesertLedge(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_on_desert_ledge(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["two-way"]["Misery Mire"] = "Elder House Exit (East)"
        slot_data["entrances"][1]["two-way"]["Bush Covered House"] = "Hookshot Cave Front Exit"
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Lake Hylia Fortune Teller"
        slot_data["entrances"][1]["entrances"]["Desert Palace Entrance (West)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Ocarina (Activated)", "Progressive Glove"], ["Magic Mirror"]])
        self.assertCanReachPyramidCrackWith([
            ["Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Ocarina (Activated)", "Progressive Glove", "Beat Agahnim 1"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Magic Mirror", "Beat Agahnim 1"],
        ])


class TestBigBombShopAtCapacityShop(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_capacity_shop(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        del slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"]
        del slot_data["entrances"][1]["two-way"]["Capacity Upgrade"]
        slot_data["entrances"][1]["two-way"]["Dark Lake Hylia Ledge Fairy"] = "Desert Palace Exit (East)"
        slot_data["entrances"][1]["entrances"]["Capacity Upgrade"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Flippers", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Flippers", "Ocarina (Activated)", "Beat Agahnim 1"],
        ])

class TestBigBombShopAtWaterfallFairy(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_waterfall_fairy(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Desert Healer Fairy"
        slot_data["entrances"][1]["entrances"]["Waterfall of Wishing"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Flippers", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Flippers", "Ocarina (Activated)", "Beat Agahnim 1"],
        ])

class TestBigBombShopAtDMDWest(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_capacity_shop(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        del slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"]
        del slot_data["entrances"][1]["two-way"]["Death Mountain Return Cave (West)"]
        slot_data["entrances"][1]["two-way"]["Dark Lake Hylia Ledge Fairy"] = "Death Mountain Return Cave Exit (East)"
        slot_data["entrances"][1]["entrances"]["Death Mountain Return Cave (West)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Magic Mirror", "Ocarina (Activated)", "Beat Agahnim 1"],
        ])


class TestBigBombShopOnDeathMountain(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_capacity_shop(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Hookshot Fairy"
        slot_data["entrances"][1]["entrances"]["Old Man Cave (East)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Ocarina (Activated)", "Beat Agahnim 1"],
            ])


class TestBigBombShopOnTopOfHyruleCastle(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_on_top_of_hyrule_castle(self):
        # There is a sphere one connector to east Dark World
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Dark Lake Hylia Ledge Healer Fairy"
        slot_data["entrances"][1]["entrances"]["Hyrule Castle Entrance (East)"] = "Big Bomb Shop"
        slot_data["entrances"][1]["entrances"]["Hyrule Castle Entrance (West)"] = "Paradox Cave Exit (Top)"  # Making a connector
        slot_data["entrances"][1]["entrances"]["20 Rupee Cave"] = "Spectacle Rock Cave Exit (Top)"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.can_reach_region("Hyrule Castle Ledge")
        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror"],
            ["Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Ocarina (Activated)", "Beat Agahnim 1"],
        ])


class TestBigBombShopInEastDarkWorld(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_in_east_dark_world(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Archery Game"
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.can_reach_entrance("Pyramid Crack")


class TestBigBombShopInNorthDarkWorld(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_in_north_dark_world(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "20 Rupee Cave"
        slot_data["entrances"][1]["entrances"]["Thieves Town"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Moon Pearl", "Progressive Glove", "Flippers"]])
        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Beat Agahnim 1"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
            ["Moon Pearl", "Progressive Glove", "Progressive Glove", "Hammer"],
        ])


class TestBigBombShopAtCuriosityShop(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_dark_world_mirror_then_walk(self):
        # You can't jump down the ledge to leave without Mirror
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Mimic Cave"
        slot_data["entrances"][1]["entrances"]["Red Shield Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"]])
        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Beat Agahnim 1"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
        ])


class TestBigBombShopAtDarkShoppingMall(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_dark_shopping_mall(self):
        # You can't jump down the ledge to leave without Mirror
        slot_data = deepcopy(slot_data_crossed.slot_data)
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl", "Flippers"]])
        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Beat Agahnim 1", "Moon Pearl", "Flippers"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl", "Flippers"],
        ])


class TestBigBombShopInMire(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_in_mire(self):
        # You can't jump down the ledge to leave without Mirror
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Aginahs Cave"
        slot_data["entrances"][1]["entrances"]["Mire Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Beat Agahnim 1", "Ocarina (Activated)", "Progressive Glove", "Progressive Glove"],
            ["Magic Mirror", "Hammer", "Moon Pearl", "Ocarina (Activated)", "Progressive Glove", "Progressive Glove"],
        ])


class TestBigBombShopAtCheckerboard(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_in_mire(self):
        # You can't jump down the ledge to leave without Mirror
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Chest Game"
        slot_data["entrances"][1]["entrances"]["Checkerboard Cave"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Beat Agahnim 1", "Ocarina (Activated)", "Progressive Glove", "Progressive Glove", "Magic Mirror"],
            ["Hammer", "Ocarina (Activated)", "Progressive Glove", "Progressive Glove", "Magic Mirror"],
        ])


class TestBigBombShopInBackOfSkull(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_in_back_of_skull(self):
        # You can't jump down the ledge to leave without Mirror
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Lake Hylia Shop"
        slot_data["entrances"][1]["entrances"]["Skull Woods Final Section"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Beat Agahnim 1", "Fire Rod", "Moon Pearl"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Fire Rod", "Moon Pearl"],
        ])


class TestBigBombShopAtIcePalace(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_ice_palace(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Dark Lake Hylia Shop"
        slot_data["entrances"][1]["entrances"]["Ice Palace"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.collect_by_name(["Progressive Glove", "Flippers"])
        assert self.can_reach_entrance("Ice Palace"), "Cannot reach the bomb shop"
        self.assertCanNotReachPyramidCrackWith(
                                   [["Magic Mirror", "Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"]])
        self.assertCanReachWith(["Pyramid Crack"], "location", [
            ["Magic Mirror", "Ocarina (Activated)", "Beat Agahnim 1"],
            ["Magic Mirror", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
        ])


class TestBigBombShopOnDarkDeathMountain(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_on_dark_death_mountain(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Bonk Rock Cave"
        slot_data["entrances"][1]["entrances"]["Spike Cave"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith(
                                   [["Magic Mirror", "Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"]])
        self.assertCanReachWith(["Pyramid Crack"], "location", [
            ["Magic Mirror", "Ocarina (Activated)", "Beat Agahnim 1"],
            ["Magic Mirror", "Ocarina (Activated)", "Progressive Glove", "Hammer", "Moon Pearl"],
        ])


class TestBigBombShopAtDarkPotionShop(BigBombShopEntranceShuffleBase):
    def test_big_bomb_shop_at_dark_potion_shop(self):
        slot_data = deepcopy(slot_data_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Dam"
        slot_data["entrances"][1]["entrances"]["Dark Potion Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Progressive Glove", "Moon Pearl"],
            ["Hammer", "Moon Pearl"],
            ["Magic Mirror", "Beat Agahnim 1"],
        ])


class TestBigBombInverted(BigBombShopBase):
    options = {
        "world_mode": "inverted",
        "prize_shuffle": True,
    }

    def test_big_bomb_inverted(self):
        self.assertCanNotReachPyramidCrackWith([["Flippers", "Progressive Glove"]])
        self.assertCanReachPyramidCrackWith([["Hammer"], ["Ocarina (Activated)"], ["Magic Mirror", "Progressive Glove", "Progressive Glove", "Moon Pearl"]])


class TestBigBombInvertedFluteShuffle(BigBombShopBase):
    auto_construct = False
    options = {
        "world_mode": "inverted",
        "prize_shuffle": True,
        "flute_shuffle": "chaos",
        "test_slot_data": {},
    }

    def test_big_bomb_inverted_flute_to_catfish(self):
        # When the only Flute to east Dark World is near Catfish
        slot_data = deepcopy(slot_data_inverted_flute_shuffle.slot_data)
        slot_data["ow-flutespots"][1] = [0, 2, 3, 10, 15, 16, 19, 48]
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Ocarina (Activated)"]])
        self.assertCanReachPyramidCrackWith([["Hammer"],
                                             ["Ocarina (Activated)", "Progressive Glove"],  # Flute to catfish
                                             ["Magic Mirror", "Progressive Glove", "Progressive Glove", "Moon Pearl"],
                                            ])


    def test_big_bomb_inverted_flute_no_east_dark_world(self):
        # There are no Flute spots in east dark world
        slot_data = slot_data_inverted_flute_shuffle.slot_data
        slot_data["ow-flutespots"][1] = [0, 2, 3, 10, 16, 17, 19, 48]
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Ocarina (Activated)", "Progressive Glove", "Flippers"]])


class BigBombInvertedEntranceShuffleBase(BigBombShopBase):
    auto_construct = False
    options = {
        "world_mode": "inverted",
        "prize_shuffle": True,
        "entrance_shuffle": "crossed",
        "shuffle_links_house": True,  # Shuffles the Bomb Shop
        "test_slot_data": {},
    }


class TestBigBombShopInEastDarkWorldInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_in_east_dark_world(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Graveyard Cave"
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.can_reach_entrance("Pyramid Crack")


class TestBigBombShopInNorthDarkWorldInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_in_north_dark_world(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Palace of Darkness Hint"
        slot_data["entrances"][1]["entrances"]["Chest Game"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Progressive Glove", "Progressive Glove", "Hammer"],
            ["Ocarina (Activated)"],
            ["Magic Mirror", "Progressive Glove", "Progressive Glove", "Moon Pearl"],
            ["Magic Mirror", "Progressive Glove", "Hammer", "Moon Pearl"],
        ])


class TestBigBombShopAtCuriosityShopInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_curiousity_shop(self):
        # You can't jump off the ledge with the Big Bomb
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Village of Outcasts Shop"
        slot_data["entrances"][1]["entrances"]["Red Shield Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanNotReachPyramidCrackWith([["Progressive Glove", "Progressive Glove", "Hammer", "Moon Pearl"]])
        self.assertCanReachPyramidCrackWith([
            ["Ocarina (Activated)"],
            ["Magic Mirror"],
        ])


class TestBigBombShopInDarkShoppingMallInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_in_dark_shopping_mall(self):
        # You can't jump off the ledge with the Big Bomb
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        del slot_data["entrances"][1]["entrances"]["Chicken House"]
        del slot_data["entrances"][1]["two-way"]["Dark Lake Hylia Ledge Fairy"]
        slot_data["entrances"][1]["two-way"]["Chicken House"] = "Misery Mire Exit"
        slot_data["entrances"][1]["entrances"]["Dark Lake Hylia Ledge Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Ocarina (Activated)", "Flippers"],
            ["Magic Mirror", "Flippers"],
        ])


class TestBigBombShopInMireInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_in_mire(self):
        # You can't jump off the ledge with the Big Bomb
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "50 Rupee Cave"
        slot_data["entrances"][1]["entrances"]["Mire Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Ocarina (Activated)"],
            ["Magic Mirror"],
        ])


class TestBigBombShopInBackOfSkullInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_in_back_of_skull(self):
        # You can't jump off the ledge with the Big Bomb
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Aginahs Cave"
        slot_data["entrances"][1]["entrances"]["Skull Woods Final Section"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Ocarina (Activated)"],
            ["Magic Mirror"],
        ])


class TestBigBombShopOnDarkDeathMountainInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_on_dark_death_mountain(self):
        # You can't jump off the ledge with the Big Bomb
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Dark Death Mountain Healer Fairy"
        slot_data["entrances"][1]["entrances"]["Dark Death Mountain Fairy"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([["Ocarina (Activated)"]])


class TestBigBombShopAtIcePalaceInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_ice_palace(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        del slot_data["entrances"][1]["entrances"]["Chicken House"]
        del slot_data["entrances"][1]["two-way"]["Ice Palace"]
        slot_data["entrances"][1]["two-way"]["Chicken House"] = "Hyrule Castle Exit (South)"
        slot_data["entrances"][1]["entrances"]["Ice Palace"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertAccessDependency(["Pyramid Crack"], [["Ocarina (Activated)"]])


class TestBigBombShopAtBumperCaveTopInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_bumper_cave_top(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Ice Rod Cave"
        slot_data["entrances"][1]["entrances"]["Bumper Cave (Top)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([["Ocarina (Activated)", "Magic Mirror"]])

class TestBigBombShopAtDarkPotionShopInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_dark_potion_shop(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Checkerboard Cave"
        slot_data["entrances"][1]["entrances"]["Dark Potion Shop"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Progressive Glove", "Fire Rod", "Flippers"],
            ["Hammer", "Fire Rod", "Flippers"],
            ["Ocarina (Activated)", "Fire Rod", "Flippers"],
            ["Magic Mirror", "Moon Pearl", "Fire Rod", "Flippers"],  # Mirror from Potion Shop, walk the bomb through the Light World to HC. Mearl is required to reach Potion Shop
        ])


class TestBigBombShopInKakInverted(BigBombInvertedEntranceShuffleBase):
    def test_big_bomb_shop_in_kak(self):
        # Big bomb shop is in Kak with the slot data
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([["Magic Mirror"]])


class TestBigBombShopOnTopOfHyruleCastleInverted(BigBombInvertedEntranceShuffleBase):
    def test_big_bomb_shop_on_top_of_hyrule_castle(self):
        # This will have to be rewritten if the slot data changes, so there aren't any duplicate entrances.
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Lake Hylia Fortune Teller"
        slot_data["entrances"][1]["entrances"]["Hyrule Castle Entrance (East)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror"],
        ])


class TestBigBombShopAtDesertSouthInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_desert_south(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        del slot_data["entrances"][1]["entrances"]["Chicken House"]
        del slot_data["entrances"][1]["two-way"]["Desert Palace Entrance (South)"]
        slot_data["entrances"][1]["two-way"]["Chicken House"] = "Palace of Darkness Exit"
        slot_data["entrances"][1]["entrances"]["Desert Palace Entrance (South)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertAccessDependency(["Pyramid Crack"], [["Magic Mirror", "Ocarina (Activated)", "Book of Mudora", "Moon Pearl"]], only_check_listed=True)


class TestBigBombShopAtDesertLedgeInverted(BigBombInvertedEntranceShuffleBase):
    # Desert West is a connector
    def test_inverted_big_bomb_shop_at_desert_ledge(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        del slot_data["entrances"][1]["entrances"]["Chicken House"]
        del slot_data["entrances"][1]["two-way"]["Desert Palace Entrance (North)"]
        slot_data["entrances"][1]["two-way"]["Chicken House"] = "Skull Woods Final Section Exit"
        slot_data["entrances"][1]["entrances"]["Desert Palace Entrance (North)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertAccessDependency(["Pyramid Crack"], [["Magic Mirror", "Ocarina (Activated)", "Progressive Glove"]], only_check_listed=True)


class TestBigBombShopAtCapacityShopInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_capacity_shop(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Brewery"
        slot_data["entrances"][1]["entrances"]["Capacity Upgrade"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertAccessDependency(["Pyramid Crack"], [["Magic Mirror", "Ocarina (Activated)", "Flippers", "Moon Pearl"]], only_check_listed=True)


class TestBigBombShopAtWaterfallInverted(BigBombInvertedEntranceShuffleBase):
    def test_inverted_big_bomb_shop_at_waterfall_shop(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Dark Lake Hylia Shop"
        slot_data["entrances"][1]["entrances"]["Waterfall of Wishing"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertAccessDependency(["Pyramid Crack"], [["Magic Mirror", "Ocarina (Activated)", "Flippers", "Moon Pearl"]], only_check_listed=True)


class TestBigBombShopAtLightWorldTopOfDeathMountainInverted(BigBombInvertedEntranceShuffleBase):
    # Paradox Top is a connector
    def test_inverted_big_bomb_shop_at_waterfall_shop(self):
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Capacity Upgrade"
        slot_data["entrances"][1]["entrances"]["Tower of Hera"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertAccessDependency(["Pyramid Crack"], [["Magic Mirror", "Ocarina (Activated)", "Hammer", "Moon Pearl"]], only_check_listed=True)


class TestBigBombShopAtLightWorldSouthwestDeathMountainInverted(BigBombInvertedEntranceShuffleBase):
    # There is a series of connectors to floating island
    def test_big_bomb_shop_southwest_light_death_mountain(self):
        # This will have to be rewritten if the slot data changes, so there aren't any duplicate entrances.
        slot_data = deepcopy(slot_data_inverted_crossed.slot_data)
        slot_data["entrances"][1]["entrances"]["Chicken House"] = "Fortune Teller (Light)"
        slot_data["entrances"][1]["entrances"]["Old Man Cave (East)"] = "Big Bomb Shop"
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachPyramidCrackWith([
            ["Magic Mirror", "Ocarina (Activated)"],
        ])
