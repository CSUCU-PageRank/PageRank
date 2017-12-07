# import some stuff
import numpy as np
import read_data as data


# keep it clean and tidy
def float_format(vector, decimal):
    return np.round((vector).astype(np.float), decimals=decimal)

def create_matrix(filename):
    a = data.ReadData(filename)
    file = a.open_file()
    return a.make_matrix(file)

# we have 3 webpages and probability of landing to each one is 1/3
# (defaultProbability)
M = create_matrix('data1.txt')
sizem = (np.sqrt(M.size)).astype(np.int64)
#print(sizem)
dp = 1/sizem
#print(dp)

E = np.zeros((sizem, sizem))
E[:] = dp
#print(E)

# taxation
beta = 0.7

# WWW matrix
A = (1-beta * M) + ( beta * E)

# initial vector
r = np.matrix([dp]*sizem)
#print(r)
r = np.transpose(r)

previous_r = r
for it in range(1, 100):
    r = A * r
    print(float_format(r, 3))
    # check if converged
    if (previous_r == r).all():
        break
    previous_r = r

summ = r.sum()
print("Final:\n", float_format(r, 3))
print("sum", np.round(summ), np.round(1.234567))
print("%.2f" % summ)