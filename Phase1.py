import copy

class Node:
    def __init__(self, matrix):
        self.matrix = matrix

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
    matrix = node.matrix
    
    def find_pos() -> tuple:
        ''' finding robot position'''
        for i, row in enumerate(matrix):
            for j, cell in enumerate(row):
                if 'r' in cell:
                    return i, j
    i, j = find_pos()

    feasable_dirs = ['U', 'R', 'D', 'L']
    # the directions who survive in the list, can be taken
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
        output['U'] = temp
    if 'L' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i][j-1] += 'r'
        if 'b' in temp[i][j-1]:
            temp[i][j-1] = temp[i][j-1].replace('b', '')
            temp[i][j-2] += 'b'
        output['L'] = temp
    if 'D' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i+1][j] += 'r'
        if 'b' in temp[i+1][j]:
            temp[i+1][j] = temp[i+1][j].replace('b', '')
            temp[i+2][j] += 'b'
        output['D'] = temp
    if 'R' in feasable_dirs:
        temp = copy.deepcopy(matrix)
        temp[i][j] = temp[i][j].replace('r', '')
        temp[i][j+1] += 'r'
        if 'b' in temp[i][j+1]:
            temp[i][j+1] = temp[i][j+1].replace('b', '')
            temp[i][j+2] += 'b'
        output['R'] = temp
    
    return output

class Graph:

    def __init__(self, root_node) -> None:
        self.root_node = root_node
        self.goal_nodes = self.find_goals()

    def find_goals(self) -> list:
        matrix = copy.deepcopy(self.root_node.matrix)
        p_poses = [] # positions of p's
        for i, row in enumerate(matrix):
                for j, cell in enumerate(row):
                    if 'r' in cell:
                        matrix[i][j] = matrix[i][j].replace('r', '')
                    if 'b' in cell:
                        matrix[i][j] = matrix[i][j].replace('b', '')
                    elif 'p' in cell:
                        matrix[i][j] += 'b'
                        p_poses.append((i, j))
        
        goal_nodes = []
        for p in p_poses:
            for d in ['U', 'L', 'D', 'R']:
                if check_dirs(p[0], p[1], d, matrix):
                    temp = copy.deepcopy(matrix)
                    if d == 'U':
                        temp[p[0]-1][p[1]] += 'r'
                    if d == 'L':
                        temp[p[0]][p[1]-1] += 'r'
                    if d == 'D':
                        temp[p[0]+1][p[1]] += 'r'
                    if d == 'R':
                        temp[p[0]][p[1]+1] += 'r'
                    goal_nodes.append(Node(temp))
        return goal_nodes
            
    def goal_test(self, node) -> bool:
        for n in self.goal_nodes:
            if n.matrix == node.matrix:
                return True
        return False
