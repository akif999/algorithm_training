# Software Design 2023.1 P45 より


def fib1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n - 1) + fib1(n - 2)


# print(fib1(10))
# print(fib1(50))


fib_list_global = [0] * 101


def fib2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        if fib_list_global[n] == 0:
            fib_list_global[n] = fib2(n - 1) + fib2(n - 2)
        return fib_list_global[n]


print(fib2(50))
print(fib2(100))


def fib3(n):
    fib_list = [0] * (n + 1)  # nが小さいときの結果をメモするためのリスト
    fib_list[1] = 1  # 初期値a1 = 1(a0 = 0 は初期化時に代入済

    # 2番目からn番目の値を順番に求めていく
    for i in range(2, n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]

    return fib_list[n]  # 結果 an


print(fib3(50))
print(fib3(100))
