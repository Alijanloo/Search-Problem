from Phase1 import Node # successor_func, cost_func, goal_test, depth_func, heuristics
from Phase2 import BFS, DFS, IDS, UCS # we will import Phase1's functions inside this and next lib
from Phase3 import A_Star, BestFS


if __name__ == '__main__':
    m, n = [int(i) for i in input().split()]
    input_matrix = []

    for i in range(m):
        row = [int(i) for i in input().split()]
        input_matrix.append(row)

    initial_node = Node(input_matrix, cost=0, depth=0)

    methods = [BFS, DFS, IDS, UCS, A_Star, BestFS]
    setOfAnsowers = []
    
    for method in methods:
        steps, total_cost, total_depth = func(initial_node)
        setOfAnsowers.append([steps, total_cost, total_depth])
    
    best_ans = [None, float(inf)]