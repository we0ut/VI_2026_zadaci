from errno import EADV

from constraint import *

problem = Problem(solver=BacktrackingSolver())

vari = list(range(1,17))
dom = list(range(1,17))

problem.addVariables(vari, dom)

# contraints
# contraint 1: each row must sum to 34
for i in range(4):
    row_variables = [1+i*4, 2+i*4, 3+i*4, 4+i*4 ]
    problem.addConstraint(ExactSumConstraint(34), row_variables)

# contraint 2: each col must sum to 34
for i in range(4):
    col_variables = [1+i, 5+i, 9+i, 13+i ]
    problem.addConstraint(ExactSumConstraint(34), col_variables)

# contraint 3: each diag must sum to 34
main_diag = [1, 6, 11, 16]
alt_diag = [4, 7, 10, 13]

problem.addConstraint(ExactSumConstraint(34), main_diag)
problem.addConstraint(ExactSumConstraint(34), alt_diag)

# constraint 4: all variables must be different
problem.addConstraint(AllDifferentConstraint(), vari)

print(problem.getSolution())