from searching_framework import * #, just an example, import whatever you actually need from the searching framework
# note that your program won't work if you copy paste classes instead of import them via the above statement

# from searching_framework.uninformed_search import breadth_first_graph_search


# define your Problem class here

class Fudbal(Problem):
    def __init__(self, initial, protivnici, obrac, grid, goal=None):
        super().__init__(initial, goal)
        self.protivnici = protivnici
        self.obrac = obrac # stativa, goal_post
        self.grid = grid

    def check_valid(self, player, ball, protivnik1, protivnik2):
        playerx, playery = player
        ballx, bally = ball

        if not (0 <= playerx < self.grid[0] and 0 <= playery < self.grid[1]):
            return False

        if ball not in self.obrac:
            if not (0 <= ballx < self.grid[0] and 0 <= bally < self.grid[1]):
                return False

        for protivnik in [protivnik1, protivnik2]:
            px, py = protivnik

            if (playerx, playery) == (px, py):
                return False
            if ballx in range(px - 1, px + 2) and bally in range(py - 1, py + 2):
                return False

        return True

    def successor(self, state):
        successors = {}

        actions = ['up', 'down', 'right', 'up-right', 'down-right']
        directions = [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1)]

        protivnik1, protivnik2 = self.protivnici

        player, ball = state

        plx, ply = player
        bx, by = ball

        for (dx, dy), action in zip(directions,actions):

            npx, npy = plx + dx, ply + dy
            new_player = (npx, npy)

            if (npx, npy) == (bx, by):
                nbx, nby = bx + dx, by + dy

                new_ball = (nbx, nby)
                if self.check_valid(new_player, new_ball, protivnik1, protivnik2):
                    successors[f'Push ball {action}'] = (new_player, new_ball)

            else:
                if self.check_valid(new_player, ball, protivnik1, protivnik2):
                    successors[f'Move man {action}'] = (new_player, ball)

        return successors




    def goal_test(self, state):
        ball = state[1]
        obrac1, obrac2 = self.obrac # ((7, 3), (7, 4))
        return ball == obrac1 or ball == obrac2



    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


if __name__ == '__main__':
    # print("Read the input, create an instance of your problem class and use the searching algorithms here")
    player_start_pos = tuple(map(int, input().split(',')))
    ball_start_pos = tuple(map(int, input().split(',')))

    grid = (8,6)
    protivnici = ((3, 3), (5, 4))
    obrac = ((7, 2), (7, 3))

    initial = (player_start_pos, ball_start_pos)
    problem = Fudbal(initial, protivnici, obrac, grid)

    result = breadth_first_graph_search(problem)

    if result:
        print(result.solution())
    else:
        print("No Solution!")