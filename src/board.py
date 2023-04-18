# Class that represents Tic-Tac-Toe board.
class Board:

	# Stores board squares for diagonal scoring.
	diag_squares = {1,5,9}
	anti_diag_squares = {3,5,7}

	# Maps square to board position.
	square_map = \
		{ 
		  1: (0,0),
		  2: (0,1),
		  3: (0,2),
		  4: (1,0),
		  5: (1,1),
		  6: (1,2),
		  7: (2,0),
		  8: (2,1),
		  9: (2,2)
		}

	def __init__(self):
		# Set up attributes to track win.
		self._rows = [0] * 3
		self._cols = [0] * 3
		self._diag = 0
		self._anti_diag = 0

		self._num_moves = 0
		self._force_end = False

		# Set up board for display.
		self._board = [[" " for _ in range(3)] for _ in range(3)]

	# Makes move for player. If move is successful, return true. If not, return false.
	def make_move(self, square, player):
		if square not in Board.square_map:
			return (False, "Square position doesn't exist. Query rules for positions.")
		row, col = Board.square_map[square]
		if self._board[row][col] != " ":
			return (False, "Square position is already filled. Choose an empty position.")
		self._num_moves += 1
		self._board[row][col] = player.get_rep()
		self._rows[row] += player.get_ref()
		self._cols[col] += player.get_ref()
		if square in Board.diag_squares:
			self._diag += player.get_ref()
		if square in Board.anti_diag_squares:
			self._anti_diag += player.get_ref()
		return (True, "")

	# If player is winner, return true. Otherwise, return false.
	def find_winner(self, player):
		win_num = player.get_ref() * 3
		if win_num in self._rows or win_num in self._cols \
		   or win_num == self._diag or win_num == self._anti_diag:
		    return True
		return False

	# If no one has won by 9 moves, there are no more squares left
	# to fill and game is a tie.
	def check_for_tie(self):
		return self._num_moves >= 9

	def check_for_end(self):
		return self._force_end

	def prepare_force_end(self):
		self._force_end = True

	# Return string representation of board.
	# Example:
	# X |   | O
	#---+---+---
	#   | O |   
	#---+---+---
	#   |   | X
	def get_board_rep(self):
		result = ""
		for i in range(len(self._board)):
			row = self._board[i]
			result += " {} | {} | {} \n".format(row[0], row[1], row[2])
			if i != len(self._board) - 1:
				result += "---+---+---\n"
		return result

	def __repr__(self):
		return self.get_board_rep()

	def __str__(self):
		return self.get_board_rep()
