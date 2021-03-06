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
        # TODO
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist.')

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # # TODO
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue and enqueue the starting vertex ID
        # Create an empty Set to store visited verticies
        # While the queue is not empty...
            # Dequeue the first vertex
            # If that vertex has not been visited...
                # Mark it as visited
                # Then add all of its neighbors to the back of the queue
        # TODO
        q = Queue()
        q.enqueue(starting_vertex)
        visited = set()

        while q.size() > 0:
            current_vertex = q.dequeue()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO
        s = Stack()
        s.push(starting_vertex)
        visited = set()

        while s.size() > 0:
            current_vertex = s.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            for neighbor in self.get_neighbors(starting_vertex):
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()

        while q.size() > 0:
            # grab list
            path = q.dequeue()
            # take last in path
            current_vertex = path[-1]
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return path
                
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    # create a new path to append neighbor
                    new_path = path.copy()
                    # new_path = list(path)     <-- Also works to copy
                    new_path.append(neighbor)
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO
        s = Stack()
        s.push([starting_vertex])
        visited = set()

        while s.size() > 0:
            # grab list
            path = s.pop()
            # take last in path
            current_vertex = path[-1]
            if current_vertex not in visited:
                if current_vertex == destination_vertex:
                    return path
                
                visited.add(current_vertex)
                for neighbor in self.get_neighbors(current_vertex):
                    # create a new path to append neighbor
                    new_path = path.copy()
                    # new_path = list(path)     <-- Also works to copy
                    new_path.append(neighbor)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        if visited is None:
            visited = set()
        if path is None:
            path = []
            
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path

        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path is not None:
                    return new_path
        return None

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
    print('==================== Breadth-First Traversal ====================')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('==================== Depth-First Traversal ====================')
    graph.dft(1)
    print('==================== Depth-First Traversal Recursive ====================')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('==================== BFT Shortest ====================')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('==================== DFT Shortest ====================')
    print(graph.dfs(1, 6))
    print('==================== DFT Shortest Recursive ====================')
    print(graph.dfs_recursive(1, 6))
