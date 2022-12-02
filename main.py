from Phase1 import Node, successor_func # successor_func, goal_test, depth_func, heuristic
from Phase2 import BFS #, DFS, IDS, UCS # we will import Phase1's functions inside this and next lib
# from Phase3 import A_Star, BestFS


if __name__ == '__main__':
    m, n = [int(i) for i in input().split()]
    input_matrix = []

    for i in range(m):
        row = [i for i in input().split()]
        input_matrix.append(row)

    initial_node = Node(input_matrix, 0, 0)
    
    print(BFS(initial_node))

    # temp = successor_func(initial_node)
    # for state in graph.goal_nodes:
    #     for row in state.matrix:
    #         print(row)
    #     print()
    # methods = [BFS, DFS, IDS, UCS, A_Star, BestFS]
    # setOfAnsowers = []
    
    # for method in methods:
    #     steps, total_cost, total_depth = func(initial_node)
    #     setOfAnsowers.append([steps, total_cost, total_depth])
    
    # best_ans = [None, float(inf), None]

    # for i, ans in enumerate(setOfAnsowers):
    #     if ans[1] < best_ans[1] :
    #         best_ans = ans

    # if best_ans[1] == float('inf'):
    #     print("can't pass the butter")
    # else:
    #     print(" ".join(best_ans[0]))
    #     print(best_ans[1])
    #     print(best_ans[2])