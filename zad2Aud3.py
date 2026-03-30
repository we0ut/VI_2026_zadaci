from searching_framework import Problem
from searching_framework.uninformed_search import breadth_first_graph_search

def move_atom(x, y, dx, dy, others, obstacles):
    while True:
        nx, ny = x + dx, y + dy
        if not (0 <= nx <= 8):
            break
        if not (0 <= ny <= 6):
            break
        if [nx, ny] in obstacles:
            break
        if (nx, ny) in others:
            break
        x, y = nx, ny
    return x,y


class Molecule(Problem):
    def __init__(self, obstacles, initial, goal=None):
        super().__init__(initial, goal)
        self.obstacles = obstacles

    def successor(self, state):
        successors = {}

        (h1x, h1y), (ox, oy), (h2x, h2y) = state
        positions = {
            "h1": (h1x, h1y),
            "o": (ox, oy),
            "h2": (h2x, h2y)
        }

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        actions = ['Right', 'Left', 'Up', 'Down']

        for atom, (x, y) in positions.items():
            others = {pos for name, pos in positions.items() if name != atom}
            for (dx, dy), action in zip(directions, actions):
                nx, ny = move_atom(x, y, dx, dy, others, self.obstacles)
                if (nx, ny) != (x, y):
                    nh1 = (nx, ny) if atom == 'h1' else (h1x, h1y)
                    no = (nx, ny) if atom == 'o' else (ox, oy)
                    nh2 = (nx, ny) if atom == 'h2' else (h2x, h2y)
                    successors[f'{action}{atom.upper()}'] = (nh1, no, nh2)

        return successors

    def goal_test(self, state):
        # za da bide true treba da bide H1-O-H2
        (h1x, h1y), (ox, oy), (h2y, h2y) = state
        return h1y == oy == h2y and h1x + 1 == ox and ox + 1 == h2x



    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]





if __name__ == '__main__':
    obs = [[0, 1], [1, 1], [1, 3], [2, 5], [3, 1], [3, 6], [4, 2], [5, 6], [6, 1], [6, 2], [6, 3], [7, 3], [7, 6], [8, 5]]
    h1x, h1y = 2, 1
    h2x, h2y = 2, 6
    ox, oy = 7, 2

    initial = ((h1x, h1y), (ox, oy), (h2x, h2y))

    molecule = Molecule(obs, initial)

    print(breadth_first_graph_search(molecule).solution())