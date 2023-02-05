# Class that represents Tic-Tac-Toe board.
class Board:

	def __init__(self):
		# Set up win trackers.
		self.rows = [0] * 3
		self.cols = [0] * 3
		self.diag = 0
		self.anti_diag = 0
		self.diag_squares = {1,5,9}
		self.anti_diag_squares = {3,5,7}

		self.num_moves = 0
		self.force_end = False

		# Set up board for display.
		self.board = [[" " for _ in range(3)] for _ in range(3)]

		# Maps square to board position.
		self.square_map = { 
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

	# Makes move for player. If move is successful, return true. If not, return false.
	def make_move(self, square, player):
		if square not in self.square_map:
			return (False, "Square position doesn't exist. Query rules for positions.")
		row, col = self.square_map[square]
		if self.board[row][col] != " ":
			return (False, "Square position is already filled. Choose an empty position.")
		self.num_moves += 1
		self.board[row][col] = player.rep
		self.rows[row] += player.ref
		self.cols[col] += player.ref
		if square in self.diag_squares:
			self.diag += player.ref
		if square in self.anti_diag_squares:
			self.anti_diag += player.ref
		return (True, "")

	# If player is winner, return true. Otherwise, return false.
	def find_winner(self, player):
		win_num = player.ref * 3
		if win_num in self.rows or win_num in self.cols \
		   or win_num == self.diag or win_num == self.anti_diag:
		    return True
		return False

	def check_for_tie(self):
		return self.num_moves >= 9

	def clear(self):
		self.rows = [0] * 3
		self.cols = [0] * 3
		self.diag = 0
		self.anti_diag = 0
		self.num_moves = 0
		self.board = [[" " for _ in range(3)] for _ in range(3)]

	# Return string representation of board.
	# Example:
	# X |   | O
	#---+---+---
	#   | O |   
	#---+---+---
	#   |   | X
	def get_board_rep(self):
		result = ""
		for i in range(len(self.board)):
			row = self.board[i]
			result += " {} | {} | {} \n".format(row[0], row[1], row[2])
			if i != len(self.board) - 1:
				result += "---+---+---\n"
		return result

	def __repr__(self):
		return self.get_board_rep()

	def __str__(self):
		return self.get_board_rep()
