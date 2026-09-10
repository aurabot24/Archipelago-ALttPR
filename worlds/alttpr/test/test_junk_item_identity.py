"""Junk placement must remove the placed object, not an equal unplaced copy."""
import unittest
from types import SimpleNamespace

from BaseClasses import Item, ItemClassification, Location
from ..Items import place_junk_items_in_pots


class TestJunkItemIdentity(unittest.TestCase):
    def check_placement(self, *, pots, progression=False):
        name = "Triforce Piece" if progression else "Small Heart"
        classification = ItemClassification.progression if progression else ItemClassification.filler
        unplaced = Item(name, classification, 1, 1)
        placed = Item(name, classification, 1, 1)
        self.assertEqual(unplaced, placed)
        self.assertIsNot(unplaced, placed)
        pool = [unplaced, placed]
        progitempool = pool if progression else []
        filleritempool = [] if progression else pool
        locations = [Location(1, f"Pot {i:03}") for i in range(257)] if pots else [
            Location(1, "Chest 1"), Location(1, "Chest 2")]
        original_locations = list(locations)
        # Pot candidates are reversed by the function; local-fill candidates need
        # a reversed shuffle to put the second equal object first instead.
        shuffle = (lambda values: None) if pots else (lambda values: values.reverse())
        world = SimpleNamespace(
            player=1,
            random=SimpleNamespace(shuffle=shuffle),
            options=SimpleNamespace(non_local_items=set(), local_fill_percent=0 if pots else 50),
        )

        place_junk_items_in_pots(progitempool, [], filleritempool, locations, world)

        self.assertEqual(len(pool), 1)
        self.assertIs(pool[0], unplaced)
        self.assertIsNone(unplaced.location)
        self.assertIsNotNone(placed.location)
        self.assertIs(placed.location.item, placed)
        self.assertTrue(placed.location.locked)
        self.assertEqual(len(locations), len(original_locations) - 1)
        self.assertNotIn(placed.location, locations)

    def test_local_fill_removes_the_placed_filler_copy(self):
        self.check_placement(pots=False)

    def test_pot_overflow_removes_the_placed_filler_copy(self):
        self.check_placement(pots=True)

    def test_pot_overflow_removes_the_placed_progression_copy(self):
        self.check_placement(pots=True, progression=True)
