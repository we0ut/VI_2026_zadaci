import pygad


def read_input():
    M, N = map(int, input().split())
    K = int(input())
    B = int(input())

    unusable = set()
    for _ in range(B):
        r, c = map(int, input().split())
        unusable.add((r, c))

    return M, N, K, unusable


def fitness_func(ga_instance, solution, solution_idx):
    # TODO: implement fitness function
    sprinklers = list(set(map(int, solution)))
    num_sprinklers = len(sprinklers)

    sprinkler_coords = []

    for s in sprinklers:
        x = s//N
        y = s%N
        sprinkler_coords.append((x,y))

    romb = [(-2,0), (-1,0), (-1,-1), (1,0), (2,0), (0,0), (0,-1), (0,-2), (0,1), (0,2), (1,-1), (1,1), (-1,1),]

    crops_covered = set()
    for x,y in sprinkler_coords:
        for rx, ry in romb:
            crop_x, crop_y = rx+x, ry+y
            if 0 <= crop_x < M and 0 <= crop_y < N:
                crop = (crop_x, crop_y)
                if crop not in sprinkler_coords and crop not in unusable:
                    crops_covered.add(crop)

    num_covered = len(crops_covered)

    return num_covered - num_sprinklers


if __name__ == "__main__":
    M, N, K, unusable = read_input()

    params = {
        'num_generations': 100,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': K,  # TODO: fill empty params
        'gene_space': list(range(M*N)),
        'fitness_func': fitness_func,
        'mutation_num_genes': 1
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, _, _ = ga.best_solution()

    # TODO: Print required data
    sprinkler = set(best_solution)
    fitness = fitness_func(None,best_solution, 0)
    print(f'br na watered crops: {len(sprinkler)+fitness}')
    print(f'br na sprinklers: {len(sprinkler)}')
    for i in sprinkler:
        xx = i//N
        yy = i%N
        print(f'pos na sprinkler: ({xx}, {yy})')