import networkx as nx
from collections import deque


def dfs_iterative(graph, start, end):
    visited = set()
    stack = [start]
    print("DFS algorythm:")
    while stack:
        vertex = stack.pop()
        if vertex == end:
            print(vertex, end=" ")
            return
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            for key in graph[vertex]:
                stack.append(key)
    print("Path does not exist")


def bfs_iterative(graph, start, end):
    visited = set()
    queue = deque([start])
    print("BFS algorythm:")
    while queue:
        vertex = queue.popleft()
        if vertex == end:
            print(vertex, end=" ")
            return
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    print("Path does not exist")


G = nx.Graph()
nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
G.add_nodes_from(nodes)
G.add_edges_from(
    [
        ("A", "B"),
        ("A", "C"),
        ("A", "G"),
        ("B", "H"),
        ("C", "E"),
        ("C", "H"),
        ("B", "D"),
        ("D", "E"),
        ("D", "F"),
        ("E", "F"),
        ("F", "H"),
        ("G", "I"),
        ("H", "I"),
        ("I", "J"),
        ("C", "J"),
    ]
)

start = input("Input the start point in graph 'ABCDEFGHIJ'\n").upper()
end = input("Inpit the end point in graph 'ABCDEFGHIJ'\n").upper()

if start in "ABCDEFGHIJ" and end in "ABCDEFGHIJ":
    dfs_iterative(G, start, end)
    print("")
    bfs_iterative(G, start, end)
else:
    print("Wrong input")

