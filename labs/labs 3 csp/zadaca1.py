from constraint import *


if __name__ == '__main__':
    K = int(input())
    grid = [list(map(int, input().split())) for _ in range(K)]
    N = max(map(max, grid))  # Number of regions

    problem = Problem(solver=BacktrackingSolver())

    # Dodadete gi promenlivite i domenite tuka.
    # Add the variables and domains here.

    regions = {}
    variables = []
    domain = [0, 1]

    for i in range(K):
        for j in range(K):

            cell = (i, j)
            problem.addVariable(cell, domain)
            variables.append(cell)

            region_id = grid[i][j]
            if region_id not in regions:
                regions[region_id] = []

            regions[region_id] += [cell]


    # Dodadete gi ogranichuvanjata tuka.
    # Add the constraints here.
    # 1) mora da ima N dzvezdi
    problem.addConstraint(ExactSumConstraint(N), variables)

    # 2) sekoj region sodrzi najmnogu 2 dzvezdi
    for id in regions:
        problem.addConstraint(MaxSumConstraint(2), regions[id])

    # 3) 2 dzezdi od razlicen region ne mozat da se na ista redica ili kolona
    ids = list(regions.keys())
    for i in range(len(regions.keys())):
        for j in range(i+1, len(regions.keys())):
            cells1 = regions[ids[i]]
            cells2 = regions[ids[j]]
            for c1 in cells1:
                for c2 in cells2:
                    if c1[0] == c2[0] or c1[1] == c2[1]:
                        problem.addConstraint(MaxSumConstraint(1), [c1, c2])

    # 4) dzvezdi od isti region ne mozat da se 1 levo desno gore ili dole oddaleceni
    for rc in regions.values():
        for i in range(len(rc)):
            for j in range(i+1, len(rc)):
                c1 = rc[i]
                c2 = rc[j]
                if abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]) == 1:
                    problem.addConstraint(MaxSumConstraint(1), [c1, c2])

    result = problem.getSolution()

    # Ispechatete go reshenieto vo baraniot format.
    # Print the solution in the required format.
    if result:
        for i in range(K):
            res_row = []
            for j in range(K):
                if result[(i,j)] == 1:
                    res_row.append("*")
                else:
                    res_row.append(str(grid[i][j]))
            print(" ".join(res_row))
    else:
        print("No Solution!")
