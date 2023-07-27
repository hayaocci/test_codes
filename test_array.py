
array = []

for i in range(20):
    array.append(0)

print(array)

for i in range(20):
    del array[0]
    array.append(i)

print(array)

sum_array = sum(array)

print(sum_array)

differential_array = []

for i in range(len(array)):
    differential = array[i] - array[i-1]
    differential_array.append(differential)

del differential_array[0]

print(len(differential_array))
print("differential array ", differential_array)