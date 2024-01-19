import networkx as nx
import copy


def dijkstra(graph, start):
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    graph_paths = dict()
    graph_paths[start] = start
    unvisited = copy.deepcopy(graph)

    while unvisited.nodes():
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
        if distances[current_vertex] == float("infinity"):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                graph_paths[neighbor] = graph_paths[current_vertex] + neighbor
        unvisited.remove_node(current_vertex)
    print(graph_paths)
    print(distances)


G = nx.Graph()

nodes = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
G.add_nodes_from(nodes)

G_description = [
    ("A", "B", 6),
    ("A", "C", 5),
    ("A", "G", 9),
    ("B", "H", 6),
    ("C", "E", 4),
    ("C", "H", 9),
    ("B", "D", 7),
    ("D", "E", 3),
    ("D", "F", 6),
    ("E", "F", 3),
    ("F", "H", 7),
    ("G", "I", 3),
    ("H", "I", 2),
    ("I", "J", 4),
    ("C", "J", 14),
]

G.add_weighted_edges_from(G_description)

for node in G.nodes:
    print(f"Node: {node}")
    dijkstra(G, node)
