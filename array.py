# Software Design 2023.1 P28 より

# 配列Aを宣言して、出力する
A = [3, 1, 4, 1, 5, 9, 2]
print(A)

# 2番目の要素を10に書き換えて、出力する
A[2] = 10
print(A)

# 挿入クエリ: 配列の末尾に7を挿入して、出力する
A.append(7)
print(A)

# 削除クエリ: 3番目の要素(1)削除して、出力する
del A[3]
print(A)

# 検索クエリ: 値10があるかどうかを検索する
if 10 in A:
    print('Yes')