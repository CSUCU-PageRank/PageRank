from pagerank import *
import matplotlib.pyplot as plt


def output_data(info):
    data = page_rank(info)
    res = power_iteration(data[0], data[1])
    return create_top_ranks(res)


def create_chart(info):
    lst = output_data(info)
    plt.rcdefaults()
    objects = (lst[i][1] for i in range(len(lst)))
    y_pos = np.arange(10)
    performance = [lst[i][0] for i in range(len(lst))]
    plt.bar(y_pos, performance, color='r', align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Rank')
    plt.xlabel('Page number')
    plt.title('Top 10 pages')
    plt.show()


data = 'data.txt'
print(output_data(data))
create_chart(data)
