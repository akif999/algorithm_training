# Software Design 2023.1 P31 より

# 双方向連結リストの各ノード
class Node:
    def __init__(self, value=''):
        self.next = None  # 次のノード
        self.prev = None  # 前のノード
        self.value = value  # ノードに不随している値


# 双方向連結リストの初期化
nil = Node()  # 何もないことを表すノードnilを用意する
nil.next = nil  # 初期状態ではnilの次がnilを指すようにする
nil.prev = nil  # 初期状態ではnilの前がnilを指すようにする


# ノードpの直後にノードvを挿入する
def insert(v, p):
    v.next = p.next
    (p.next).prev = v
    p.next = v
    v.prev = p


# ノードvを削除する
def erase(v):
    (v.prev).next = v.next
    v.next.prev = v.prev


# 連結リストの中身を順に出力する
def printList():
    values = []
    current = nil.next  # 先頭から出発
    while current != nil:
        values.append(current.value)
        current = current.next
    print(values)


# 図6に示す連結リストを作る
sato = Node('sato')
suzuki = Node('suzuki')
takahashi = Node('takahashi')
ito = Node('ito')
watanabe = Node('watanabe')
yamamoto = Node('yamamoto')
nodes = [yamamoto, watanabe, ito, takahashi, suzuki, sato]
for node in nodes:
    insert(node, nil)
print('Before: ')
printList()


# 「渡辺」ノードを削除する
erase(watanabe)
print('After: ')
printList()
