import numpy as np
import read_data as data


def create_matrix(filename):
    a = data.ReadData(filename)
    file = a.open_file()
    return a.make_matrix(file)


def page_rank(filename, coeff=0.15):
    init_ranks_matrix = create_matrix(filename)
    matrix_size = (np.sqrt(init_ranks_matrix.size)).astype(np.int64)
    std_importance = 1/matrix_size
    si_matrix = np.zeros((matrix_size, matrix_size))
    si_matrix[:] = std_importance

    upd_matrix = (coeff * init_ranks_matrix) + ((1-coeff) * si_matrix)
    std_vector = np.transpose(np.matrix([std_importance]*matrix_size))
    return upd_matrix, std_vector


def power_iteration(matrix, vector):
    previous_vector = vector
    for it in range(1, 100):
        vector = matrix * (vector/vector.sum())
        if (previous_vector == vector).all():
            break
        previous_vector = vector
    return vector


def create_top_ranks(matrix):
    ranks = [float(i[0][0]) for i in matrix]
    top_ten_ranks = list(reversed(sorted([(ranks[i], i) for i in range(len(ranks))])))[:10]
    return top_ten_ranks


def output_data():
    data = page_rank('data_inv.txt')
    res = power_iteration(data[0], data[1])
    return create_top_ranks(res)
