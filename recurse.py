# Software Design 2023.1 P36 より
import math


def factorial(n):
    # (3) 問題の解が自明な場合は再起呼び出しを行わないようにする
    if n == 0:
        return 1

    # (1) 問題を1段階簡単にしたうえで再起呼び出しを行う
    ret = factorial(n-1)

    # (2)再起呼び出しの結果を利用して問題を一段階だけ解く
    ans = n * ret

    return ans


print(math.factorial(10))
print(factorial(10))
