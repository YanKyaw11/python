L = [1, 2, 3, 4, 10, 123, 22]

N = []

for x in L:
    if x % 3 == 0:
        N.append(x)

print(N)