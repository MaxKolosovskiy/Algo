def bfs(graph, visited, start):
    queue = [start]

    while queue:
        vertex = queue.pop(0)
        visited[vertex] = True

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)

def find_root_vertices(graph):
    n = len(graph)
    visited = [False] * n

    in_degree = [0] * n
    for vertex in range(n):
        for neighbor in graph[vertex]:
            in_degree[neighbor] += 1

    root_vertices = []
    for vertex in range(n):
        if in_degree[vertex] == 0:
            root_vertices.append(vertex)

    for vertex in root_vertices:
        bfs(graph, visited, vertex)

    if all(visited):
        return root_vertices
    else:
        return -1

def read_graph_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        graph = [[] for _ in range(n)]
        for line in lines[1:]:
            u, v = map(int, line.strip().split())
            graph[u].append(v)
        return graph

def write_result_to_file(result, file_name):
    with open(file_name, 'w') as file:
        if isinstance(result, list):
            file.write(" ".join(map(str, result)))
        else:
            file.write(str(result))

if __name__ == "__main__":
    graph = read_graph_from_file("input.txt")
    root_vertices = find_root_vertices(graph)
    write_result_to_file(root_vertices, "output.txt")