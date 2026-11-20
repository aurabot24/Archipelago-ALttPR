from copy import deepcopy

from data import slot_data_doors_boss_shuffle
from .bases import ALttPRTestBaseNoDefaultTests
from .data import slot_data_basic_doors


class TestReadDoorsSlotData(ALttPRTestBaseNoDefaultTests):
    auto_construct = False
    options = {
        "door_shuffle": "basic",
    }

    def test_read_doors_slot_data(self):
        slot_data = deepcopy(slot_data_basic_doors.slot_data)
        self.options["test_slot_data"] = slot_data
        self.world_setup()
        assert_key_logic_matches_slot_data(slot_data, self.world)


class TestReadDoorsBossSlotData(ALttPRTestBaseNoDefaultTests):
    auto_construct = False
    options = {
        "boss_shuffle": "chaos",
        "door_shuffle": "basic",
    }

    def test_read_doors_boss_slot_data(self):
        slot_data = deepcopy(slot_data_doors_boss_shuffle.slot_data)
        self.options["test_slot_data"] = slot_data
        self.world_setup()
        assert_key_logic_matches_slot_data(slot_data, self.world)


def assert_key_logic_matches_slot_data(slot_data, world):
    slot_data_key_logic = slot_data["doors"]["1"]["key_logic"]["doors"]
    key_logic = world.door_rando_world.key_logic[1]
    for dungeon_key_logic in key_logic.values():
        for door, door_rules in dungeon_key_logic.door_rules.items():
            assert door in slot_data_key_logic
            assert door_rules.small_key_num == slot_data_key_logic[door]
