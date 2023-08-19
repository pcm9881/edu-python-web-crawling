num = 0

while num < 10:
    print(num)
    num = num + 1


# 무한루프 절대 하면 안되는 행위!

num = 0
count = 0

while num < 10:
    print(num)
    count = count + 1

    if count == 100:
        break
