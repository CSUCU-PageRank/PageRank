from pagerank import *
import matplotlib.pyplot as plt


def output_data(info):
    data = page_rank(info)
    res = power_iteration(data[0], data[1])
    return create_ranks(res)


def create_chart(info):
    """
    Creates a chart with top 10 pages.
    :param info: a tuple with all ranks, top ten ranks
    """
    lst = output_data(info)[1]
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


def save_to_csv(info):
    """
    Saves all ranks to a csv file.
    :param info: a tuple with all ranks, top ten ranks
    """
    all_ranks = sorted(output_data(info)[0], key=lambda x: x[1])
    with open('page_ranks.csv', 'w') as file:
        file.write('\t\t' + "Contains ranks of all pages" + '\n')
        for rank in all_ranks:
            file.write('Page number: ' + str(rank[1]) + ', page rank:' + str(rank[0]) + '\n')


data = 'data.txt'
print(output_data(data))
create_chart(data)
save_to_csv(data)
