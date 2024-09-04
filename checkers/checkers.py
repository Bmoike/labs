from numpy import random

# checks make sure this file is not running as main
if __name__ == "__main__":
    print("Please do not run this file directly. It should be imported from a separate main.py file.")

else:
    # function to build a board with specified colors at random intervals
    def build_board(size):
        board_size = random.choice(["Empty", "Red", "Black"], (size, size))
        return board_size

    # counts the number of times a specific color has appeared on the board
    def get_count(checker_board, color):
        total = checker_board == color
        return total.sum()
