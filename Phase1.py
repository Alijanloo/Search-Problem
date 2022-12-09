import copy

class Node:
    def __init__(self, matrix, cost=None, depth=None):
        self.matrix = matrix
        self.cost = cost
        self.depth = depth
    # make nodes comparable, because it will be needed in sorting priority queue
    def __lt__(self, other):
        return True

def find_poses(matrix):
    #Finds robot, Butters and Points Positions
    res = [(), [], []]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if 'r' in matrix[i][j]:
                res[0] = (i,j)
            if 'b' in matrix[i][j]:
                res[1].append((i,j))
            if 'p' in matrix[i][j]:
                res[2].append((i,j))
    return res

def check_dirs(i, j, dir, matrix) -> bool:
    '''checks if the proposed direction from that position is possible or not'''
    try:
        if dir == 'U' and (i == 0 or matrix[i-1][j] == 'x' or ('b' in matrix[i][j] and 'b' in matrix[i-1][j])):
            return False
        if dir == 'L' and (j == 0 or matrix[i][j-1] == 'x' or ('b' in matrix[i][j] and 'b' in matrix[i][j-1])):
            return False
        if dir == 'D' and (i == len(matrix) or matrix[i+1][j] == 'x' or ('b' in matrix[i][j] and 'b' in matrix[i+1][j])):
            return False
        if dir == 'R' and (j == len(matrix[0]) or matrix[i][j+1] == 'x' or ('b' in matrix[i][j] and 'b' in matrix[i][j+1])):
            return False
    except:
        return False
    return True

def successor_func(node) -> dict:
    ''' produses directions that robot can go from current position, along with 
    the nodes that will have created after going that directions in the format
     of keys and values in a dictinary'''

    matrix = node.matrix
    
    i, j = find_poses(matrix)[0]

    feasable_dirs = ['U', 'R', 'D', 'L']
    # the directions whose survive in the list, can be taken
    if (not check_dirs(i, j, 'U', matrix)) or ('b' in matrix[i-1][j] and not check_dirs(i-1, j, 'U', matrix)):
        feasable_dirs.remove('U')
    if (not check_dirs(i, j, 'L', matrix)) or ('b' in matrix[i][j-1] and not check_dirs(i, j-1, 'L', matrix)):
        feasable_dirs.remove('L')
    if (not check_dirs(i, j, 'D', matrix)) or ('b' in matrix[i+1][j] and not check_dirs(i+1, j, 'D', matrix)):
        feasable_dirs.remove('D')
    if (not check_dirs(i, j, 'R', matrix)) or ('b' in matrix[i][j+1] and not check_dirs(i, j+1, 'R', matrix)):
        feasable_dirs.remove('R')

    output = {}
    if 'U' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i-1][j] += 'r'
        if 'b' in temp[i-1][j]:
            temp[i-1][j] = temp[i-1][j].replace('b', '')
            temp[i-2][j] += 'b'
        output['U'] = Node(temp, node.cost + int(temp[i-1][j][0]), node.depth + 1)
    if 'L' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i][j-1] += 'r'
        if 'b' in temp[i][j-1]:
            temp[i][j-1] = temp[i][j-1].replace('b', '')
            temp[i][j-2] += 'b'
        output['L'] = Node(temp, node.cost + int(temp[i][j-1][0]), node.depth + 1)
    if 'D' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i+1][j] += 'r'
        if 'b' in temp[i+1][j]:
            temp[i+1][j] = temp[i+1][j].replace('b', '')
            temp[i+2][j] += 'b'
        output['D'] = Node(temp, node.cost + int(temp[i+1][j][0]), node.depth + 1)
    if 'R' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i][j+1] += 'r'
        if 'b' in temp[i][j+1]:
            temp[i][j+1] = temp[i][j+1].replace('b', '')
            temp[i][j+2] += 'b'
        output['R'] = Node(temp, node.cost + int(temp[i][j+1][0]), node.depth + 1)
    
    return output

def goal_test(node) -> bool:
    for row in node.matrix:
        for cell in row:
            if ('p' in cell) and ('b' not in cell):
                return False
    return True

def manhatan_dis(start, end):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

def heuristic(node):
    robot, butters, points = find_poses(node.matrix)

    #Find Min Distance Robot to butters
    rtob = float('inf')
    for b in butters:
        if manhatan_dis(robot, b) < rtob:
            rtob = manhatan_dis(robot, b)
        
    total_btop = 0 #Minimum Summations (Every B From P's)
    for b in butters:
        btop = float('inf')
        for p in points:
            if manhatan_dis(b, p) < btop:
                btop = manhatan_dis(b, p)
        total_btop += btop

    return rtob + total_btop

from queue import PriorityQueue
def is_feasible(node):
    """it check if the problem can be solved or not:
    breaks our problem to some subproblems, wich in the way in every subproblem, it considers just one
    butter and one point in the table an trys to solve it, if at least one of these subproblems couldn't 
    be solved, our original problem has no solution, thus it returns False"""
    table = copy.deepcopy(node.matrix)
    robot, butters, points = find_poses(table)

    # clearing the table of all butters and points
    for i, row in enumerate(table):
        for j, cell in enumerate(row):
            if 'b' in cell:
                table[i][j] = table[i][j].replace('b', '')
            if 'p' in cell:
                table[i][j] = table[i][j].replace('p', '')

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False    

    for butter in butters:
        # plant the butter to its position
        table[butter[0]][butter[1]] += 'b'
        for point in points:
            table[point[0]][point[1]] += 'p'
            found = False

            # now we try to drive robot to target using bestfs
            root_node = Node(table, 0, 0)
            pq = PriorityQueue()
            pq.put((0, root_node))
            visited = [root_node]

            while not pq.empty():
                node = pq.get()[1]

                if goal_test(node):
                    found = True
                    break

                next_nodes = successor_func(node)
                
                for n in next_nodes.values():
                    if not is_visited(n):
                        h = heuristic(n)
                        pq.put((h, n))
                        visited.append(n)

            if not found: return False
            table[point[0]][point[1]] = table[point[0]][point[1]].replace('p', '')
        # pull the butter out from its place to make table clear for next subproblems
        table[butter[0]][butter[1]] = table[butter[0]][butter[1]].replace('b', '')
    return True
