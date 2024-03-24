import bisect
from searching_framework import Problem, breadth_first_graph_search


def manhattan_distance(node1, node2):
    x1 = int(node1[0])
    y1 = int(node1[1])
    x2 = int(node2[0])
    y2 = int(node2[1])
    return abs(x1 - x2) + abs(y1 - y2)


class Football(Problem):
    def __init__(self,initial,opponents_pos,goal_pos):
        super().__init__(initial)
        self.goal_pos = goal_pos
        self.opponents_pos = opponents_pos
        self.width = 8
        self.height = 6

    def successor(self, state):
        successors = dict()
        actions = ["gore", "dolu", "desno", "gore-desno", "dolu-desno"]
        action_coords = ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1))
        action_coords_ball = ((0, 1), (0, -1), (1, 0), (1, 1), (1, -1))

        for action, action_coords in zip(actions, action_coords):
            new_state = self.move_player(state, action_coords)
            if self.check_valid(new_state,False):
                successors[f"Pomesti choveche {action}"] = new_state
        if manhattan_distance(state[0], state[1]) <= 1:
            for action, action_coords_ball in zip(actions, action_coords_ball):
                new_ball_state = self.move_ball(state, action_coords_ball)
                if self.check_valid(new_ball_state,True):
                    successors[f"Turni topka {action}"] = new_ball_state
        return successors

    def goal_test(self,state):
        ball_pos = state[1]
        return ball_pos in self.goal_pos

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def move_player(self, state, action_coords):
        player = list(state[0])
        action = list(action_coords)
        player[0] += action[0]
        player[1] += action[1]
        player = tuple(player)
        return player, state[1]

    def move_ball(self, state, action_coords):
        ball = list(state[1])
        action = list(action_coords)
        ball[0] += action[0]
        ball[1] += action[1]
        ball = tuple(ball)

        return state[0], ball

    def check_valid(self, state, flag):
        player = state[0]
        ball = state[1]
        # if flag:
        #     if player[1] == ball[1]:
        #         if manhattan_distance(player,ball) != 2:
        #             return False
        #     else:
        #         if manhattan_distance(player,ball) != 4:
        #             return False

        if player == ball:
            return False
        if player in self.opponents_pos:
            return False
        for opponent in self.opponents_pos:
            if manhattan_distance(opponent, ball) < 2:
                return False
        if player[0] >= self.width or player[1] >= self.height or player[0] < 0 or player[1] < 0:
            return False
        if ball[0] >= self.width or ball[1] >= self.height or ball[0] < 0 or ball[1] < 0:
            return False
        return True


if __name__ == '__main__':
    opponents = ((3, 3), (5, 4))
    goal_position = ((7, 3), (7, 2))

    player_input = input().split(",")
    player_input = list(map(int, player_input))
    player = tuple(player_input)
    ball_input = input().split(",")
    ball_input = list(map(int, ball_input))
    ball = tuple(ball_input)

    fb_problem = Football((player, ball), opponents, goal_position)
    print(breadth_first_graph_search(fb_problem).solution())