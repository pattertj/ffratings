import unittest

from src.ffratings import enums, fantasyclient


class TestSimple(unittest.TestCase):
    def test_add(self):
        client = fantasyclient.FantasyClient()
        result = client.get_projections(enums.Source.BetIQ, enums.Position.ALL)
        self.assertEqual(result, enums.Position.ALL)


if __name__ == "__main__":
    unittest.main()
