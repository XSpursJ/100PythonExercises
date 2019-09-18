# li = [1,2,3]
#
#
# for i in li:
#     for j in li:
#         for k in li:
#             if i != j and j != k and i != k:
#                 print([i,j,k])

import itertools
li = [1,2,3]

for x in itertools.permutations(li):
    print(list(x))
