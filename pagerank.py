import numpy as np
import read_data as data


def create_matrix(filename):
    """
    Creates a reference matrix from data.
    :param filename: name of the text file where initial data is located
    :return: reference matrix A where if A[i, j] == 1 then
    that page j links to page i
    """
    a = data.ReadData(filename)
    file = a.open_file()
    return a.make_matrix(file)


def page_rank(filename, coeff=0.15):
    """
    Initializes a matrix from data and makes it suitable for future calculations
    (takes care of possible shortcomings in standard algorithm).
    :param filename: name of the text file where initial data is located
    :param coeff: standard coefficient reportedly used by Google, is used
    to take care of  dangling nodes
    :return: matrix that is used for further calculations, standard importance
    vector
    """
    init_ranks_matrix = create_matrix(filename)
    matrix_size = (np.sqrt(init_ranks_matrix.size)).astype(np.int64)
    std_importance = 1/matrix_size
    si_matrix = np.zeros((matrix_size, matrix_size))
    si_matrix[:] = std_importance

    upd_matrix = (coeff * init_ranks_matrix) + ((1-coeff) * si_matrix)
    std_vector = np.transpose(np.matrix([std_importance]*matrix_size))
    return upd_matrix, std_vector


def power_iteration(matrix, vector):
    """
    Computes an eigenvector using power method.
    :param matrix: link matrix
    :param vector: column vector with all entries 1/n,
    where n is number of links in initial data
    :return: matrix with final importance scores
    """
    previous_vector = vector
    for it in range(1, 100):
        vector = matrix * (vector/vector.sum())
        if (previous_vector == vector).all():
            break
        previous_vector = vector
    return vector


def create_ranks(matrix):
    """
    Returns all acquired data and top ten most important pages.
    :param matrix: matrix with final importance scores
    :return: all ranks, top ten ranks
    """
    ranks = [float(i[0][0]) for i in matrix]
    ranks = list(reversed(sorted([(ranks[i], i) for i in range(len(ranks))])))
    top_ten_ranks = ranks[:10]
    return ranks, top_ten_ranks
