import networkx as nx
import matplotlib.pyplot as plt

# 有向图
dg = nx.DiGraph()

dg.add_nodes_from(['847594', '847280', '847835', '847492', '848445', '848374'])
dg.add_edges_from(
    [('847594', '847492'), ('847594', '847835'), ('847594', '847280'), ('847280', '847835'), ('847835', '847492'),
     ('847835', '847280'), ('847492', '847280'), ('847280', '847492'), ('847492', '847835'), ('847280', '848445'),
     ('847835', '848374'), ('847492', '847594'), ('847835', '847594'), ('847280', '847594')])

# edge_list = [('a', 'c', 1.0), ('a', 'd', 3.0), ('a', 'h', 10.0)]
# dg.add_weighted_edges_from(edge_list)

# dg.add_weighted_edges_from([('b', 'h', 100.0)])

# nx.draw(dg, with_labels=True, node_size=900, node_color='green')
#
# plt.show()

nx.write_gexf(dg, 'd:\\test.gexf')
