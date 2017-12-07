import numpy as np


class ReadData:

    def __init__(self, filename):
        """
        Creates an empty list.
        :param filename: the name of a file.
        """
        self.filename = filename

    def open_file(self):
        """
        Opens a file and saves all the information in a list
        (split by newlines).
        :return: a list with all the information from the file.
        """
        openfile = open(self.filename, encoding="utf-8")
        all_links = openfile.readlines()
        return all_links

    def make_matrix(self, lst):
        print(lst)
        z = np.empty([len(lst), len(lst)])
        for i in range(len(lst)):
            links = lst[i].split()
            for number in range(1, len(links)):
                if links[number] != '-1':
                    z[i][int(links[number])] = 1
        return z


a = ReadData("data1.txt")
file = a.open_file()
print(a.make_matrix(file))
