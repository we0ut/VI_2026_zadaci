from constraint import *

problem = Problem(solver=BacktrackingSolver())


variables = list(range(8))
domain = list(range(8))

problem.addVariables(variables, domain)

problem.addConstraint(AllDifferentConstraint(), variables)

print(problem.getSolution())