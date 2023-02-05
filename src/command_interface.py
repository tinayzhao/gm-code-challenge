import time

# Utility class for command line prompting.
class CommandInterface:

	@staticmethod
	def start_new_game():
		print("Hello players! Welcome to a new game of Tic-Tac-Toe.\n")
		CommandInterface.print_rules()
		input("Press ENTER to confirm both players are ready to start the game.\n")
		print("=======================\n"
			  "======GAME START!======\n"
			  "=======================\n")
		time.sleep(1)

	@staticmethod
	def print_rules():
		print("The rules are: \n"
			  "1. The game is played on a grid that's 3 squares by 3 squares.\n"
			  "2. First Player is X, second player is O. Players take turns marking empty squares by inputting position of square.\n"
			  "3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.\n"
			  "4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.\n"
			 )

		print("Input positions:")
		# Prints out:
		# 1 | 2 | 3
		#---+---+---
		# 4 | 5 | 6  
		#---+---+---
		# 7 | 8 | 9
		row = [1,2,3]
		for i in range(3):
			print(" {} | {} | {} ".format(row[0] + 3 * i, row[1] + 3 * i, row[2] + 3 * i))
			# Do not print dividing line on last loop.
			if i !=  2:
				print("---+---+---")
		print()

	@staticmethod
	def play_turn(board, player):
		print("Player {}'s turn. Current board state:".format(player.rep))
		print(board)
		# Run loop until valid input is received and acted upon.
		while True:
			print("Input options:\n"
				  " - \"help\" to print rules\n"
			      " - \"mark <position>\" to make a move\n"
			      " - \"stop\" to end game\n"
			      " - \"skip\" to skip turn"
			     )
			answer = input("Type input: ").lower()
			if answer == "help":
				CommandInterface.print_rules()
			elif "mark" in answer:
				args = answer.strip().split()
				if len(args) < 2 or not args[1].isdigit():
					print("Invalid input. Try again.")
					continue
				square = int(args[1])
				result,err_msg = board.make_move(square, player)
				if result:
					break
				print(err_msg)
			elif answer == "stop":
				board.force_end = True
				break
			elif answer == "skip":
				print("Skipped Player {}'s turn.".format(player.rep))
				break
			else:
				print("Invalid input. Try again.")

	@staticmethod
	def log_end_game(end_msg, board):
		print(end_msg)
		print(board)

	@staticmethod
	def ask_play_again():
		while True:
			answer = input("Play again? Press Y for yes and N for no: ").lower()
			if answer == "y":
				return True
			elif answer == "n":
				return False
			else:
				print("Invalid input. Try again.")



