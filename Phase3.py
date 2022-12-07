from queue import PriorityQueue
from Phase1 import successor_func, goal_test, heuristic

def BestFS(root_node):
    pq = PriorityQueue()
    pq.put((0, ([], root_node)))
    visited = [root_node]

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    while not pq.empty():
        steps, node = pq.get()[1]

        if goal_test(node):
            # for row in n.matrix:
            #     print(row)
            return steps, node.cost, node.depth

        next_nodes = successor_func(node)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                h = heuristic(n) + n.cost
                pq.put((h, (steps.copy(), n)))
                visited.append(n)
                steps.pop(len(steps)-1)