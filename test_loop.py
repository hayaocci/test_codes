
def test(r):
    while r > 0:
        print(r)
        r -= 1


def test2():
     for i in range(10):
        print("右回転" + str(i+1))
    
if __name__ == "__main__":
    test(3)