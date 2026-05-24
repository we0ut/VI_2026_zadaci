import pygad
from sklearn.tree import DecisionTreeClassifier

dataset = [
    [2, 3, 1, 7, 0],
    [5, 6, 4, 3, 1],
    [1, 1, 2, 8, 1],
    [7, 8, 6, 4, 1],
    [3, 2, 1, 9, 0],
    [8, 7, 5, 2, 1],
    [4, 5, 2, 6, 1],
    [1, 3, 1, 9, 0],
    [9, 8, 7, 2, 1],
    [2, 2, 3, 8, 0]
]

# TODO: Split dataset here
X, y = [row[:-1] for row in dataset], [row[-1] for row in dataset]
split_index = int(0.75 * len(dataset))


train_X, train_y = X[:split_index], y[:split_index]
test_X, test_y = X[split_index:], y[split_index:]

def decode(solution):

    if solution[0] == 1:
        criterion = 'gini'
    else:
        criterion = 'entropy'

    max_depth = int(solution[1])
    min_samples_split = int(solution[2])
    max_leaf_nodes = int(solution[3])

    params = {
        'criterion': criterion,
        'max_depth': max_depth,
        'min_samples_split': min_samples_split,
        'max_leaf_nodes': max_leaf_nodes
    }

    return params


def fitness_func(ga_instance, solution, solution_idx):
    # TODO: Define fitness function

    params = decode(solution)

    criterion = params['criterion']
    max_depth = params['max_depth']
    min_samples_split = params['min_samples_split']
    max_leaf_nodes = params['max_leaf_nodes']

    model = DecisionTreeClassifier(**params)
    model.fit(train_X, train_y)

    acc = model.score(test_X, test_y)

    value = acc - max_depth*10 - max_leaf_nodes*10

    return value


# 1 za gini, 2 za entropy
gene_space = [[1,2], [5, 10, 15, 20, 25], [2, 3, 4, 5, 10], [5, 10, 15, 20, 25]]

ga_instance = pygad.GA(
    num_generations=40,
    sol_per_pop=50,
    num_parents_mating=25,
    fitness_func=fitness_func,
    num_genes=4,  # TODO: Define missing params
    gene_space=gene_space,
    mutation_num_genes=1
)

ga_instance.run()
best_solution, _, _ = ga_instance.best_solution()

# TODO: Print best params and accuracy of best model

params = decode(best_solution)

model = DecisionTreeClassifier(**params)
model.fit(train_X, train_y)
acc = model.score(test_X, test_y)

for k in params.keys():
    print(f'{k} = {params.get(k)}')
print(f'acc = {acc}')