from copy import deepcopy
from .bases import ALttPRTestBaseNoDefaultTests
from .data import slot_data_crossed


class TestSpikeCaveWithPotions(ALttPRTestBaseNoDefaultTests):
    options = {
        "pre_activated_flute": True,
    }

    def test_spike_cave_with_potions(self):
        # Bottle items could be Bottle, Bottle (Bee), etc. so we need to find the right name for this seed
        bottle_name = [item.name for item in self.multiworld.itempool if item.name.startswith("Bottle")][0]
        self.assertCanNotReachWith(["Spike Cave"], "location",
[["Moon Pearl", "Progressive Glove", "Ocarina (Activated)", "Hammer", "Cape"]])
        self.assertCanReachWith(["Spike Cave"], "location",
[[bottle_name, "Moon Pearl", "Progressive Glove", "Ocarina (Activated)", "Hammer", "Cape"]])


class TestMimicCaveEnemyDropShuffle(ALttPRTestBaseNoDefaultTests):
    auto_construct = False
    options = {
        "entrance_shuffle": "crossed",
        "enemy_drop_shuffle": "underworld",
    }

    def test_mimic_cave_enemy_drop_shuffle(self):
        # Mimic Cave is at the Red Shield Shop. Need entrance shuffle to check if the back enemies
        # are dependent on Hammer, which is always needed to reach the vanilla location
        slot_data = deepcopy(slot_data_crossed.slot_data)
        self.options["test_slot_data"] = slot_data
        self.world_setup()

        self.assertCanReachWith(["Mimic Cave Enemy #5", "Mimic Cave Enemy #6"],
                                "location", [["Moon Pearl", "Hammer"]])
        self.assertCanReachWith(["Mimic Cave Enemy #7", "Mimic Cave Enemy #8"],
                                "location", [["Moon Pearl", "Blue Boomerang", "Red Boomerang"]])