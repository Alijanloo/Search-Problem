import copy

class Node:
    def __init__(self, matrix):
        self._matrix = matrix
    
    def get_matrix(self):
        return self._matrix

class Graph:

    def __init__(self, root_node) -> None:
        self.root_node = root_node
        self.goal_nodes = find_goals()

    def successor_func(self, node) -> dict:
        matrix = node.get_matrix()
        
        def find_pos() -> tuple:
            ''' finding robot position'''
            for i, row in enumerate(matrix):
                for j, cell in enumerate(row):
                    if 'r' in cell:
                        return i, j
        i, j = find_pos()
        
        def check_dirs(i, j, dir) -> bool:
            '''checks if the proposed directions from that position is possible or not'''
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

        feasable_dirs = ['U', 'R', 'D', 'L']
        # the directions who survive in the list, can be taken
        if (not check_dirs(i, j, 'U')) or ('b' in matrix[i-1][j] and not check_dirs(i-1, j, 'U')):
            feasable_dirs.remove('U')
        if (not check_dirs(i, j, 'L')) or ('b' in matrix[i][j-1] and not check_dirs(i, j-1, 'L')):
            feasable_dirs.remove('L')
        if (not check_dirs(i, j, 'D')) or ('b' in matrix[i+1][j] and not check_dirs(i+1, j, 'D')):
            feasable_dirs.remove('D')
        if (not check_dirs(i, j, 'R')) or ('b' in matrix[i][j+1] and not check_dirs(i, j+1, 'R')):
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

    def find_goals(self):
        pass
            
    def goal_test(self, node) -> bool:
        pass
