import unittest
import poker_spades_game


class MyTestCase(unittest.TestCase):
    # Testing the check_straight function
    def test_straights_1(self):
        self.assertEqual(poker_spades_game.check_straight('SJ', 'SK', 'SQ'), 13)

    def test_straights_2(self):
        self.assertEqual(poker_spades_game.check_straight('S5', 'S3', 'S4'), 5)

    def test_straights_3(self):
        self.assertEqual(poker_spades_game.check_straight('S2', 'SK', 'S9'), 0)

    # Testing the check_3ofa_kind function
    def test_3_kind_1(self):
        self.assertEqual(poker_spades_game.check_3ofa_kind('SJ', 'SK', 'SQ'), 0)

    def test_3_kind_2(self):
        self.assertEqual(poker_spades_game.check_3ofa_kind('SJ', 'SJ', 'SJ'), 11)

    # Testing the check_royal_flush function
    def test_royal_flush1(self):
        self.assertEqual(poker_spades_game.check_royal_flush('SJ', 'SQ', 'SA'), 0)

    def test_royal_flush2(self):
        self.assertEqual(poker_spades_game.check_royal_flush('SQ', 'SA', 'SK'), 14)

    def test_royal_flush3(self):
        self.assertEqual(poker_spades_game.check_royal_flush('SJ', 'SQ', 'SK'), 0)

    # Testing the play_cards function.
    # First trying 3 of a kind win conditions
    def test_left_win_3kind(self):
        self.assertEqual(poker_spades_game.play_cards('SJ', 'SJ', 'SJ', 'S5', 'S5', 'S5'), -1)

    def test_right_win_3kind(self):
        self.assertEqual(poker_spades_game.play_cards('S3', 'S3', 'S3', 'S5', 'S5', 'S5'), 1)

    def test_tie_win_3kind(self):
        self.assertEqual(poker_spades_game.play_cards('S5', 'S5', 'S5', 'S5', 'S5', 'S5'), 0)

    # Trying 1 player with a straight and 1 with a 3 of a kind win condition
    def test_left_win_straight(self):
        self.assertEqual(poker_spades_game.play_cards('S6', 'S7', 'S8', 'SJ', 'SJ', 'SJ'), -1)

    def test_right_win_straight(self):
        self.assertEqual(poker_spades_game.play_cards('S5', 'S5', 'S5', 'S4', 'S2', 'S3'), 1)

    def test_tie_straight(self):
        self.assertEqual(poker_spades_game.play_cards('S5', 'S7', 'S6', 'S5', 'S6', 'S7'), 0)

    # Try win condition with royal flush
    def test_left_royal_flush(self):
        self.assertEqual(poker_spades_game.play_cards('SA', 'SQ', 'SK', 'SQ', 'SK', 'SJ'), -1)

    def test_right_royal_flush(self):
        self.assertEqual(poker_spades_game.play_cards('S6', 'S7', 'S8', 'SQ', 'SK', 'SA'), 1)

    def test_tie_royal_flush(self):
        self.assertEqual(poker_spades_game.play_cards('S6', 'S3', 'S8', 'SJ', 'SQ', 'SJ'), 0)


if __name__ == '__main__':
    unittest.main()
