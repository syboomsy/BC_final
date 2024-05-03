
import numpy as np
import networkx as ntx
import copy
from ipdb import set_trace


def degree_discount_IC(graph:ntx.Graph, seed_k:int, p:float):
    assert graph is not None
    seed_set = []
    
    degree = dict(graph.degree())
    ddv_dict = degree.copy()
    tv_dict = degree.copy()
    for k, _ in tv_dict.items():
        tv_dict[k] = 0
    
    nodes = list(graph.nodes())
    selected_dict = {k:False for k in nodes}

    for i in range(1,seed_k+1,1):
        max_ddv = -1e9
        u_node = None
        for v_node in nodes:
            if selected_dict[v_node]:
                continue
            if ddv_dict[v_node] > max_ddv:
                u_node = v_node
                max_ddv = ddv_dict[v_node]
        
        seed_set.append(u_node)
        selected_dict[u_node] = True

        u_neighbor = graph.neighbors(u_node) # iterator
        for nei in u_neighbor:
            if selected_dict[nei]:
                continue
            tv_dict[nei] += 1
            ddv_dict[nei] = \
                  degree[nei] - 2* tv_dict[nei] - (degree[nei] - tv_dict[nei])*tv_dict[nei] *p
            
        pass
    return seed_set


if __name__ == '__main__':

    testg = ntx.Graph()
    nodes = [1,2,3,4,5]
    edges = [[1,2], [1,4], [1,5], [3,5]]
    testg.add_edges_from(edges)
    testg.add_nodes_from(nodes)
    node_list = list(testg.nodes().data())
    edge_list = list(testg.edges().data())
    degree = dict(testg.degree())

    set_trace()
    s_ret = ntx.shortest_path_length(testg, 1,)

    seed_set = degree_discount_IC(testg, 1, 0.5)
    set_trace()
    pass