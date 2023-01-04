# Software Design 2023.1 P33 より


# 定数B (基数)とM (除数)
B, M = 30, 1000003


# 文字列を30進法の整数値とみなし、そのハッシュ値を返す関数
def hash(S):
    res = 0  # ハッシュ値
    for c in S:
        # 英小文字を整数に変換する
        n = ord(c) - ord('a') + 1

        # resをB倍してnを足す
        res *= B
        res += n

        # Mで割った余を求める
        res %= M
    return res


# "algorithm", "ubmf"はともにハッシュ値が569196
print(hash("algorithm"))
print(hash("ubmf"))
