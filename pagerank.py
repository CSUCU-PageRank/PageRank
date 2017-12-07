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
M = create_matrix('data_inv.txt')
sizem = (np.sqrt(M.size)).astype(np.int64)
#print(sizem)
dp = 1/sizem
#print(dp)

E = np.zeros((sizem, sizem))
E[:] = dp
#print(E)

# taxation
beta = 0.15

# WWW matrix
A = (beta * M) + ((1-beta) * E)
#print(A)

# initial vector
r = np.matrix([dp]*sizem)
#print(r)
r = np.transpose(r)
#print(r.sum())

previous_r = r
for it in range(1, 100):
    #print(r/np.linalg.norm(r))
    r = A * (r/r.sum())
    #print(r.sum())
    #print(float_format(r, 3))
    # check if converged
    if (previous_r == r).all():
        break
    previous_r = r


print("Final:\n", float_format(r, 3))
print("sum", np.round(r.sum()))
ranks = [float(i[0][0]) for i in r]
top_ten_ranks = list(reversed(sorted([(ranks[i], i) for i in range(len(ranks))])))[:10]

print(len(top_ten_ranks))
