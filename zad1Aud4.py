from searching_framework import Problem, astar_search

class House(Problem):
    def __init__(self, initial, house, grid ):
        super().__init__(initial)
        self.house = house
        self.grid = grid

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def move_obs(self, o):
        ox, oy, odir = o

        if odir == "down":
            nox, noy = ox, oy - 1
            if noy >= 0:
                return nox, noy, odir
            else:
                return ox, oy, 'up'
        else:
            nox, noy = ox, oy + 1
            if noy < self.grid[1]:
                return nox, noy, odir
            else:
                return ox, oy, 'down'


    def successor(self, state):
        successors = {}

        man, o1, o2 = state
        mx, my = man

        no1 = self.move_obs(o1)
        no2 = self.move_obs(o2)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        actions = ['right', 'left', 'up', 'down']

        for (dx, dy), action in zip(directions, actions):
            nmx, nmy = mx + dx, my + dy
            if self.check_valid((nmx, nmy), no1, no2):
                successors[action] = ((nmx,nmy), no1, no2)

        return successors

    def goal_test(self, state):
        man = state[0]
        return man == self.house

    def check_valid(self, man, o1, o2):

        mx, my = man
        no1 = o1
        no2 = o2
        return (mx, my) != (no1[0], no1[1]) and (mx, my) != (no2[0], no2[1]) and 0 <= mx < self.grid[0] and 0 <= my < self.grid[1]

    def h(self, node):
        state = node.state
        mx, my = state[0]
        hx, hy = self.house

        return abs(mx - hx) // 2 + abs(my - hy)

if __name__ == '__main__':

    mx, my = 0, 2
    o1x, o1y, o1dir = 2, 5, 'down'
    o2x, o2y, o2dir = 5, 0, 'up'
    hx, hy = 7, 4
    gx, gy = 8, 6

    initial = ((mx, my), (o1x, o1y, o1dir), (o2x, o2y, o2dir))
    house = hx, hy
    grid = gx, gy

    problem = House(initial,house, grid)
    solution = astar_search(problem)

    print(astar_search(problem).solution())
    pass