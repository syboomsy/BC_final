import networkx as ntx
import numpy as np
import random
import os.path as osp
import os
from tqdm import tqdm
from matplotlib import pyplot as plt
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
    random_acyclic_graph
)
from utils import plot_graph

def batch_test(
    trail_num = 10,
):
    greed_mean = []
    greed_minmax = []
    rand_mean = []
    rand_minmax = []

    rand_edge_p = 0.4
    rand_node_n = 30
    seed_k = 5

    for i in tqdm(range(trail_num)):
        graph = randomize_delay(random_acyclic_graph(rand_node_n, rand_edge_p), min_d=1, max_d=5)
        greedy_seeds = degree_discount_IC(graph, seed_k, p= 0.5)
        greedy_mean_mete = mean_delay(greedy_seeds, graph)
        greedy_minmax_mete = minmax_delay(greedy_seeds, graph)

        greed_mean.append(greedy_mean_mete)
        greed_minmax.append(greedy_minmax_mete)

        random_seeds = random_select(graph, seed_k)
        rand_mean_mete = mean_delay(random_seeds, graph)
        rand_minmax_mete = minmax_delay(random_seeds, graph)

        rand_mean.append(rand_mean_mete)
        rand_minmax.append(rand_minmax_mete)

    layout = ntx.spring_layout(graph) 
    plot_graph(graph,layout, greedy_seeds, 'greedy', './res')
    plot_graph(graph,layout, random_seeds, 'random', './res')

    gred_mean_sum = sum(greed_mean) / trail_num
    gred_minmax_sum = sum(greed_minmax)/ trail_num
    rand_mean_sum = sum(rand_mean)/ trail_num
    rand_minmax_sum = sum(rand_minmax)/ trail_num

    x = range(2)
    bar_width = 0.2
    plt.bar(x, [gred_mean_sum, gred_minmax_sum], width=bar_width, label=['greedy mean metric', 'random mean metric'])

    plt.bar([i + bar_width for i in x], [rand_mean_sum, rand_minmax_sum], width=bar_width, label=['greedy minmax metric', 'random minmax metric'])
    # # for i, value in enumerate([gred_mean_sum, gred_minmax_sum, rand_mean_sum, rand_minmax_sum]):
    #     plt.text(i % 2 + i // 2 * bar_width, value + 0.2, str(value), ha='center')

    plt.xlabel('Group')
    plt.ylabel('metric values')
    plt.title('Comparison of metric, node_num=30, edge_p=0.4, epoch=100')
    plt.xticks([i + 0.5*bar_width for i in x], ['greedy', 'random'])  # Assuming you want A and B labels for x-axis
    plt.legend()

    plt.savefig('./batch_test.png')
    plt.clf()



if __name__ == '__main__':
    batch_test(
        trail_num=100
    )