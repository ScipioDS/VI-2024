from searching_framework import Problem, astar_search, breadth_first_graph_search


class MazeHouse(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial)
        self.goal = goal

    def successor(self, state):
        successors = dict()
        actions = ("Desno 2", "Desno 3", "Gore", "Dolu", "Levo")
        for action in actions:
            new_state = make_move(state, action)
            if check_valid(new_state, action, self.goal):
                successors[action] = new_state
        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        player = state[0]
        return player == goal

    def h(self, node):
        player = list(node.state[0])
        self.goal = list(node.state[1])
        return abs(player[0] - goal[0]) / 3 + abs(player[1] - goal[1])


def make_move(state, action):
    player = list(state[0])
    if action == "Desno 2":
        player[0] += 2
    elif action == "Desno 3":
        player[0] += 3
    elif action == "Gore":
        player[1] += 1
    elif action == "Dolu":
        player[1] -= 1
    elif action == "Levo":
        player[0] -= 1
    return tuple(player), state[1], state[2]


def check_valid(state, action, goal):
    player = state[0]
    obstacles = state[1]
    grid = state[2]
    if player == goal:
        return True
    if player in obstacles:
        return False
    if player[0] < 0 or player[0] >= grid or player[1] < 0 or player[1] >= grid:
        return False
    if action == "Desno 2":
        for obstacle in obstacles:
            if player[0] - 1 == obstacle[0] and player[1] == obstacle[1]:
                return False
    if action == "Desno 3":
        for obstacle in obstacles:
            if player[0] - 1 == obstacle[0] and player[1] == obstacle[1]:
                return False
            if player[0] - 2 == obstacle[0] and player[1] == obstacle[1]:
                return False
    return True


if __name__ == '__main__':
    # your code here
    grid_size = int(input())
    num_obstacles = int(input())
    obstacles = []

    for i in range(0, num_obstacles):
        input_obs = input().split(",")
        obstacles.append(tuple(map(int, input_obs)))

    obstacles = tuple(obstacles)

    start_input = input().split(",")
    start = tuple(map(int, start_input))

    goal_input = input().split(",")
    goal = tuple(map(int, goal_input))

    maze = MazeHouse((start, obstacles, grid_size), goal)
    if astar_search(maze) is not None:
        print(astar_search(maze).solution())