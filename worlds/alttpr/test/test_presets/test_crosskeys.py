from ..bases import ALttPRTestBase


class TestCrosskeys(ALttPRTestBase):
    options = {
        "entrance_shuffle": "crossed",
        "map_shuffle": "true",
        "compass_shuffle": "true",
        "small_key_shuffle": "true",
        "big_key_shuffle": "true",
    }