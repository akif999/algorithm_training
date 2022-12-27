# Software Design 2023.1 P21 より

# 線形探索
def liner_search(data, key):
    position = 0
    end = len(data) - 1
    steps = 1  # ステップ数
    while position <= end:
        if data[position] == key:
            return steps, position
        steps += 1  # ステップ数を1増やす
        position += 1  # 位置を1つ増やす
    return steps, -1


# 二分探索
def binary_search(data, key):
    start = 0  # 最初の位置
    end = len(data) - 1  # 最後の位置
    steps = 1  # ステップ数
    while start <= end:
        middle = (start + end) // 2  # 配列の中央値を求める
        if data[middle] == key:  # 中央値と探索値が一致したら発見
            return steps, middle
        elif data[middle] < key:  # 中央値が探索値よりも小さい場合
            start = middle + 1
        else:  # 中央値が探索地よりも大きい場合
            end = middle - 1
        steps += 1  # ステップ数を1増やす
    return steps, -1


# 探索の実行と最大ステップ数を求める処理
def search(title, data, func):
    print(title)
    max_steps = 1
    for key in data:
        steps, pos = func(data, key)
        if max_steps < steps:
            max_steps = steps
        print("key:{} position:{} steps:{}".format(key, pos, steps))
    print("最大ステップ数:{}\n".format(max_steps))
    return


if __name__ == '__main__':
    data = [1, 3, 7, 13, 17, 21, 74]  # 探索するデータ
    length = len(data)
    print("探索データ:{}\n長さ:{}\n".format(data, length))
    search("線形探索", data, liner_search)
    search("二分木探索", data, binary_search)
