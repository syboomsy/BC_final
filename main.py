import networkx as ntx
import numpy as np
import random
import os.path as osp
import os
from ipdb import set_trace

from central_select import degree_discount_IC
from random_select import random_select

from metric import (
    mean_delay,
    minmax_delay
)

from utils import (
    randomize_delay,
    complete_bipartite,
    complete_graph,
    barbell_graph,
)
from utils import plot_graph


if __name__ == '__main__':

    # create graph
    graph = barbell_graph(4,8)
    # assign random delay between 0 and 10 to edges in the graph
    graph = randomize_delay(graph, min_d=0, max_d=10)
    # c_nodes = list(graph.nodes)
    # c_edges = list(graph.edges.data())
    # set_trace()

    # greedy algo test
    seed_k = 5
    greedy_seeds = degree_discount_IC(graph, seed_k, p= 0.5)
    # greedy algo metrics
    greedy_mean_mete = mean_delay(greedy_seeds, graph)
    greedy_minmax_mete = minmax_delay(greedy_seeds, graph)
    # save fig
    plot_graph(graph, greedy_seeds, 'greedy','./res', False)
    print("greedy mean mete: {}, minmax mete: {}".format(greedy_mean_mete, greedy_minmax_mete))

    # random algo test
    random_seeds = random_select(graph, seed_k)
    rand_mean_mete = mean_delay(random_seeds, graph)
    rand_minmax_mete = minmax_delay(random_seeds, graph)
    plot_graph(graph, random_seeds, 'rand','./res', False)
    print("random mean mete: {}, minmax mete: {}".format(rand_mean_mete, rand_minmax_mete))
    pass