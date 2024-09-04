import checkers


# game asks the user for the size of the checkers board they want and makes sure it is between 4 and 16
def game():
    while True:
        board_size = input("Please enter a number 4 to 16 to determine board size: ")
        try:
            board_size = int(board_size)
            if 4 <= board_size <= 16:
                break
            else:
                print("Please enter a valid number as directed.\n")
        except ValueError:
            print("Please enter a valid number as directed.\n")
    # calls checkers file to build the board size
    board = checkers.build_board(board_size)
    print(board)
    # counts the number of times each color shows up on the board then prints out the total
    count_red = checkers.get_count(board, "Red")
    count_black = checkers.get_count(board, "Black")
    count_empty = checkers.get_count(board, "Empty")
    print(f"There are {count_red} Red squares, {count_black} Black squares, and {count_empty} Empty squares.")


# checks to see if this file is running as main
if __name__ == "__main__":
    game()
