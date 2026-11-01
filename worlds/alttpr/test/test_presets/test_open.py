from ..bases import ALttPRTestBase


class TestOpen(ALttPRTestBase):
    def test_non_randomized_locations_hidden(self):
        assert len([location for location in self.world.get_locations() if location.address]) == 216