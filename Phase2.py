from Phase1 import successor_func

def BFS(graph):
    fring = []
    fring.append(([], graph.root_node))
    visited = [graph.root_node]
    
    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    while fring:
        steps, temp = fring.pop(0)
        next_nodes = successor_func(temp)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                
                if graph.goal_test(n):
                    for row in n.matrix:
                        print(row)
                    return steps
                    
                fring.append((steps.copy(), n))
                visited.append(n)
                steps.pop(len(steps)-1)