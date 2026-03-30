from constraint import Problem, BacktrackingSolver, AllDifferentConstraint, ExactSumConstraint, MaxSumConstraint

if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]
    N = max(map(max, grid))  # Number of regions

    problem = Problem(solver=BacktrackingSolver())

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.
    variables = [(i, j) for i in range(K) for j in range(K)]
    domain = [0, 1]
    problem.addVariables(variables, domain)
    regions = {}
    for i in range(K):
        for j in range(K):
            cell = (i, j)

            reg = grid[i][j]
            if reg not in regions:
                regions[reg] = []

            regions[reg].append(cell)

    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.
    # 1) ima N dzvezdi
    problem.addConstraint(ExactSumConstraint(N), variables)

    # 2) sekoj region sodrzi najmnogu 2 dzvezdi
    for id in regions:
        problem.addConstraint(MaxSumConstraint(2), regions[id])

    # 3) Ѕвезди кои припаѓаат на различни региони не смеат да бидат поставени во иста редица или иста колона
    region_id = list(regions.keys())
    for i in range(len(region_id)):
        for j in range(i+1, len(region_id)):
            cells1 = regions[region_id[i]]
            cells2 = regions[region_id[j]]

            for c1 in cells1:
                for c2 in cells2:
                    if c1[0] == c2[0] or c1[1] == c2[1]:
                        problem.addConstraint(MaxSumConstraint(1), [c1, c2])

    # 4) Ѕвезди кои припаѓаат на ист регион не смеат да бидат ортогонално соседни (т.е. не смеат две ѕвезди да бидат директно лево, десно, горе или долу меѓу себе)
    for i in range(K):
        for j in range(K):
            if j+1<K and grid[i][j] == grid[i][j+1]:
                problem.addConstraint(MaxSumConstraint(1), [(i, j), (i, j+1)])

            if  i+1 < K and grid[i][j] == grid[i+1][j] :
                problem.addConstraint(MaxSumConstraint(1), [(i, j), (i+1, j)])


    result = problem.getSolution()

    # Ispechatete go reshenieto vo baraniot format.
    # Print the solution in the required format.

    if result:
        for i in range(K):
            red = []
            for j in range(K):
                if result[(i,j)] == 1:
                    red.append("*")
                else:
                    red.append(str(grid[i][j]))

            print(" ".join(red))
    else:
        print("No Solution!")
