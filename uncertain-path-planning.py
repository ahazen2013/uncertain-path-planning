
class Point:
    utility = 0
    utility_old = 0
    if_west = 0
    if_north = 0
    if_south = 0
    if_east = 0
    identifier = ''
    goodness = 0

    def __init__(self, identifier):
        if identifier == 'Destination':
            self.utility = 100
            self.identifier = '.'
        if identifier == 'Obstacle':
            self.utility = -100
            self.identifier = 'o'
        else:
            self.identifier = '_'

    def update_utility(self, new_utility):
        self.utility_old = self.utility
        self.utility = new_utility

    def e_check(self):
        if abs(self.utility - self.utility_old) < .01:
            return True
        else:
            return False


# Implementation Guide:
# - In the Bellman equation for value iteration, there are two parameters “Gamma” (γ) and
# “Epsilon” (ε). Please set the value of gamma to be 0.9 and epsilon to be 0.01.
# - Moving off the grid is considered a valid action (for example, at state (0, 0) moving
# North is off the grid). In this case, consider this a transition from (0, 0) to (0, 0) with
# action North (i.e., it will end up staying in the current position).
# - Treat obstacles as non-terminal, meaning that the robot can (theoretically) move into and
# over an obstacle.
# robot has .1 chance to move in each unintended direction, and .7 chance to move in the correct direction
# -1 for each movement, -100 for hitting obstacle, +100 for reaching destination

def find_direction(gridspace, row, col, size):
    if row == 0:
        U_north = gridspace[row][col].utility
    else:
        U_north = gridspace[row - 1][col].utility
    if row == (size - 1):
        U_south = gridspace[row][col].utility
    else:
        U_south = gridspace[row + 1][col].utility
    if col == (size - 1):
        U_east = gridspace[row][col].utility
    else:
        U_east = gridspace[row][col + 1].utility
    if col == 0:
        U_west = gridspace[row][col].utility
    else:
        U_west = gridspace[row][col - 1].utility

    best_north = .9 * ((.7 * U_north) + (.1 * U_south) + (.1 * U_east) + (.1 * U_west)) - 1
    best_south = .9 * ((.1 * U_north) + (.7 * U_south) + (.1 * U_east) + (.1 * U_west)) - 1
    best_east = .9 * ((.1 * U_north) + (.1 * U_south) + (.7 * U_east) + (.1 * U_west)) - 1
    best_west = .9 * ((.1 * U_north) + (.1 * U_south) + (.1 * U_east) + (.7 * U_west)) - 1

    maximum = best_north        # If there's a tie, it breaks in order of N S E W
    if maximum < best_south:
        maximum = best_south
    if maximum < best_east:
        maximum = best_east
    if maximum < best_west:
        maximum = best_west
    if maximum == best_north:
        return '^', maximum
    if maximum == best_south:
        return 'v', maximum
    if maximum == best_east:
        return '>', maximum
    if maximum == best_west:
        return '<', maximum


# Input:
input_file = open("input.txt", "r")  # read input file always named input.txt
parameters = input_file.readlines()
input_file.close()

n = int(parameters[0])   # (n x n grid)
grid = list()
for a in range(0, n):
    templist = list()
    for b in range(0, n):
        templist.append(Point('null'))
    grid.append(templist)

num_obstacles = parameters[1]   # (number of obstacles)
obstacles = list()              # list of obstacles
for i in range(2, len(parameters) - 1):
    tempstring = parameters[i].split(',')
    grid[int(tempstring[1])][int(tempstring[0])] = Point('Obstacle')
    obstacles.append([int(tempstring[1]), int(tempstring[0])])
destination = parameters[len(parameters)-1]  # coordinates of destination
destination = destination.split(',')
destination_row = int(destination[1])
destination_col = int(destination[0])
grid[destination_row][destination_col].identifier = '.'
grid[destination_row][destination_col].utility = 100

b = True
while b:
    b = False
    for m in range(0, n):
        for l in range(0, n):
            if grid[m][l].identifier != 'o' and grid[m][l].identifier != '.':
                tempnode = grid[m][l]
                tempnode.identifier, x = find_direction(grid, m, l, n)
                tempnode.update_utility(x)
                grid[m][l] = tempnode
                if not b:
                    if not tempnode.e_check():
                        b = True    # Stays in loop if even one difference is more than epsilon

# Output: n x n grid showing 'o' for obstacles, . for destination
# ^, >, v, < for N, E, S, and W respectively
output_file = open("output.txt", "w")  # Output to output.txt
for x in grid:
    for y in x:
        output_file.write(str(y.identifier))
    output_file.write('\n')
output_file.close()
