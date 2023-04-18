import time

from board import Board
from command_interface import CommandInterface
from player import Player

# Main class to run Tic-Tac-Toe game.
class Game:

	def play_new_game(self):
		board = Board()
		player1 = Player("X", 1)
		player2 = Player("O", -1)
		players = [player1, player2]
		turn = 0
		CommandInterface.start_new_game()
		# The while loop keeps the game running until there is a tie
		# or win that breaks the loop.
		while True:
			current_player = players[turn]
			CommandInterface.play_turn(board, current_player)
			if self.can_end_game(board, current_player):
				break
			# Switches turn between 0 and 1 to swap between players.
			turn = 1 - turn
			time.sleep(1)
			print("======Moving onto next turn!======\n")
			time.sleep(2)
		# Game has ended.
		time.sleep(2)
		return CommandInterface.ask_play_again()

	# Check if program can declare end of game.
	def can_end_game(self, board, current_player):
		if board.find_winner(current_player):
			win_msg = "Congratulations, Player " + current_player.get_rep() + ", you have won!"
			CommandInterface.log_end_game(win_msg, board)
			return True
		elif board.check_for_tie():
			tie_msg = "Tie game. No one has won or lost."
			CommandInterface.log_end_game(tie_msg, board)
			return True
		elif board.check_for_end():
			force_end_msg = "Forced end of game."
			CommandInterface.log_end_game(force_end_msg, board)
			return True
		return False

def main():
	game = Game()
	while True:	
		if not game.play_new_game():
			# End program if player does not want to start new game.
			break
	print("Closing program.")
	time.sleep(1)
	print("======Thanks for playing!======")
	time.sleep(1)

if __name__ == "__main__":
	main()
