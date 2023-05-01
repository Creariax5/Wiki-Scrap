import networkx as nx
import matplotlib.pyplot as plt
import csv
from tqdm import tqdm

edges = []
with open("D:/devProjects/PycharmProjects/scraping/wikipedia/brain/csv/data.csv", 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        tmp = []
        for col in row:
            tmp.append(col)
        edges.append(tmp)

G = nx.Graph()
for i in tqdm(range(len(edges))):
    G.add_node(edges[i][0])
    for e in edges:
        for j in range(len(e)):
            G.add_edges_from([(e[0], e[j])])

nx.draw_networkx(G, with_labels=False)
plt.show()
