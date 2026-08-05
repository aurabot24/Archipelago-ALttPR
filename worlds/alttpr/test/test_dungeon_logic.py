import pytest
from .bases import ALttPRTestBaseNoDefaultTests
from ..Items import ItemFactory


class TestDungeonLogic(ALttPRTestBaseNoDefaultTests):
    options = {
        "crystals_required_for_ganons_tower": 0,
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


    def test_tile_room(self):
        self.assertAccessDependency(["Ganons Tower - Tile Room"],
                [["Progressive Glove", "Progressive Glove", "Moon Pearl", "Lamp", "Hookshot", "Cane of Somaria"]], only_check_listed=True)