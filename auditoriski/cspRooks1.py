from constraint import *

problem = Problem(solver=BacktrackingSolver())

variables = []
domain = [0, 1]

# variables
for i in range(8):
    for j in range(8):
        problem.addVariable((i, j), domain)
        variables.append((i, j))

# constraints
# is there 8 rooks on the board
def cons_1(*vars):
    counter = 0
    for cell in vars:
        if cell == 1:
            counter += 1

    return counter == 8

# each row must have 1 rook
def cons_2(*vars):
    counter = 0
    for cell in vars:
        if cell == 1:
            counter += 1

    return counter == 1

problem.addConstraint(cons_1, variables)
for i in range(8):
    row = []
    cols = []
    for j in range(8):
        row.append((i, j))
        cols.append((j ,i))

    problem.addConstraint(cons_2, row)
    problem.addConstraint(cons_2, cols)

print(problem.getSolution())