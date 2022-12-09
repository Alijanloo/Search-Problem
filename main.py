from Phase1 import Node, is_feasible
from Phase2 import BFS, DFS, IDS, UCS # we will import Phase1's functions inside this and next lib
from Phase3 import A_star, BestFS


def main():
    m, n = [int(i) for i in input().split()]
    input_matrix = []

    for i in range(m):
        row = [i for i in input().split()]
        input_matrix.append(row)

    initial_node = Node(input_matrix, 0, 0)

    if not is_feasible(initial_node):
        print("can't pass the butter")
        return
    
    # print(BFS(initial_node))
    methods = {'BFS': BFS, 'DFS': DFS, 'IDS': IDS, 'UCS': UCS, 'A_star': A_star, 'BestfS': BestFS}
    setOfAnsowers = []
    
    for name, method in methods.items():
        print(f'running {name} ...')
        steps, total_cost, total_depth = method(initial_node)
        print(f'{name} answer: {[steps, total_cost, total_depth]}')
        setOfAnsowers.append([steps, total_cost, total_depth])
    
    best_ans = [None, float('inf'), None]

    for ans in setOfAnsowers:
        if ans[1] < best_ans[1] :
            best_ans = ans

    print(" ".join(best_ans[0]))
    print(best_ans[1])
    print(best_ans[2])

main()