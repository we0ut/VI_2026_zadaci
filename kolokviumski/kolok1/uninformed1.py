from searching_framework import *

class Box(Problem):
    def __init__(self, initial, end_point):
        super().__init__(initial, None)
        self.end_point = end_point

    def goal_test(self, state):

        man, box1, box2 = state
        mx, my = man
        b1x, b1y = box1
        b2x, b2y = box2

        return (b1x,b1y) == (4,4) and (b2x, b2y) == (4,4)

    @staticmethod
    def check_valid(man, turnata, stoi):
        mx, my = man
        tx, ty = turnata
        sx, sy = stoi

        if (sx, sy) == (4,4):
            return 0 <= mx < 5 and 0 <= my < 5

        return 0 <= mx < 5 and 0 <= my < 5 and (tx, ty) != (sx, sy)

    def successor(self, state):
        succ = {}

        man, box1, box2 = state

        mx, my = man
        b1x, b1y = box1
        b2x, b2y = box2

        actions = ['up', 'down', 'left', 'right']
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        for (dx, dy), action in zip(direction, actions):
            nmx, nmy = mx+dx, my+dy

            if (nmx, nmy) == (b1x, b1y):
                nbx, nby = b1x+dx, b1y+dy
                if self.check_valid((nmx, nmy), (nbx, nby), (b2x, b2y)):
                    succ[f'Push box 1 {action}']=((nmx, nmy), (nbx, nby), (b2x, b2y))

            elif (nmx, nmy) == (b2x, b2y):
                nbx, nby = b2x + dx, b2y + dy
                if self.check_valid((nmx, nmy), (nbx, nby), (b1x, b1y)):
                    succ[f'Push box 2 {action}'] = ((nmx, nmy), (b1x, b1y), (nbx, nby))
            else:
                if self.check_valid((nmx, nmy), (b1x, b1y), (b2x, b2y)):
                    succ[f'Move man {action}'] = ((nmx, nmy), (b1x, b1y), (b2x, b2y))


        return succ

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # ((x1, y1), (x2, y2), (x3, y3))
    initial_state = (tuple(map(int, input().split(','))),
                     tuple(map(int, input().split(','))),
                     tuple(map(int, input().split(','))))

    box = Box(initial_state, (4, 4))

    result = breadth_first_graph_search(box)

    if result is not None:
        print(result.solution())
    else:
        print("No Solution!")