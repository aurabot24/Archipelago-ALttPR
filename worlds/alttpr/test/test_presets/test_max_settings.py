from ..bases import ALttPRTestBase


# Testing if someone goes crazy and enables every setting they can.
class TestMaxSettings(ALttPRTestBase):
    options = {
        "world_mode": "inverted",
        "goal": "triforcehunt",
        "open_pyramid": "auto",
        "crystals_needed_for_ganon": 6,
        "triforce_hunt_goal": 50,
        "triforce_hunt_total": 50,
        "entrance_shuffle": "crossed",
        "shuffle_links_house": "true",
        "shuffle_tavern": "true",
        "door_shuffle": "crossed",
        "door_type_shuffle": "big",
        "lobby_shuffle": "true",
        "map_shuffle": "true",
        "compass_shuffle": "true",
        "small_key_shuffle": "true",
        "big_key_shuffle": "true",
        "key_drop_shuffle": "true",
        "shopsanity": "true",
        "pot_shuffle": "lottery",
        "enemy_drop_shuffle": "underworld",
        "enemy_shuffle": "logical",
        "boss_shuffle": "chaos",
        "prize_shuffle": "true",
        "flute_shuffle": "chaos",
        "pseudoboots": "true",
        "mirror_scroll": "true",
        "zelgawoods": "true",
    }