from sklearn import datasets
from sklearn.preprocessing import scale
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel
import networkx as nx
import matplotlib.pyplot as plt

iris = datasets.load_iris()
data = scale(iris.data)
label = iris.target
n_instances,n_features = data.shape

# Extract the labels
tp = np.unique(label)
nodecolor = ['r','y','g','w','b','k']
assert len(tp)<=len(nodecolor),"Color is not enough"

sigma = 1.0

affinity = rbf_kernel(data,gamma=1./(2*sigma**2))

# Construct the similarity graph
g = nx.Graph()
for i in range(0,n_instances-1):
    for j in range(i+1,n_instances):
        g.add_edge(i,j,weight=affinity[i,j])

ax = plt.figure(figsize=(10,10))

pos = nx.spring_layout(g)

# Draw the similarity matrix
# Step 1: Draw nodes in different colors according to their classes
for i in range(n_instances):
    nx.draw_networkx_nodes(g,pos,
            nodelist=[i],
            node_color=nodecolor[label[i]],
            node_size=200,
            alpha=1.0,
            labels=str([i]))
    nx.draw_networkx_labels(g,pos,
            font_size=8,
            font_color='k',
            alpha = 0.5)
plt.savefig('foo_1.png')

ax_2 = plt.figure(figsize=(10,10))
for i in range(n_instances):
    nx.draw_networkx_nodes(g,pos,
            nodelist=[i],
            node_color=nodecolor[label[i]],
            node_size=200,
            alpha=1.0,
            labels=str([i]))
    nx.draw_networkx_labels(g,pos,
            font_size=8,
            font_color='w',
            alpha = 0.5)
plt.savefig('foo_2.png')
# Step 2: Draw edges
#nx.draw_networkx_edges(g,pos,width=0.2,alpha=0.1)

#nx.draw_networkx(g,pos)

#plt.show()
