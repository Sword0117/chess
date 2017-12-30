from configurations import *

# inherits from dictionary class in python
class Model(dict):
	captured_pieces = { 'white': [], 'black': [] }
	player_turn = None
	# number of turns played since the last capture or the pawn movement
	halfmove_clock = 0 
	# increments after each every black move
	full_move_number = 1
	history = []

	def __init__(self):
		pass

	def get_piece_at(self, position):
		return self.get(position)

	# returns alphanumeric position of the rowcol given.
	def get_alphanumeric_position(self, rowcol):
		if self.is_on_board(rowcol):
			row, col = rowcol
			return "{}{}".format(X_AXIS_LABELS[col], Y_AXIS_LABELS[row])

	def is_on_board(self, rowcol):
		row, col = rowcol
		return (0 <= row <= 7) and (0 <= col <= 7)