from Phase1 import successor_func, goal_test

def BFS(root_node):
    # total_cost = 0
    # total_depth = 0
    fring = []
    fring.append(([], root_node))
    visited = [root_node]

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    while fring:
        steps, node = fring.pop(0)

        if goal_test(node):
            # for row in n.matrix:
            #     print(row)
            return steps, node.cost, node.depth

        next_nodes = successor_func(node)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                fring.append((steps.copy(), n))
                visited.append(n)
                steps.pop(len(steps)-1)