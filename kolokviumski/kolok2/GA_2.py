import pygad
import numpy as np


def fitness_func(ga_instance, solution, solution_idx):
    # 1 4 5 3 6 ...
    timovi = []
    num_teams = len(solution) // 4

    for i in range(len(solution) // 4):
        tim = solution[i*4 : i*4+4]
        timovi.append(tim)

    tipovi = set(m[1] for m in mashini)

    najkratko = 99999

    for tip in tipovi:
        sum = 0
        for tim in timovi:
            vreminja = [mashini[int(i)][0] for i in tim]
            types = [mashini[int(i)][1] for i in tim]

            bool = True
            for type in types:
                if type != tip:
                    bool = False

            if bool:
                sum += min(vreminja)
            else:
                sum+=max(vreminja)

        if sum < najkratko:
            najkratko = sum

    return -najkratko



if __name__ == '__main__':
    # TODO: Read input
    n = int(input())
    mashini = []

    for i in range(n):
        vlez = input().split()
        vreme = vlez[0]
        tip = vlez[1]
        mashini.append((float(vreme), tip))


    num_teams = n // 4

    gene_space = list(range(n))

    params = {
        'num_generations': 300,
        'sol_per_pop': 50,
        'num_parents_mating': 20,
        'num_genes': n,  # TODO: fill empty params
        'gene_space': gene_space,
        'fitness_func': fitness_func,
        'mutation_num_genes': 1,


        'allow_duplicate_genes': False
    }

    ga = pygad.GA(**params)
    ga.run()

    best_solution, best_solution_fitness, _ = ga.best_solution()

    # Фитнесот е негативен, па го враќаме во позитивен за времето
    min_vreme = -best_solution_fitness

    # Треба да откриеме кој тип P го дал тоа најдобро време
    tipovi = set(m[1] for m in mashini)
    najdobar_P = None

    for tip in tipovi:
        vkupno = 0
        for i in range(num_teams):
            tim_indeksi = best_solution[i * 4: i * 4 + 4]
            types = [mashini[int(idx)][1] for idx in tim_indeksi]
            vreminja = [mashini[int(idx)][0] for idx in tim_indeksi]

            if all(t == tip for t in types):
                vkupno += min(vreminja)
            else:
                vkupno += max(vreminja)

        if vkupno == min_vreme:
            najdobar_P = tip
            break

    # Печатење на бараните информации
    print(f"Минимално време: {min_vreme}")
    print(f"Префериран тип: {najdobar_P}")
    print("Тимови:")
    for i in range(num_teams):
        tim_indeksi = best_solution[i * 4: i * 4 + 4]
        # Печати ги самите машини за овој тим (индекси или податоци)
        print(f"  Тим {i + 1}: {[int(idx) for idx in tim_indeksi]}")