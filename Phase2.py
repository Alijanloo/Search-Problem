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

def DFS(root_node):
    st = []
    st.append(([], root_node))
    visited = [root_node]

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    while st:
        steps, node = st.pop(0)

        if goal_test(node):
            return steps, node.cost, node.depth

        next_nodes = successor_func(node)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                st.insert(0,(steps.copy(), n))
                visited.append(n)
                steps.pop(len(steps)-1)

def IDS(root_node,maxdepth):
    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False
    depth = 0
    while depth<maxdepth :
        st = []
        st.append(([], root_node))
        visited = [root_node]
        while st:
            steps, node = st.pop(0)
            if node.depth > depth:
                continue

            if goal_test(node):
                return steps, node.cost, node.depth

            next_nodes = successor_func(node)
            
            for dir, n in next_nodes.items():
                if not is_visited(n):
                    steps.append(dir)
                    st.insert(0,(steps.copy(), n))
                    visited.append(n)
                    steps.pop(len(steps)-1)
        depth += 1

