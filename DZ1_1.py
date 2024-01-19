import networkx as nx
import matplotlib.pyplot as plt

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

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
is_connected = nx.is_connected(G)
degree_centrality = nx.degree_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)

print(f"Кількість вузлів: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"граф - зв'язний: {is_connected}")

output_data = {node: [] for node in nodes}
for node in degree_centrality:
    output_data[node].append(float(degree_centrality[node]))
for node in closeness_centrality:
    output_data[node].append(float(closeness_centrality[node]))
for node in betweenness_centrality:
    output_data[node].append(float(betweenness_centrality[node]))

print(f"Вузол | Ступінь центральносі | Близькість     | Посередництво ")
for node in output_data:
    print(
        f"{node:<6}| {output_data[node][0]:<21.5f}| {output_data[node][1]:<15.5f}| {output_data[node][2]:<15.5f}"
    )

nx.draw(G, with_labels=True)
plt.show()
