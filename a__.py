import time

# t_start = time.time()

# while time.time() - t_start < 20:
#     num = int(input())

#     if num != 0:
#         print("Hello")
#     else:
#         print("Bye")
#         break

# print("Broke out of loop")

# CONST = 10

# def test():
#     print(CONST)

# test()

# def test2(count):
#     print(count)
#     count += 1
#     return count

# count = 0
# while True:
#     count = test2(count)
#     if count == 11:
#         break

# s = 0

# print(f'{s}m')

print('Start')
t_start = time.time()
count = 0

while True:
    if time.time() - t_start > 10:
        break
    
    print(count)
    count += 1
    time.sleep(1)