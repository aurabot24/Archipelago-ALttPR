from BaseClasses import MultiWorld
from .bases import ALttPRTestBaseNoDefaultTests


class TestKeyDropOverridesNoPottery(ALttPRTestBaseNoDefaultTests):
    options = {
        "key_drop_shuffle": True,
        "pot_shuffle": "none",
    }

    def test_key_drop_overrides_no_pottery(self):
        assert self.world.door_rando_world.pottery[1] == "keys"


class TestKeyDropOverridesCavePottery(ALttPRTestBaseNoDefaultTests):
    options = {
        "key_drop_shuffle": True,
        "potsanity": "cave",
    }

    def test_key_drop_overrides_cave_pottery(self):
        assert self.world.door_rando_world.pottery[1] == "cavekeys"

class TestCavePotteryWithoutKeyDrop(ALttPRTestBaseNoDefaultTests):
    options = {
        "potsanity": "cave",
    }

    def test_cave_pottery_without_key_drop(self):
        assert self.world.door_rando_world.pottery[1] == "cave"


class TestKeyDropAndNoSwordWithNoEnemyDropShuffle(ALttPRTestBaseNoDefaultTests):
    options = {
        "key_drop_shuffle": True,
        "enemy_drop_shuffle": "none",
    }

    def test_key_drop_overrides_no_enemy_drop(self):
        assert self.world.door_rando_world.dropshuffle[1] == "keys"
        assert len(self.world.door_rando_world.precollected_items) == 0
        assert self.world.door_rando_world.dungeon_counters[1] == "pickup"


num_cave_keys = 144
num_dungeon_keys = 658
num_pot_keys = 19

class TestPotteryCaveShuffle(ALttPRTestBaseNoDefaultTests):
    options = {
        "potsanity": "cave",
    }

    def test_pottery_cave_shuffle(self):
        assert len([location for location in self.world.get_locations() if location.address]) == 216 + num_cave_keys


class TestPotteryCaveKeysShuffle(ALttPRTestBaseNoDefaultTests):
    options = {
        "potsanity": "cavekeys",
    }

    def test_pottery_cave_keys_shuffle(self):
        assert len([location for location in self.world.get_locations() if location.address]) == 216 + num_cave_keys + num_pot_keys


class TestPotteryDungeonShuffle(ALttPRTestBaseNoDefaultTests):
    options = {
        "potsanity": "dungeon",
    }

    def test_pottery_dungeon_shuffle(self):
        assert len([location for location in self.world.get_locations() if location.address]) == 216 + num_dungeon_keys


class TestPotteryLotteryShuffle(ALttPRTestBaseNoDefaultTests):
    options = {
        "potsanity": "lottery",
    }

    def test_pottery_lottery_shuffle(self):
        assert len([location for location in self.world.get_locations() if location.address]) == 216 + num_cave_keys + num_dungeon_keys


class TestEnemyDropShuffleUnderworld(ALttPRTestBaseNoDefaultTests):
    options = {
        "enemy_drop_shuffle": "underworld",
    }

    def test_enemy_drop_shuffle_underworld(self):
        assert self.world.door_rando_world.dropshuffle[1] == "underworld"
        assert len(self.world.door_rando_world.precollected_items) == 0
        assert self.world.door_rando_world.dungeon_counters[1] == "on"
