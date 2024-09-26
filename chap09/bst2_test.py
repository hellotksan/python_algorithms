# ２分探索木クラスBinarySearchTreeの利用例（その２）

from enum import Enum
from bst2 import BinarySearchTree

Menu = Enum('Menu', ['挿入', '削除', '探索', '昇順ダンプ', '降順ダンプ', 'キー範囲', '終了'])

def select_Menu() -> Menu:
    """メニュー選択"""
    s = [f'({m.value}){m.name}' for m in Menu]
    while True:
        print(*s, sep='  ', end='')
        n = int(input('：'))
        if 1 <= n <= len(Menu):
            return Menu(n)

tree = BinarySearchTree()                        # ２分探索木を生成

while True:
    menu = select_Menu()                         # メニュー選択

    if menu == Menu.挿入:                        # 挿入
        key = int(input('キー：'))
        val = input('値：')
        if not tree.add(key, val):
            print('挿入失敗！')

    elif menu == Menu.削除:                      # 削除
        key = int(input('キー：'))
        tree.remove(key)

    elif menu == Menu.探索:                      # 探索
        key = int(input('キー：'))
        t = tree.search(key)
        if t is not None:
            print(f'そのキーをもつ値は{t}です。')
        else:
            print('該当するデータはありません。')

    elif menu == Menu.昇順ダンプ:                # 昇順ダンプ
        tree.dump()

    elif menu == Menu.降順ダンプ:                # 降順ダンプ
        tree.dump(reverse = True)

    elif menu == Menu.キー範囲:                  # キー範囲（最小値と最大値）
        print(f'キーの最小値＝{tree.min_key()}')
        print(f'キーの最大値＝{tree.max_key()}')

    else:                                        # 終了
        break
