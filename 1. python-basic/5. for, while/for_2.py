# 2단과 3단을 분리해서 list 형태로 변수에 담아보세요.

num2 = []

num3 = []

# 구구단 2,3 단
for i in range(2, 4):
    for j in range(1, 10):
        if i % 2 == 0:
            num2.append(str(i) + " * " + str(j) + " = " + str(i * j))
        else:
            num3.append(str(i) + " * " + str(j) + " = " + str(i * j))

print(num2)

print(num3)


num22 = []

num33 = []

# 구구단 2,3 단
for i in range(2, 4):
    for j in range(1, 10):
        result = str(i) + " * " + str(j) + " = " + str(i * j)
        if i % 2 == 0:
            num22.append(result)
        else:
            num33.append(result)

print(num22)

print(num33)
