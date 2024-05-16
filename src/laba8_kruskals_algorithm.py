import os
import csv

#helps to connect nodes without creating cycles
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    #Find the root node
    def find(self, node):
        parent = self.parent
        if parent[node] != node:
            parent[node] = self.find(parent[node])
        return parent[node]

#Combines two components using ranks
    def union(self, root1, root2):
        #srch roots
        root1 = self.find(root1)
        root2 = self.find(root2)
        parent = self.parent
        rank = self.rank
        #Use ranks for choose father(parent)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1
            return True
        return False

#Finds a minimum spanning tree (MST) in a graph using Kruskal's algorithm
def find_minimum_spanning_tree(edges, num_vertices):
    """
    sorting edges by wght
    """
    edges.sort(key=lambda x: x[2])

    separated_sets = UnionFind(num_vertices)
    total_cable_length = 0
    num_edges_used = 0

    for vertex1, vertex2, distance in edges:
        # add to MST if it isn`t cycles
        if separated_sets.union(vertex1, vertex2):
            total_cable_length += distance
            num_edges_used += 1
            if num_edges_used == num_vertices - 1:
                break

    if num_edges_used == num_vertices - 1:
        return total_cable_length
    else:
        return -1
#edges reader
def read_edges_from_csv(filename):
    if not os.path.isfile(filename):
        raise FileNotFoundError(f"File not found: {filename}")

    with open(filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        edges = []
        vertex_set = set()
        for row in reader:
            well1 = int(row[0])
            well2 = int(row[1])
            distance = int(row[2])
            edges.append((well1, well2, distance))
            vertex_set.add(well1)
            vertex_set.add(well2)
        return edges, len(vertex_set)
