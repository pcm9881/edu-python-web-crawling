# 1, 2, 3, 4, 5
for i in [1, 2, 3, 4, 5]:
    print(i)

# 1, 2, 3, 4, 5
for i in range(1, 5):
    print(i)

# 구구단 2,3 단
for i in range(2, 4):
    for j in range(1, 10):
        print(str(i) + " * " + str(j) + " = " + str(i * j))
