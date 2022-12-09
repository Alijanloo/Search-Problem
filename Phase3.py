from queue import PriorityQueue
from Phase1 import successor_func, goal_test, heuristic

def BestFS(root_node): # a greedy algorithm that just considers heuristic to expand child nodes
    pq = PriorityQueue()
    pq.put((0, ([], root_node))) # our elements of pq will be tupels wich when we put a new tuple to it 
    # compares tuples to put it in the right position, in that way it's always remains sorted,
    # when it trys to compare two tuples, first it compares the first elements of tuples, if they were equal
    # it puts theme beside each other
    visited = [root_node]

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    while not pq.empty():
        steps, node = pq.get()[1]

        if goal_test(node):
            return steps, node.cost, node.depth

        next_nodes = successor_func(node)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                h = heuristic(n)
                pq.put((h, (steps.copy(), n)))
                visited.append(n)
                steps.pop(len(steps)-1)
                
                
def A_star(root_node): # uses heuristics to find the answer
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
            return steps, node.cost, node.depth

        next_nodes = successor_func(node)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                h = heuristic(n) + n.cost
                pq.put((h, (steps.copy(), n)))
                visited.append(n)
                steps.pop(len(steps)-1)
