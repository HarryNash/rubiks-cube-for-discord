import unittest

from commands import hands, custom, text, ALL_MOVES

from db import create_cube_if_channel_has_none, delete_cube, append_movements_to_cube

TEST_CHANNEL_ID = '00'

def reset_test_cube():
	"""Creates an entry in the database for a solved cube."""
	delete_cube(TEST_CHANNEL_ID)
	create_cube_if_channel_has_none(TEST_CHANNEL_ID)

class TestUM(unittest.TestCase):

	def setUp(self):
		pass

	def test_hands_nothing(self):
		self.assertIsNone(hands(TEST_CHANNEL_ID, ''))

	def test_hands_punctuation(self):
		self.assertIsNone(hands(TEST_CHANNEL_ID, ' \t \n   '))

	def test_hands_all_moves(self):
		self.assertIsNone(hands(TEST_CHANNEL_ID, ' '.join(ALL_MOVES)))

	def test_hands_basic(self):
		self.assertIsNone(hands(TEST_CHANNEL_ID, 'S'))

	def test_hands_basic(self):
		self.assertIsNotNone(hands(TEST_CHANNEL_ID, 'P'))

	def test_hands__bad_start(self):
		self.assertIsNotNone(hands(TEST_CHANNEL_ID, 'T x2 y'))

	def test_hands__bad_end(self):
		self.assertIsNotNone(hands(TEST_CHANNEL_ID, 'x R J'))


	def test_custom_nothing(self):
		reset_test_cube()
		self.assertIsNotNone(custom(TEST_CHANNEL_ID, ''))

	def test_custom_bad_length(self):
		reset_test_cube()
		self.assertIsNotNone(custom(TEST_CHANNEL_ID, 'rrrrrrrrrroooooooooogg'))

	def test_custom_bad_colours(self):
		reset_test_cube()
		self.assertIsNotNone(custom(TEST_CHANNEL_ID,
			'rrzrrrrrryyyyyyyyygggggggggwwwwwwwwwooooooooobbbbbbbbb'))

	def test_custom_impossible_cube(self):
		reset_test_cube()
		self.assertIsNotNone(custom(TEST_CHANNEL_ID, 'r' * 54))

	def test_custom_solved_cube(self):
		reset_test_cube()
		self.assertIsNone(custom(TEST_CHANNEL_ID,
			'rrrrrrrrryyyyyyyyygggggggggwwwwwwwwwooooooooobbbbbbbbb'))

	def test_custom_right_rotate_90_clockwise_cube(self):
		reset_test_cube()
		self.assertIsNone(custom(TEST_CHANNEL_ID,
			'rrrrrrrrryygyygyygggwggwggwwwbwwbwwboooooooooybbybbybb'))

	
	def test_append_basic(self):
		reset_test_cube()

		append_movements_to_cube(TEST_CHANNEL_ID, 'y z E')
		progress = append_movements_to_cube(TEST_CHANNEL_ID, 'M M2 M\'')

		self.assertEqual(progress, ' y z E M M2 M\'')

	def test_delete_clears_preexisting(self):
		reset_test_cube()

		append_movements_to_cube(TEST_CHANNEL_ID, 'L M B')
		delete_cube(TEST_CHANNEL_ID)

		progress = append_movements_to_cube(TEST_CHANNEL_ID, '')

		self.assertEqual(progress, '')

	def test_create_does_not_clear_preexisting(self):
		reset_test_cube()

		append_movements_to_cube(TEST_CHANNEL_ID, 'x R R2')
		create_cube_if_channel_has_none(TEST_CHANNEL_ID)
		progress = append_movements_to_cube(TEST_CHANNEL_ID, '')

		self.assertEqual(progress, ' x R R2')


if __name__ == '__main__':
	unittest.main()
