from typing import Iterable
import networkx as ntx
import random
import numpy as np
import copy
import os.path as osp
import os

from datetime import datetime

from matplotlib import pyplot as plt
from matplotlib import colors

def graph_mat_2_ntx(graph:np.ndarray):
    pass

def ntx_2_graph_mat(graph:ntx.Graph):
    pass


def get_time_stamp():
    timestamp = datetime.now()
    timestamp_str = timestamp.strftime("%Y-%m-%d_%H-%M-%S")
    return timestamp_str


def randomize_delay(graph:ntx.Graph, min_d, max_d, inplace=True):
    
    assert min_d >=0
    assert max_d >=0

    if not inplace:
        graph = copy.deepcopy(graph)

    edges = list(graph.edges)

    for u,v in edges:
        rand_d = random.randint(min_d, max_d)
        graph.edges[u,v]['delay'] = rand_d

    return graph

def plot_graph(
    graph:ntx.Graph, 
    layout,
    special_nodes:Iterable,
    save_name:str='',
    save_dir:str=None, 
    show:bool=False
):
    
    nodes = list(graph.nodes)
    node_colors = ['skyblue' if x not in special_nodes else 'red' for x in nodes]
    edge_colors = [edge[2]['delay'] if 'delay' in edge[2] else 1 for edge in graph.edges(data=True)]
    cmap = plt.cm.get_cmap('viridis')
    norm = colors.Normalize(vmin=min(edge_colors), vmax=max(edge_colors))

    ntx.draw(
        graph,
        pos=layout,
        node_color=node_colors, 
        with_labels=True,
        edge_color=edge_colors, 
        edge_cmap=cmap,
        edge_vmin=min(edge_colors), 
        edge_vmax=max(edge_colors)
    )

    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])
    cbar = plt.colorbar(sm, label='Delay')
    cbar.ax.yaxis.label.set_size(12)   
    cbar.ax.tick_params(labelsize=10)  

    if save_dir is not None:
        plt.savefig(osp.join(save_dir, "graph_{}_{}.png".format(save_name,get_time_stamp())))
    if show:
        plt.show()
    plt.clf()

def barbell_graph(m1, m2):
    return ntx.barbell_graph(m1, m2)

def complete_graph(n_node):
    return ntx.complete_graph(n_node)   

def complete_bipartite(n1, n2):
    return ntx.complete_bipartite_graph(n1, n2)

def random_acyclic_graph(n_node, edge_p):
    return ntx.erdos_renyi_graph(n_node, edge_p)


if __name__ == '__main__':

    ag = random_acyclic_graph(20, 0.5)
    print(ag)
    # show_graph(
    #     randomize_delay(ntx.complete_graph(20), 1, 20),
    #     [1,2,3],
        
    #     './'
    # )
    pass