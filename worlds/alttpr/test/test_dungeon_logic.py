import pytest
from .bases import ALttPRTestBaseNoDefaultTests
from ..Items import ItemFactory


class TestDungeonLogic(ALttPRTestBaseNoDefaultTests):
    options = {
        "crystals_needed_for_ganons_tower": 0,
        "small_key_shuffle": "true",
        "key_drop_shuffle": "true",
    }


    def test_left_side_swamp(self):
        for _ in range(0, 2):
            self.multiworld.state.collect(ItemFactory("Small Key (Swamp Palace)", 1))
        self.assertAccessDependency(["Swamp Palace - West Chest", "Swamp Palace - Big Key Chest"],
                [["Progressive Glove", "Hammer", "Moon Pearl", "Flippers", "Magic Mirror", "Small Key (Swamp Palace)"]], only_check_listed=True)


    def test_ice_palace_lobby(self):
        self.assertCanNotReachWith(["Ice Palace - Compass Chest"], "location",
            [["Flippers", "Progressive Glove", "Progressive Glove", "Moon Pearl", "Small Key (Ice Palace)", "Bombos"]])
        self.assertCanReachWith(["Ice Palace - Compass Chest"], "location", [
            ["Flippers", "Progressive Glove", "Progressive Glove", "Moon Pearl", "Small Key (Ice Palace)", "Fire Rod"],
            ["Flippers", "Progressive Glove", "Progressive Glove", "Moon Pearl", "Small Key (Ice Palace)", "Bombos", "Progressive Sword"],
        ])


    def test_ice_palace_backwards_room(self):
        ip_small_keys = self.get_items_by_name("Small Key (Ice Palace)")
        for i in range(0, 4):
            self.collect(ip_small_keys[i])
        core_ip_items = ["Flippers", "Progressive Glove", "Progressive Glove", "Moon Pearl", "Fire Rod"]
        self.assertCanNotReachWith(["Ice Backwards Room Down Stairs"], "entrance", [core_ip_items + ["Big Key (Ice Palace)", "Book of Mudora"]])
        self.assertCanReachWith(["Ice Backwards Room Down Stairs"], "entrance", [ core_ip_items + ["Big Key (Ice Palace)", "Small Key (Ice Palace)"]])


    def test_tile_room(self):
        self.assertCanReachWith(["Ganons Tower - Tile Room"], "location",
                [["Progressive Glove", "Progressive Glove", "Moon Pearl", "Lamp", "Hookshot", "Cane of Somaria"]])


class TestDungeonCrystalBookLogic(ALttPRTestBaseNoDefaultTests):
    options = {
        "crystals_needed_for_ganons_tower": 0,
        "small_key_shuffle": "true",
        "key_drop_shuffle": "true",
        "crystal_book": "true",
    }


    def test_ice_palace_backwards_room(self):
        ip_small_keys = self.get_items_by_name("Small Key (Ice Palace)")
        for i in range(0, 5):
            self.collect(ip_small_keys[i])
        core_ip_items = ["Flippers", "Progressive Glove", "Progressive Glove", "Moon Pearl", "Fire Rod"]
        self.assertCanNotReachWith(["Ice Backwards Room Down Stairs"], "entrance", [core_ip_items + ["Big Key (Ice Palace)"]])
        self.assertCanReachWith(["Ice Backwards Room Down Stairs"], "entrance", [core_ip_items + ["Small Key (Ice Palace)", "Big Key (Ice Palace)"], core_ip_items + ["Small Key (Ice Palace)", "Book of Mudora"]])
