from searching_framework import Problem, astar_search, breadth_first_graph_search


class ReachHouse(Problem):
    def __init__(self, initial, allowed):
        super().__init__(initial)
        self.allowed = allowed

    def successor(self, state):
        successors = dict()
        actions = ("Stoj", "Gore 1", "Gore 2", "Gore-desno 1", "Gore-desno 2", "Gore-levo 1", "Gore-levo 2")
        house_move_state = move_house(state)
        for action in actions:
            new_state = make_move(house_move_state, action)
            if check_valid(new_state, self.allowed):
                successors[action] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        player = state[0]
        house = state[1]
        return player[0] == house[0] and player[1] == house[1]

    def h(self,node):
        value=0
        x_man = node.state[0][0]
        y_man = node.state[0][1]
        for a in allowed:
            if a[1]==y_man and a[0]>x_man:
                value+=1
        return value


def check_valid(state, allowed):
    player = state[0]
    house = state[1]
    if player[0] == house[0] and player[1] == house[1]:
        return True
    if player not in allowed:
        return False
    if player[0] < 0 or player[0] > 4 or player[1] < 0 or player[1] > 8:
        return False
    return True


def move_house(state):
    house = list(state[1])
    direction = state[2]
    if direction == "desno":
        if house[0] == 4:
            direction = "levo"
            house[0] -= 1
        else:
            house[0] += 1
    else:
        if house[0] == 0:
            direction = "desno"
            house[0] += 1
        else:
            house[0] -= 1
    return state[0], tuple(house), direction


def make_move(state,action):
    player = list(state[0])
    direction = state[2]
    # ("Stoj", "Gore 1", "Gore 2", "Gore-desno 1", "Gore-desno 2", "Gore-levo 1", "Gore-levo 2")
    if action == "Stoj":
        player[1] += 0
        player[0] += 0
    elif action == "Gore 1":
        player[1] += 1
    elif action == "Gore 2":
        player[1] += 2
    elif action == "Gore-desno 1":
        player[1] += 1
        player[0] += 1
    elif action == "Gore-desno 2":
        player[1] += 2
        player[0] += 2
    elif action == "Gore-levo 1":
        player[1] += 1
        player[0] -= 1
    elif action == "Gore-levo 2":
        player[1] += 2
        player[0] -= 2
    return tuple(player), state[1], direction


if __name__ == '__main__':
    allowed = [(1, 0), (2, 0), (3, 0), (1, 1), (2, 1), (0, 2), (2, 2), (4, 2), (1, 3), (3, 3), (4, 3), (0, 4), (2, 4),
               (2, 5), (3, 5), (0, 6), (2, 6), (1, 7), (3, 7)]
    # your code here
    # INPUTS
    player_input = input().split(",")
    player = tuple(map(int, player_input))
    house_input = input().split(",")
    house = tuple(map(int, house_input))
    direction = input()

    House = ReachHouse((player, house, direction), allowed)
    if astar_search(House) is not None:
        print(astar_search(House).solution())
