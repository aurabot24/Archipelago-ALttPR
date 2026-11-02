from Options import OptionError
from ..bases import ALttPRTestBase


class TestInvalidOptions(ALttPRTestBase):
    @property
    def run_default_tests(self) -> bool:
        return False

    def test_invalid_option(self):
        # Tests if invalid options raise an OptionError
        # Range options like the required number of crystals throw an exception before
        # our world is created, so we don't need to test them.
        invalid_options = {
            "world_mode": "invalid",
            "goal": "invalid",
            "open_pyramid": "invalid",
            "entrance_shuffle": "invalid",
            "enemy_shuffle": "invalid",
            "boss_shuffle": "invalid",
            "flute_shuffle": "invalid",
            "dungeon_counters": "invalid",
            "sprite": "invalid",
            "heart_beep_rate": "invalid",
            "heart_color": "invalid",
            "fast_menu": "invalid",
        }
        default_options = self.options.copy()
        for option, value in invalid_options.items():
            with self.subTest(option=option, value=value):
                self.options = default_options.copy()
                self.options[option] = value
                error = KeyError if option != "sprite" else OptionError
                self.assertRaises(error, self.world_setup)
        self.options = default_options
