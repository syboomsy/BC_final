import numpy as np
import networkx as ntx
import copy
from typing import Iterable
from ipdb import set_trace

def shortest_seed(graph:ntx.Graph, seed_set:Iterable, node_i:int):
    shortest_path = ntx.shortest_path_length(
        graph, node_i, weight='delay'
    )
    shortest_path_seed = [(x, shortest_path[x]) for x in seed_set]
    min_seed = min(shortest_path_seed, key=lambda x: x[-1])
    return min_seed
   

def mean_delay(seed_set:Iterable, graph:ntx.Graph):
    nodes = list(graph.nodes)
    nodes = [x for x in nodes if x not in seed_set]

    delays = [ 
        shortest_seed(graph, seed_set, x) for x in nodes
    ]
    sum_del = sum(x[-1] for x in delays)
    
    return sum_del / len(nodes)
    pass

def minmax_delay(seed_set:Iterable, graph:ntx.Graph):
    nodes = list(graph.nodes)
    nodes = [x for x in nodes if x not in seed_set]

    delays = [ 
        shortest_seed(graph, seed_set, x) for x in nodes
    ]
    max_del = max(delays, key=lambda x: x[-1])
    return max_del[-1]