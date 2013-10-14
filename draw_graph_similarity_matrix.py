import networkx as nx
import matplotlib.pyplot as plt

g = nx.Graph()

edges = []
edges.append(('A','B',2.5))
edges.append(('B','C',2.3))
edges.append(('C','D',2.7))
edges.append(('D','E',2.5))
edges.append(('E','A',3.2))
edges.append(('F','E',4.5))

g.add_weighted_edges_from(edges)

pos = nx.spring_layout(g)

nodelist = ['A','B','C','D','E','F']
nodecolor = ['r','k','y','g','m','w']

# node_size and alpha value could also be set in the draw_networkx_nodes func
for i in range(len(nodelist)):
    nx.draw_networkx_nodes(g,pos,
            nodelist=nodelist[i],
            node_color=nodecolor[i])

nx.draw_networkx_edges(g,pos)

plt.show()
