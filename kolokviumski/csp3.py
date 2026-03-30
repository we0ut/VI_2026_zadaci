from constraint import *

if __name__ == '__main__':
    solver = input()

    if solver == "BacktrackingSolver":
        problem = Problem(BacktrackingSolver())
    elif solver == "RecursiveBacktrackingSolver":
        problem = Problem(RecursiveBacktrackingSolver())
    else:
        problem = Problem(MinConflictsSolver())

    # variables
    K = 81
    variables = [i for i in range(K)]
    domain = [i for i in range(1,10)]

    problem.addVariables(variables, domain)

    # constraints
    # 1) proverka za red
    for i in range(9):
        row_vars = [i*9 + j for j in range(9)]
        problem.addConstraint(AllDifferentConstraint(), row_vars)

    # 2) proverka za kolonite
    for j in range(9):
        col_vars = [i*9 + j for i in range(9)]
        problem.addConstraint(AllDifferentConstraint(), col_vars)

    # 3) vo blokot ne smee da se povtoruva niedna cifra
    i = 1
    counter = 0
    while i < K:

        red1 = [i-1, i, i+1]
        red2 = [i+8, i+9, i+10]
        red3 = [i+17, i+18, i+19]

        problem.addConstraint(AllDifferentConstraint(), red1 + red2 + red3)
        # print(i)

        if counter < 2:
            i += 3
            counter += 1
        else:
            i += 21
            counter = 0

    res = problem.getSolution()

    if res is not None:
        print(res)
    else:
        print("None")