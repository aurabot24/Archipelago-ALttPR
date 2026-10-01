from .bases import ALttPRTestBaseNoDefaultTests


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