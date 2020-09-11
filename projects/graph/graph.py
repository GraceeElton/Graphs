"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # what data structure do we use for a BFS -- A = queue
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue(starting_vertex)
        # make a set to track if we have been to an node before (we dont ever want to go to a node twice)
        visited = set()
        # while our queue is not empty
        while q.size() > 0:
            # dequeue whatever is at the front of our line and this is our current_node
            current_node = q.dequeue()
            # if we havent visited the node yet,--
            if current_node not in visited:
                #  mark it as visted
                visited.add(current_node)
                print(current_node)
                # and get the current_node friends
                neighbors = self.get_neighbors(current_node)
                # for each of  the friends
                for neighbor in neighbors:
                    #  add them to queue
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # what data structure do we use for a DFS -- A = STACK
        # make a stack
        s = Stack()
        # push on our starting node
        s.push(starting_vertex)
        # make a set to track if we have been to an node before (we dont ever want to go to a node twice)
        visted = set()
        # while our STACK is not empty
        while s.size() > 0:
            # pop off whatever node is on top and this is our current_node
            current_node = s.pop()
            # if we havent visited the node yet,--
            if current_node not in visted:
                # mark it as visted
                visted.add(current_node)
                print(current_node)
                # # and get the current_node friends
                neighbors = self.get_neighbors(current_node)
                # for each of  the friends
                for neighbor in neighbors:
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        visited.add(starting_vertex)
        print(starting_vertex)

        for n in self.get_neighbors(starting_vertex):
            if n not in visited:
                self.dft_recursive(n, visited)

        # Broken pseudocode
        # for n in node.neighbors:
        # 	dft_recursive(n)

    def bfs(self, starting_vertex,  destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and
        q = Queue()
        # enqueue A PATH TO the starting vertex ID
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            current_path = q.dequeue()
            # Grab the last vertex from the PATH
            last_node = current_path[-1]
            # If that vertex has not been visited...
            if last_node not in visited:
                # CHECK IF IT'S THE TARGET
                if last_node == destination_vertex:
                    # IF SO, RETURN PATH
                    return current_path
                else:
                    # Mark it as visited...
                    visited.add(last_node)
                    # Then add A PATH TO its neighbors to the back of the queue
                    neighbors = self.get_neighbors(last_node)
                    for n in neighbors:
                        # COPY THE PATH
                        copy = current_path[:]
                        # APPEND THE NEIGHOR TO THE BACK
                        copy.append(n)
                        q.enqueue(copy)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and
        s = Stack()
        # pushA PATH TO the starting vertex ID
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # pop the first PATH
            current_path = s.pop()
            # Grab the last vertex from the PATH
            last_node = current_path[-1]
            # If that vertex has not been visited...
            if last_node not in visited:
                # CHECK IF IT'S THE TARGET
                if last_node == destination_vertex:
                    # IF SO, RETURN PATH
                    return current_path
                else:
                    # Mark it as visited...
                    visited.add(last_node)
                    # Then add A PATH TO its neighbors to the back of the queue
                    neighbors = self.get_neighbors(last_node)
                    for n in neighbors:
                        # COPY THE PATH
                        copy = current_path[:]
                        # APPEND THE NEIGHOR TO THE BACK
                        copy.append(n)
                        s.push(copy)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if path is None:
            path = [starting_vertex]

        visting_node = path[-1]

        if visting_node not in visited:
            visited.add(visting_node)

            if visting_node == destination_vertex:
                return path

            for neighbor in self.get_neighbors(visting_node):
                new_path = path + [neighbor]

                find = self.dfs_recursive(
                    starting_vertex, destination_vertex, visited, new_path)

                if find:
                    return find

              # path = [1,2]
                # visiting_node = 2
                # path = [1,2,3]
                # path = [1,2,3,5]
                # path = [1,2,4]
                # path = [1,2,4]
                # visiting_node = 4
                # visited set = {1,2,4}
                # 4 != 6
                # now we loop through neighbors
                # new_path = [1,2,4] + [6] transforms path
                # path = [1,2,4,6]
                # visiting_node = 6
                # visited = {1,2,4,6}
                # is visiting node == dest.index
                # return [1,2,4,6]


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
