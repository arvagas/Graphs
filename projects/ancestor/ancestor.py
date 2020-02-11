class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('That vertex does not exist.')

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]


def earliest_ancestor(ancestors, starting_node):
    # initialize variables
    graph = Graph()    
    stack = Stack()
    early_origin = -1
    max_path_len = 1

    #  updating graph
    for relation in ancestors:
        # 0 is parent, 1 is child
        graph.add_vertex(relation[0])
        graph.add_vertex(relation[1])

        # child will have a path towards parent
        graph.add_edge(relation[1], relation[0])

    stack.push([starting_node])
    while stack.size() > 0:
        path = stack.pop()
        oldest = path[-1]

        # handles path that are the same length, but takes the 'smaller' value
        if len(path) >= max_path_len and oldest < early_origin \
            or len(path) > max_path_len:
            # ^ handles paths that don't continue off the bat
            early_origin = oldest
            max_path_len = len(path)
        
        for parent in graph.get_neighbors(oldest):
            new_path = list(path)
            new_path.append(parent)
            stack.push(new_path)
    
    return early_origin