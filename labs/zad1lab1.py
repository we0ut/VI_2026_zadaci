from searching_framework import *


class Robot(Problem):
    def __init__(self, initial, walls, M1_pos, M2_pos, M1_steps, M2_steps, grid, parts_M1, parts_M2, goal=None):
        super().__init__(initial, goal)
        self.walls = walls
        self.M1_steps = M1_steps
        self.M2_steps = M2_steps
        self.M1_pos = M1_pos
        self.M2_pos = M2_pos
        self.grid = grid
        self.parts_M1 = parts_M1
        self.parts_M2 = parts_M2

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        collectedM1, collectedM2 = state[1], state[2]
        repair_progress_M1, repair_progress_M2 = state[3], state[4]

        return len(collectedM1) == 0 and len(collectedM2) == 0 and repair_progress_M1 == self.M1_steps and repair_progress_M2 == self.M2_steps

    def check_valid(self, robot):

        robotx, roboty = robot

        return 0 <= robotx < self.grid[0] and 0 <= roboty < self.grid[1] and (robotx, roboty) not in self.walls

    def successor(self, state):
        successors = {}

        # dir = {"Up": (0, 1), "Down": (0, -1), "Left": (-1, 0), "Right": (1, 0)}  % self.grid[0/1]
        actions = ['Up', 'Down', 'Left', 'Right']
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        robot, to_collect_M1, to_collect_M2, repair_progress_M1, repair_progress_M2 = state

        robotx, roboty = robot
        m1x, m1y = self.M1_pos
        m2x, m2y = self.M2_pos

        for (dx, dy), action in zip(directions, actions):

            nrx, nry = robotx+dx, roboty+dy
            new_pos = (nrx, nry)

            if self.check_valid(new_pos):
                new_to_collect_M1 = tuple(p for p in to_collect_M1 if p != new_pos)


                if repair_progress_M1 == self.M1_steps:
                    new_to_collect_M2 = tuple(p for p in to_collect_M2 if p != new_pos)
                else:
                    new_to_collect_M2 = to_collect_M2

                new_repair_M1 = 0 if (robotx, roboty) == self.M1_pos and repair_progress_M1 < self.M1_steps else repair_progress_M1
                new_repair_M2 = 0 if (robotx, roboty) == self.M2_pos and repair_progress_M2 < self.M2_steps else repair_progress_M2

                successors[action] = (new_pos, new_to_collect_M1, new_to_collect_M2, new_repair_M1, new_repair_M2)

        if (robotx, roboty) == self.M1_pos and len(to_collect_M1) == 0 and repair_progress_M1 < self.M1_steps:
            new_repair_M1 = repair_progress_M1 + 1
            successors['Repair'] = (robot, to_collect_M1, to_collect_M2, new_repair_M1, repair_progress_M2)
        elif repair_progress_M1 == self.M1_steps and (robotx, roboty) == self.M2_pos and repair_progress_M2 < self.M2_steps and len(to_collect_M2) == 0:
            new_repair_M2 = repair_progress_M2 + 1
            successors['Repair'] = (robot, to_collect_M1, to_collect_M2, repair_progress_M1, new_repair_M2)

        return successors


if __name__ == '__main__':
    robot_start_pos = tuple(map(int, input().split(',')))
    M1_pos = tuple(map(int, input().split(',')))
    M1_steps = int(input())
    M2_pos = tuple(map(int, input().split(',')))
    M2_steps = int(input())
    parts_M1 = int(input())
    to_collect_M1 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M1)])
    parts_M2 = int(input())
    to_collect_M2 = tuple([tuple(map(int, input().split(','))) for _ in range(parts_M2)])

    walls = [(4, 0), (5, 0), (7, 5), (8, 5), (9, 5), (1, 6), (1, 7), (0, 6), (0, 8), (0, 9), (1, 9), (2, 9), (3, 9)]

    repair_progress_M1, repair_progress_M2 = 0, 0

    initial = (
        robot_start_pos,
        to_collect_M1,
        to_collect_M2,
        repair_progress_M1,
        repair_progress_M2
    )

    grid = (10,10)
    problem = Robot(initial, walls, M1_pos, M2_pos, M1_steps, M2_steps, grid, parts_M1, parts_M2)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")
