import networkx as nx
import matplotlib.pyplot as plt

# 有向图
dg = nx.DiGraph()

dg.add_node('a')
dg.add_node('b')

dg.add_nodes_from(['c', 'd', 'e', 'f', 'g', 'h', 'i'])
dg.add_edges_from([('c', 'd'), ('e', 'f'), ('d', 'g'), ('g', 'h'), ('a', 'i')])

dg.add_edge('a', 'b')

edge_list = [('a', 'c', 1.0), ('a', 'd', 3.0), ('a', 'h', 10.0)]
dg.add_weighted_edges_from(edge_list)

dg.add_weighted_edges_from([('b', 'h', 100.0)])

nx.draw(dg, with_labels=True, node_size=900, node_color='green')

plt.show()
