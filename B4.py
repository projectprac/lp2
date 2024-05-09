n = int(input("Enter the size of the board: "))
counter = 0

def reset():
    global board, counter
    board = [[0]*n for i in range(n)]
    if not marker(board, 0) and counter == 1:
        print("No feasible solution exists for the given dimensions")

def display(board):
    global counter
    counter += 1
    for i in range(0, n):
        for j in range(0, n):
            print(board[i][j], end="")
        print()
    print()

def check(board, row, column):
    for i in range(0, column):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n), range(column, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def marker(board, column):
    global counter
    possibility = False
    if column == n:
        display(board)
        return True
    for i in range(0, n):
        if check(board, i, column):
            board[i][column] = 1
            possibility = marker(board, column + 1) or possibility
            board[i][column] = 0
    return possibility

reset()
print("There are a total of " + str(counter) + " possibilities for the given dimensions!")


# 1. **CSP (Constraint Satisfaction Problem)**:

#     - **Definition**: A CSP is a problem represented by a set of variables, a domain of possible values for each variable, and a set of constraints that specify allowable combinations of values for subsets of variables.
  
#     - **Variables**: These are the unknowns we need to find values for. Each variable has a domain of possible values it can take.
  
#     - **Domains**: Each variable has a domain, which is a set of values that the variable can possibly take.
  
#     - **Constraints**: These are restrictions on the possible values of variables. They define which combinations of values are allowed.
  
#     - **Objective**: The objective in a CSP is to find an assignment of values to variables that satisfies all constraints.

#     - **Examples**: Sudoku, Map Coloring, Cryptarithmetic, Job Scheduling, etc.

# 2. **N-Queens Problem**:

#     - **Definition**: The N-Queens problem is a classic example of a CSP. It involves placing N queens on an N×N chessboard in such a way that no two queens threaten each other.
  
#     - **Variables**: In the N-Queens problem, each variable represents the column position of a queen on the chessboard.
  
#     - **Domains**: The domain of each variable is the set of row positions where the queen in that column can be placed without threatening any other queens.
  
#     - **Constraints**: The constraints in the N-Queens problem ensure that no two queens share the same row, column, or diagonal.
  
#     - **Objective**: The objective is to find a placement of N queens on the chessboard such that no two queens threaten each other.

#     - **Solution**: The solution to the N-Queens problem is a configuration of queens on the chessboard that satisfies all constraints.
  
#     - **Example**: For an 8×8 chessboard, the goal is to place 8 queens in such a way that no two queens share the same row, column, or diagonal.

# In summary, the N-Queens problem is a specific instance of a CSP where the goal is to place queens on a chessboard without any of them threatening each other, making it a classic problem studied in artificial intelligence and computer science.

