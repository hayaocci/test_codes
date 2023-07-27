
array = []

for i in range(20):
    array.append(0)

print(array)

for i in range(5):
    del array[0]
    array.append(i)

print(array)

sum_array = sum(array)

print(sum_array)