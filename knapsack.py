# Software Design 2023.1 P42 より

# ナップザックの容量
C = 5


# 品物の価値と重量(v[i]とw[i]はそれぞれ品物iの価値と重量を表す)
v = [2, 4, 3]
w = [2, 2, 3]


# 品物の種類数
n = len(v)

# 空き容量cのナップザックに
# 品物iから品物n-1を入れる場合の最大価値を産出する関数


def knapsack(i, c):

    # (3) 問題の解が自明な場合は再起呼び出しを行わないようにする
    if i >= n:
        # i >= n の品物は存在しない
        return 0

    if c < w[i]:
        # 品物 i はナップザックに入らない

        # (1) 問題を1段階簡単にしたうえで再起呼び出しを行う
        # 品物iをナップザックに入れない場合の最大価値を取得
        no_put_value = knapsack(i + 1, c)

        # (2)再起呼び出しの結果を利用して問題を一段階だけ解く
        # 品物iはナップザックに入らないので入れる場合の価値は考慮不要
        max_value = no_put_value
    else:
        # (1) 問題を1段階簡単にしたうえで再起呼び出しを行う
        # 品物iをナップザックに入れない場合の最大価値を取得
        no_put_value = knapsack(i + 1, c)

        # 品物iをナップザックに入れる場合の最大価値を取得
        put_value = knapsack(i + 1, c - w[i])

        # (2)再起呼び出しの結果を利用して問題を一段階だけ解く
        # 品物iを入れる場合と入れない場合との大きいほうの価値を取得
        max_value = max(no_put_value, put_value + v[i])

    return max_value


def main():
    max_value = knapsack(0, C)
    print(max_value)


if __name__ == '__main__':
    main()
