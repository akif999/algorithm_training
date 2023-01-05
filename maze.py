# Software Design 2023.1 P38 より

map = [
    ['o', 'o', 'o', 'o', 'o', 'x', 'o', 'x',
        'o', 'o', 'o', 'x', 'o', 'o', 'o', 'o'],
    ['o', 'x', 'o', 'x', 'x', 'x', 'o', 'x',
        'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x'],
    ['o', 'x', 'o', 'o', 'o', 'o', 'o', 'x',
        'o', 'x', 'o', 'o', 'o', 'x', 'o', 'o'],
    ['o', 'o', 'x', 'x', 'o', 'x', 'x', 'x',
        'o', 'x', 'x', 'x', 'x', 'x', 'x', 'o'],
    ['x', 'o', 'x', 'x', 'o', 'o', 'o', 'o',
        'o', 'o', 'o', 'o', 'o', 'x', 'o', 'o'],
    ['o', 'o', 'o', 'x', 'o', 'x', 'x', 'x',
        'o', 'x', 'x', 'o', 'x', 'o', 'o', 'x'],
    ['x', 'o', 'x', 'x', 'o', 'x', 'o', 'x',
        'o', 'x', 'x', 'o', 'x', 'o', 'x', 'x'],
    ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
        'o', 'x', 'o', 'o', 'x', 'o', 'o', 'G'],
]

WIDTH = len(map[0])
HEIGHT = len(map)


def maze(start, map):
    i, j = start

    if i < 0 or i >= WIDTH or j < 0 or j >= HEIGHT:  # 現在位置が迷路外
        return False

    if map[j][i] == 'p':  # 電材位置は既に通過している
        return False

    if map[j][i] == 'x':  # 現在位置は壁である
        return False

    if map[j][i] == 'G':  # 現在位置はゴールである
        return True

    # 電材位置を既に通過済みとして問題を簡単にする
    map[j][i] = 'p'

    # 現在位置の上下左右の位置をスタートとしてゴールに到達可能かを調べる
    is_goaled_left = maze((i - 1, j), map)
    is_goaled_right = maze((i + 1, j), map)
    is_goaled_up = maze((i, j - 1), map)
    is_goaled_down = maze((i, j + 1), map)

    if is_goaled_left or is_goaled_right or is_goaled_up or is_goaled_down:
        is_goaled = True
    else:
        is_goaled = False

    return is_goaled


def main():
    start = (8, 4)
    isGoal = maze(start, map)
    if isGoal:
        print('ゴールに到達可能です')
    else:
        print('ゴールに到達できません')


if __name__ == '__main__':
    main()
