from Phase1 import successor_func, goal_test
from queue import PriorityQueue
import time

def BFS(root_node):
    # start = time.time()
    fringe = []
    fringe.append(([], root_node)) # the first element of tuple stores steps taken to achive this node
    visited = [root_node]

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    while fringe:
        steps, node = fringe.pop(0)

        if goal_test(node):
            # print("duration: ", time.time() - start)
            return steps, node.cost, node.depth

        next_nodes = successor_func(node)
        
        for dir, n in next_nodes.items():
            if not is_visited(n):
                steps.append(dir)
                fringe.append((steps.copy(), n))
                visited.append(n)
                # after this iteration we're gonna see the next childs of parnt,
                #  so we won't need direction of this child anymore
                steps.pop(len(steps)-1)
    # print("duration: ", time.time() - start)

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
                st.insert(0,(steps.copy(), n)) #insert at 0 index becuse DFS is LIFO
                visited.append(n)
                steps.pop(len(steps)-1)

def IDS(root_node):
    maxdepth = 100

    def is_visited(node):
        for n in visited:
            if node.matrix == n.matrix:
                return True
        return False

    depth = 0
    while depth < maxdepth :
        st = []
        st.append(([], root_node))
        visited = [root_node]
        while st:
            steps, node = st.pop(0)
            #Checking for depth (if node depth is more than depth we continue the loop becuse we dont need to check this series)
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
        #Adding depth (we check from depth=0 to maxdepth for finding goal nodes)
        depth += 1

def UCS(root_node): # Expands the cheapest nodes first. 
    pq = PriorityQueue() # Could be replaced by two list and one of them should be always sorted which basically means a priority queue 
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
                h =  n.cost # when using UCS we pay attention only to the cost of the nodes.
                pq.put((h, (steps.copy(), n)))
                visited.append(n)
                steps.pop(len(steps)-1)
