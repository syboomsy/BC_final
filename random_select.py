import numpy as np
import networkx as ntx
import copy
import random
from ipdb import set_trace


def random_select(graph:ntx.Graph, seek_k:int):
    nodes = list(graph.nodes)
    random.shuffle(nodes)
    return nodes[:seek_k]