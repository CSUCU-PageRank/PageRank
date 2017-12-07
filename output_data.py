from pagerank import *


def output_data():
    data = page_rank('data.txt')
    res = power_iteration(data[0], data[1])
    return create_top_ranks(res)
