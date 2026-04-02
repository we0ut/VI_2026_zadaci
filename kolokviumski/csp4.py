from constraint import *

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # variables
    n = int(input())
    variables = range(1, n+1)
    domain = [(i,j) for i in range(n) for j in range(n)]

    problem.addVariables(variables,domain)

    # 1) dali ima n kralici
    problem.addConstraint(AllDifferentConstraint(), variables)

    # 2) da ne se u isti red
    pairs=[]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if not(j,i) in pairs and i!=j:
                pairs.append((i,j))


    def constraint_1(a, b):
        x1, y1 = a
        x2, y2 = b
        if x1 == x2 or y1 == y2 or (abs(x1 - x2) == abs(y1 - y2)):
            return False
        return True


    for (a, b) in pairs:
        problem.addConstraint(constraint_1, [a, b])







    if n <= 6:

        solutions = problem.getSolutions()
        print(len(solutions))
    elif n>6:

        solution = problem.getSolution()
        print(solution)
    else:
        print("No Solution!")