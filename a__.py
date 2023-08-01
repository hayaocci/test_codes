import copy

a = [1,2 ]
b = copy.copy(a)
print(a, b)

a[0] = 100
print(a, b)