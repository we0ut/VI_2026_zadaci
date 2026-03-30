
from searching_framework import Problem, depth_first_graph_search
from searching_framework.uninformed_search import breadth_first_graph_search, depth_first_graph_search

class House_Problem(Problem):

    def __init__(self, initial, house, grid):
        super().__init__(initial)
        self.house = house
        self.grid = grid

    def goal_test(self, state):
        man = state[0]
        return man == self.house

    def move_obstacle(self, o):
        ox, oy, odir = o
        if odir == 'down':
            nox, noy = ox, oy - 1
            if noy >= 0:
                return nox, noy, odir
            else:
                return ox,oy,'up'
        else: # odir == 'up'
            nox, noy = ox, oy + 1
            if noy >= 6:
                return nox, noy, odir
            else:
                return ox,oy,'down'

    def check_valid(self, man, o1, o2):
        manx, many = man
        no1 = o1
        no2 = o2
        return (manx, many) != (no1[0], no1[1]) and (manx, many) != (no2[0], no2[1]) and 0 <= manx < self.grid[0] and 0 <= many < self.grid[1]

    def successor(self, state):
        successors = {}

        man, o1, o2 = state
        mx, my = man

        no1 = self.move_obstacle(o1)
        no2 = self.move_obstacle(o2)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        actions = ['Right', 'Left', 'Up', 'Down']

        for (dx, dy), action in zip(directions, actions):
            nmx, nmy = mx+dx, my+dy
            if self.check_valid((nmx,nmy), no1, no2):
                successors[action] = ((nmx, nmy), no1, no2)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]



if __name__ == '__main__':
    mx, my = 0, 2
    o1x, o1y, o1dir = 2, 5,'down'
    o2x, o2y, o2dir = 0, 5, 'up'

    hx, hy = 7, 4
    grid_x ,grid_y = 8, 6

    initial = ((mx, my), (o1x, o1y, o1dir), (o2x, o2y, o2dir))
    house = hx, hy
    grid = grid_x, grid_y

    problem = House_Problem(initial, house, grid)

    print(depth_first_graph_search(problem).solution())