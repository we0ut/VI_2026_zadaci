from searching_framework import Problem, astar_search

class Robot(Problem):
    def __init__(self, initial, grid, walls, capacity):
        super().__init__(initial)
        self.capacity = capacity
        self.grid = grid
        self.walls = walls

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def check_valid(self, robot, kapacitet):
        rx, ry = robot

        if not (0 <= rx < self.grid[0] and 0 <= ry < self.grid[1]):
            return False

        if (rx, ry) in self.walls:
            return False

        if kapacitet < 0:
            return False

        return True


    def goal_test(self, state):
        robot, celno_pole, stanici_polnenje, momentalno = state
        rx, ry = robot

        return (rx, ry) == celno_pole


    def successor(self, state):
        successor = {}

        robot, celno_pole, stanici_polnenje, momentalno = state

        rx, ry = robot
        cx, cy = celno_pole
        stanici = stanici_polnenje
        sega = momentalno

        actions = ["Up", "Down", "Left", "Right"]
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for (dx, dy), action in zip(directions, actions):
            nrx, nry = rx + dx, ry + dy
            new_capacity = sega - 1
            if self.check_valid((nrx, nry), new_capacity):
                if (nrx, nry) in stanici:
                    new_capacity = self.capacity
                successor[action] = ((nrx, nry), celno_pole, stanici, new_capacity)
                # if sega <= 2 and stanici:
                #     current_min = min(abs(rx - sx) + abs(ry - sy) for sx, sy in stanici)
                #     new_min = min(abs(nrx - sx) + abs(nry - sy) for sx, sy in stanici)
                #     if new_min < current_min:
                #         successor[action] = ((nrx, nry), celno_pole, stanici, new_capacity)
                # else:
                #     successor[action] = ((nrx, nry), celno_pole, stanici, new_capacity)



        return successor

    def h(self, node):
        state = node.state

        robot = state[0]
        rx, ry = robot

        celno = state[1]
        cx, cy = celno

        return abs(rx - cx) + abs(ry - cy)

if __name__ == '__main__':
    walls = [
        (0, 9), (1, 9), (2, 9), (3, 9), (1, 7), (3, 6), (7, 6), (8, 6), (9, 6), (4, 0), (5, 0),
    ]

    gx, gy = 10, 10

    robot_poz = tuple(map(int, input().split(",")))
    celno_pole = tuple(map(int, input().split(",")))
    capacity = int(input())
    n = int(input())
    stanici_polnenje = []

    for i in range(n):
        xi, yi = map(int, input().split(","))
        stanici_polnenje.append((xi, yi))

    momentalno = capacity

    initial = (robot_poz, celno_pole, tuple(stanici_polnenje), momentalno)
    problem = Robot(initial, (gx, gy), walls, capacity)

    res = astar_search(problem)

    if res:
        print(res.solution())
    else:
        print("No Solution!")