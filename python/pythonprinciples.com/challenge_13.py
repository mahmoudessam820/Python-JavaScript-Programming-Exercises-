"""
    level of challenge 4/10

    Tic tac toe input

    - Here's the backstory for this challenge: 
    - imagine you're writing a tic-tac-toe game, where the board looks like this:
        
        1:  X | O | X
            -----------
        2:    |   |  
            -----------
        3:  O |   |
            A   B  C

    The board is represented as a 2D list:

    board = [
        ["X", "O", "X"],
        [" ", " ", " "],
        ["O", " ", " "],
    ]

    - Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board.
    - To do so, you need to translate from the string "C1" to row 0 and column 2
    - so that you can check board[row][column].

    - Your task is to write a function that can translate from strings of length 2 to a tuple (row, column).
    - Name your function get_row_col.
    - it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

    For example:

    - Calling get_row_col("A3") should return the tuple (2, 0).
    - Because A3 corresponds to the row at index 2 and column at index 0 in the board.

    Hint:

    - First, use indexing to extract the number and letter.
    - Use int() to cast the number from a string to an int.
    - You can use a dictionary to translate the letter into a number.
    - Return the result as a tuple: (row, column).

"""

# My Solution 

board = [
    ["X", "O", "X"], # 1
    [" ", " ", " "], # 2
    ["O", " ", " "], # 3
]   # A    B    C

def get_row_col(tic_tac):
    tic = tic_tac.upper()
    col = tic[0]
    row = int(tic[1]) - 1

    board_keys = {"A": 0, "B": 1, "C": 2}

    for key in board_keys:
        if key == col:
            column = board_keys[key]
            return (row, column)

print(get_row_col("c1"))


# Another solution 

def get_row_col(choice):
    translate = {"A": 0, "B": 1, "C": 2}
    letter = choice[0]
    number = choice[1]
    row = int(number) - 1
    column = translate[letter]
    return (row, column)