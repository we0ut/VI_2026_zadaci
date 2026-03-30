from searching_framework import Problem, astar_search

class Lavirint(Problem):
    def __init__(self, initial, walls, house, grid, num_walls):
        super().__init__(initial)
        self.walls = walls
        self.house = house
        self.grid = grid
        self.num_walls = num_walls

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def check_valid(self, man, nasoka):
        mx, my = man

        # if nasoka == 'Desno 2':
        #     return (mx, my) not in self.walls and 0 <= mx < self.grid[0] and 0 <= my < self.grid[1] and (mx - 1, my) not in self.walls
        # elif nasoka == 'Desno 3':
        #     return (mx, my) not in self.walls and 0 <= mx < self.grid[0] and 0 <= my < self.grid[1] and (mx - 1, my) not in self.walls and (mx - 2, my) not in self.walls
        #
        # return (mx, my) not in self.walls and 0 <= mx < self.grid[0] and 0 <= my < self.grid[1]
        if not (0 <= mx < self.grid[0] and 0 <= my < self.grid[1]):
            return False
        if (mx, my) in self.walls:
            return False

        if nasoka == 'Desno 2':
            return (mx - 1, my) not in self.walls
        if nasoka == 'Desno 3':
            return (mx - 1, my) not in self.walls and (mx - 2, my) not in self.walls

        return True

    def goal_test(self, state):
        man = state

        return man == self.house

    def successor(self, state):
        successors = {}

        mx, my = state

        nstate = (mx + 2, my)
        if self.check_valid(nstate, 'Desno 2'):
            successors["Desno 2"] = nstate

        nstate = (mx + 3, my)
        if self.check_valid(nstate, 'Desno 3'):
            successors["Desno 3"] = nstate

        # nstate = ((mx - 1) % self.grid[0] if mx == 0 else mx - 1, my)
        nstate = (mx-1, my)
        if self.check_valid(nstate, 'Levo'):
            successors["Levo"] = nstate

        nstate = (mx, my + 1)
        if self.check_valid(nstate, 'Gore'):
            successors["Gore"] = nstate

        nstate = (mx, my - 1)
        if self.check_valid(nstate, 'Dolu'):
            successors["Dolu"] = nstate

        return successors

    def h(self, node):
        state= node.state

        man = state
        mx, my = man
        hx, hy = self.house

        return abs(mx - hx) + abs(my - hy)




if __name__ == '__main__':
    n = int(input())
    num_walls = int(input())
    walls = []

    for i in range(num_walls):
        wx, wy = tuple(map(int, input().split(",")))
        walls.append((wx, wy))

    start = tuple(map(int, input().split(",")))
    house = tuple(map(int, input().split(",")))

    gx, gy = n, n

    initial = (start)

    problem = Lavirint(initial, walls, house, (gx, gy), num_walls)

    solution = astar_search(problem)

    if solution:
        print(solution.solution())
    else:
        print('No Solution!')