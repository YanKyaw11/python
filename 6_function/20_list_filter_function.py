def check(arg):
    if arg % 3 == 0:
        return True
    else:
        return False

L = [1, 2, 3, 4, 10, 123, 22]

filtered = list(filter(check, L))

print(filtered)